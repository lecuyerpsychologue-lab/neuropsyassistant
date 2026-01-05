"""
Module UI pour la génération du rapport.
"""

import streamlit as st
import plotly.graph_objects as go
from utils.semantic_engine import generate_rapport_complet
from models.scores import ScoreType
from models.interpretations import get_couleur_score, est_cliniquement_significatif


def render_rapport_module():
    """Affiche le module de génération de rapport."""
    
    st.title("📄 Génération du Rapport Clinique")
    
    # Vérifier que les données nécessaires sont présentes
    if 'patient' not in st.session_state or 'anamnese' not in st.session_state:
        st.error("⚠️ Veuillez d'abord renseigner les informations patient et l'anamnèse")
        return
    
    patient = st.session_state.patient
    anamnese = st.session_state.anamnese
    
    # Récupérer tous les managers
    managers = {}
    
    if 'wisc_v_manager' in st.session_state:
        managers['wisc_v'] = st.session_state.wisc_v_manager
    
    if 'kabc_ii_manager' in st.session_state:
        managers['kabc_ii'] = st.session_state.kabc_ii_manager
    
    if 'teach_manager' in st.session_state:
        managers['teach'] = st.session_state.teach_manager
    
    if 'nepsy_ii_manager' in st.session_state:
        managers['nepsy_ii'] = st.session_state.nepsy_ii_manager
    
    if 'brown_manager' in st.session_state:
        managers['brown'] = st.session_state.brown_manager
    
    if 'conners_parent_manager' in st.session_state:
        managers['conners_parent'] = st.session_state.conners_parent_manager
    
    if 'conners_teacher_manager' in st.session_state:
        managers['conners_teacher'] = st.session_state.conners_teacher_manager
    
    # Vérifier qu'au moins un test a été complété
    has_tests = any(m.has_scores() for m in managers.values())
    
    if not has_tests:
        st.warning("⚠️ Aucun test n'a été complété. Veuillez saisir au moins un score dans les modules de tests.")
        return
    
    # Résumé des données disponibles
    st.subheader("📊 Données Disponibles")
    
    with st.expander("Voir le résumé", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Patient :**")
            if patient.format_nom_complet():
                st.write(f"✅ {patient.format_nom_complet()}")
            else:
                st.write("⚠️ Nom non renseigné")
            
            st.markdown("**Tests cognitifs :**")
            if 'wisc_v' in managers and managers['wisc_v'].has_scores():
                st.write(f"✅ WISC-V ({len(managers['wisc_v'].get_valid_scores())} scores)")
            
            if 'kabc_ii' in managers and managers['kabc_ii'].has_scores():
                st.write(f"✅ KABC-II ({len(managers['kabc_ii'].get_valid_scores())} scores)")
        
        with col2:
            st.markdown("**Tests attentionnels :**")
            if 'teach' in managers and managers['teach'].has_scores():
                st.write(f"✅ TEA-Ch ({len(managers['teach'].get_valid_scores())} scores)")
            
            if 'nepsy_ii' in managers and managers['nepsy_ii'].has_scores():
                st.write(f"✅ NEPSY-II ({len(managers['nepsy_ii'].get_valid_scores())} scores)")
            
            st.markdown("**Questionnaires comportementaux :**")
            if 'brown' in managers and managers['brown'].has_scores():
                st.write(f"✅ Brown ({len(managers['brown'].get_valid_scores())} scores)")
            
            if 'conners_parent' in managers and managers['conners_parent'].has_scores():
                st.write(f"✅ Conners Parent ({len(managers['conners_parent'].get_valid_scores())} scores)")
            
            if 'conners_teacher' in managers and managers['conners_teacher'].has_scores():
                st.write(f"✅ Conners Enseignant ({len(managers['conners_teacher'].get_valid_scores())} scores)")
    
    # Visualisations
    st.subheader("📈 Visualisations")
    
    # Graphique WISC-V
    if 'wisc_v' in managers and managers['wisc_v'].has_scores():
        with st.expander("Profil WISC-V", expanded=True):
            render_wisc_profile_chart(managers['wisc_v'])
    
    # Graphique comparaison Conners
    if ('conners_parent' in managers and managers['conners_parent'].has_scores() and
        'conners_teacher' in managers and managers['conners_teacher'].has_scores()):
        with st.expander("Comparaison Parent / Enseignant (Conners)", expanded=True):
            render_conners_comparison_chart(managers['conners_parent'], managers['conners_teacher'])
    
    # Génération du rapport
    st.subheader("📝 Rapport Clinique")
    
    if st.button("🔄 Générer le Rapport", type="primary", use_container_width=True):
        with st.spinner("Génération du rapport en cours..."):
            try:
                rapport = generate_rapport_complet(patient, anamnese, **managers)
                
                st.session_state.rapport_genere = rapport
                st.success("✅ Rapport généré avec succès !")
            
            except Exception as e:
                st.error(f"❌ Erreur lors de la génération du rapport : {str(e)}")
                return
    
    # Affichage et téléchargement du rapport
    if 'rapport_genere' in st.session_state:
        st.markdown("---")
        
        # Aperçu du rapport
        with st.expander("👁️ Aperçu du Rapport", expanded=False):
            st.markdown(st.session_state.rapport_genere)
        
        # Bouton de téléchargement
        st.download_button(
            label="📥 Télécharger le Rapport (Markdown)",
            data=st.session_state.rapport_genere,
            file_name=f"rapport_{patient.nom}_{patient.prenom}.md".replace(" ", "_"),
            mime="text/markdown",
            use_container_width=True
        )
        
        st.info("💡 Le rapport a été généré au format Markdown. Vous pouvez l'ouvrir avec un éditeur de texte "
               "ou le convertir en PDF avec un outil comme Pandoc.")


def render_wisc_profile_chart(wisc_v_manager):
    """Génère un graphique du profil WISC-V."""
    
    indices = ["ICV", "IVS", "IRF", "IMT", "IVT"]
    scores_data = []
    labels = []
    colors = []
    
    for idx in indices:
        score = wisc_v_manager.get_score(idx)
        if score and score.is_valid():
            scores_data.append(score.valeur)
            labels.append(idx)
            colors.append(get_couleur_score(score.classification, ScoreType.STANDARD))
    
    if not scores_data:
        st.info("Aucun indice WISC-V renseigné")
        return
    
    # Créer le graphique
    fig = go.Figure()
    
    # Zones de référence
    fig.add_hrect(y0=130, y1=160, fillcolor="lightgreen", opacity=0.1, line_width=0, annotation_text="Très Supérieur")
    fig.add_hrect(y0=120, y1=130, fillcolor="lightgreen", opacity=0.15, line_width=0, annotation_text="Supérieur")
    fig.add_hrect(y0=110, y1=120, fillcolor="lightblue", opacity=0.1, line_width=0, annotation_text="Moyen Fort")
    fig.add_hrect(y0=90, y1=110, fillcolor="lightyellow", opacity=0.1, line_width=0, annotation_text="Moyen")
    fig.add_hrect(y0=80, y1=90, fillcolor="lightyellow", opacity=0.15, line_width=0, annotation_text="Moyen Faible")
    fig.add_hrect(y0=70, y1=80, fillcolor="lightcoral", opacity=0.1, line_width=0, annotation_text="Limite")
    fig.add_hrect(y0=40, y1=70, fillcolor="lightcoral", opacity=0.15, line_width=0, annotation_text="Très Faible")
    
    # Barres horizontales
    fig.add_trace(go.Bar(
        y=labels,
        x=scores_data,
        orientation='h',
        marker=dict(color=colors),
        text=scores_data,
        textposition='auto',
        hovertemplate='<b>%{y}</b><br>Score: %{x}<extra></extra>'
    ))
    
    fig.update_layout(
        title="Profil WISC-V - Indices Principaux",
        xaxis_title="Score Standard",
        yaxis_title="Indice",
        xaxis=dict(range=[40, 160]),
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_conners_comparison_chart(conners_parent, conners_teacher):
    """Génère un graphique de comparaison Parent/Enseignant."""
    
    from config.constants import CONNERS_3_ECHELLES
    
    echelles = []
    scores_parent = []
    scores_teacher = []
    
    for echelle in CONNERS_3_ECHELLES:
        score_p = conners_parent.get_score(echelle)
        score_t = conners_teacher.get_score(echelle)
        
        if score_p and score_p.is_valid() and score_t and score_t.is_valid():
            echelles.append(echelle)
            scores_parent.append(score_p.valeur)
            scores_teacher.append(score_t.valeur)
    
    if not echelles:
        st.info("Pas de données comparables entre Parent et Enseignant")
        return
    
    fig = go.Figure()
    
    # Zones de référence
    fig.add_hrect(y0=70, y1=80, fillcolor="lightcoral", opacity=0.1, line_width=0, annotation_text="Très Élevé")
    fig.add_hrect(y0=65, y1=70, fillcolor="lightcoral", opacity=0.15, line_width=0, annotation_text="Élevé")
    fig.add_hrect(y0=60, y1=65, fillcolor="lightyellow", opacity=0.1, line_width=0, annotation_text="Moyen Haut")
    fig.add_hrect(y0=40, y1=60, fillcolor="lightgreen", opacity=0.1, line_width=0, annotation_text="Moyen")
    
    fig.add_trace(go.Bar(
        x=echelles,
        y=scores_parent,
        name='Parent',
        marker_color='#FF6B6B'
    ))
    
    fig.add_trace(go.Bar(
        x=echelles,
        y=scores_teacher,
        name='Enseignant',
        marker_color='#4ECDC4'
    ))
    
    fig.update_layout(
        title="Comparaison Parent / Enseignant - Conners-3",
        xaxis_title="Échelle",
        yaxis_title="Score T",
        yaxis=dict(range=[30, 80]),
        barmode='group',
        height=500,
        xaxis_tickangle=-45
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Analyse des divergences
    divergences = []
    for i, echelle in enumerate(echelles):
        diff = abs(scores_parent[i] - scores_teacher[i])
        if diff >= 10:
            divergences.append((echelle, diff))
    
    if divergences:
        st.warning(f"⚠️ {len(divergences)} échelle(s) avec divergence(s) notable(s) (écart ≥10 points)")
        for echelle, diff in divergences:
            st.write(f"- {echelle}: écart de {diff:.0f} points")
    else:
        st.success("✅ Bonne convergence entre les informateurs")
