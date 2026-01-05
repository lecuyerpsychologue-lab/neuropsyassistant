"""
Module UI pour les questionnaires comportementaux (Brown et Conners-3).
"""

import streamlit as st
import pandas as pd
from models.scores import Score, ScoreManager, ScoreType
from models.interpretations import get_classification, interprete_score, est_cliniquement_significatif
from config.constants import BROWN_ECHELLES, CONNERS_3_ECHELLES


def render_comportement_module():
    """Affiche le module pour les questionnaires comportementaux."""
    
    st.title("📝 Évaluation Comportementale")
    
    # Brown
    st.header("🔵 Échelle Brown de Déficit d'Attention")
    
    if 'brown_manager' not in st.session_state:
        st.session_state.brown_manager = ScoreManager("Brown")
    
    brown_manager = st.session_state.brown_manager
    
    with st.expander("Échelles Brown (Scores T)", expanded=True):
        for echelle in BROWN_ECHELLES:
            col1, col2 = st.columns([2, 1])
            
            with col1:
                valeur = st.number_input(
                    echelle,
                    min_value=20,
                    max_value=80,
                    value=50,
                    step=1,
                    key=f"brown_{echelle.replace(' ', '_').replace('/', '_')}"
                )
            
            with col2:
                renseigne = st.checkbox("✓", key=f"brown_{echelle.replace(' ', '_').replace('/', '_')}_renseigne")
            
            if renseigne:
                classification, _ = get_classification(valeur, ScoreType.T_SCORE)
                interpretation = interprete_score(valeur, ScoreType.T_SCORE, echelle.lower())
                significatif = est_cliniquement_significatif(valeur, ScoreType.T_SCORE)
                
                score = Score(
                    nom=echelle,
                    valeur=valeur,
                    type_score=ScoreType.T_SCORE,
                    domaine=echelle.lower(),
                    classification=classification,
                    interpretation=interpretation
                )
                brown_manager.add_score(score)
                
                if significatif:
                    st.error(f"⚠️ **{classification}** - Cliniquement significatif")
                else:
                    st.success(f"✅ {classification}")
    
    if brown_manager.has_scores():
        st.success("✅ Scores Brown enregistrés")
        
        # Tableau récapitulatif
        with st.expander("📋 Tableau Récapitulatif Brown"):
            valid_scores = brown_manager.get_valid_scores()
            if valid_scores:
                df_data = []
                for score in valid_scores:
                    significatif = est_cliniquement_significatif(score.valeur, ScoreType.T_SCORE)
                    df_data.append({
                        "Échelle": score.nom,
                        "Score T": int(score.valeur),
                        "Classification": score.classification,
                        "Significatif": "⚠️ Oui" if significatif else "Non"
                    })
                df = pd.DataFrame(df_data)
                st.dataframe(df, use_container_width=True)
    
    st.session_state.brown_manager = brown_manager
    
    # Conners-3
    st.header("🔴 Échelle Conners-3")
    
    st.info("💡 Renseignez les scores pour les versions Parent ET Enseignant si disponibles")
    
    # Conners-3 Parent
    st.subheader("👨‍👩‍👧 Version Parent")
    
    if 'conners_parent_manager' not in st.session_state:
        st.session_state.conners_parent_manager = ScoreManager("Conners-3 Parent")
    
    conners_parent = st.session_state.conners_parent_manager
    
    with st.expander("Échelles Conners-3 Parent (Scores T)", expanded=False):
        for echelle in CONNERS_3_ECHELLES:
            col1, col2 = st.columns([2, 1])
            
            with col1:
                valeur = st.number_input(
                    echelle,
                    min_value=20,
                    max_value=80,
                    value=50,
                    step=1,
                    key=f"conners_parent_{echelle.replace(' ', '_').replace('/', '_')}"
                )
            
            with col2:
                renseigne = st.checkbox("✓", key=f"conners_parent_{echelle.replace(' ', '_').replace('/', '_')}_renseigne")
            
            if renseigne:
                classification, _ = get_classification(valeur, ScoreType.T_SCORE)
                interpretation = interprete_score(valeur, ScoreType.T_SCORE, echelle.lower())
                significatif = est_cliniquement_significatif(valeur, ScoreType.T_SCORE)
                
                score = Score(
                    nom=echelle,
                    valeur=valeur,
                    type_score=ScoreType.T_SCORE,
                    domaine=echelle.lower(),
                    classification=classification,
                    interpretation=interpretation
                )
                conners_parent.add_score(score)
                
                if significatif:
                    st.error(f"⚠️ **{classification}** - Cliniquement significatif")
                else:
                    st.success(f"✅ {classification}")
    
    if conners_parent.has_scores():
        st.success("✅ Scores Conners-3 Parent enregistrés")
    
    st.session_state.conners_parent_manager = conners_parent
    
    # Conners-3 Enseignant
    st.subheader("👨‍🏫 Version Enseignant")
    
    if 'conners_teacher_manager' not in st.session_state:
        st.session_state.conners_teacher_manager = ScoreManager("Conners-3 Enseignant")
    
    conners_teacher = st.session_state.conners_teacher_manager
    
    with st.expander("Échelles Conners-3 Enseignant (Scores T)", expanded=False):
        for echelle in CONNERS_3_ECHELLES:
            col1, col2 = st.columns([2, 1])
            
            with col1:
                valeur = st.number_input(
                    echelle,
                    min_value=20,
                    max_value=80,
                    value=50,
                    step=1,
                    key=f"conners_teacher_{echelle.replace(' ', '_').replace('/', '_')}"
                )
            
            with col2:
                renseigne = st.checkbox("✓", key=f"conners_teacher_{echelle.replace(' ', '_').replace('/', '_')}_renseigne")
            
            if renseigne:
                classification, _ = get_classification(valeur, ScoreType.T_SCORE)
                interpretation = interprete_score(valeur, ScoreType.T_SCORE, echelle.lower())
                significatif = est_cliniquement_significatif(valeur, ScoreType.T_SCORE)
                
                score = Score(
                    nom=echelle,
                    valeur=valeur,
                    type_score=ScoreType.T_SCORE,
                    domaine=echelle.lower(),
                    classification=classification,
                    interpretation=interpretation
                )
                conners_teacher.add_score(score)
                
                if significatif:
                    st.error(f"⚠️ **{classification}** - Cliniquement significatif")
                else:
                    st.success(f"✅ {classification}")
    
    if conners_teacher.has_scores():
        st.success("✅ Scores Conners-3 Enseignant enregistrés")
    
    st.session_state.conners_teacher_manager = conners_teacher
    
    # Comparaison Parent vs Enseignant
    if conners_parent.has_scores() and conners_teacher.has_scores():
        st.subheader("🔍 Comparaison Parent / Enseignant")
        
        with st.expander("Analyse Croisée"):
            comparison_data = []
            
            for echelle in CONNERS_3_ECHELLES:
                score_parent = conners_parent.get_score(echelle)
                score_teacher = conners_teacher.get_score(echelle)
                
                if score_parent and score_parent.is_valid() and score_teacher and score_teacher.is_valid():
                    diff = abs(score_parent.valeur - score_teacher.valeur)
                    convergence = "✅ Convergent" if diff < 10 else "⚠️ Divergent"
                    
                    comparison_data.append({
                        "Échelle": echelle,
                        "Parent (T)": int(score_parent.valeur),
                        "Enseignant (T)": int(score_teacher.valeur),
                        "Écart": int(diff),
                        "Convergence": convergence
                    })
            
            if comparison_data:
                df_comp = pd.DataFrame(comparison_data)
                st.dataframe(df_comp, use_container_width=True)
                
                divergents = [d for d in comparison_data if "Divergent" in d["Convergence"]]
                if divergents:
                    st.warning(f"⚠️ {len(divergents)} échelle(s) présentent des divergences notables entre les informateurs")
                else:
                    st.success("✅ Convergence globale entre les informateurs")
