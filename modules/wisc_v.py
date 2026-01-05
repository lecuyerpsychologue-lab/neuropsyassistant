"""
Module UI pour le WISC-V.
"""

import streamlit as st
import pandas as pd
from models.scores import Score, ScoreManager, ScoreType
from models.interpretations import get_classification, interprete_score
from config.constants import WISC_V_STRUCTURE


def render_wisc_v_module():
    """Affiche le module WISC-V."""
    
    st.title("🧠 WISC-V - Échelle d'Intelligence de Wechsler pour Enfants")
    
    # Initialisation
    if 'wisc_v_manager' not in st.session_state:
        st.session_state.wisc_v_manager = ScoreManager("WISC-V")
    
    manager = st.session_state.wisc_v_manager
    
    st.info("💡 Saisissez les scores obtenus aux différents indices et subtests du WISC-V")
    
    # Indices principaux
    st.subheader("📊 Indices Principaux (Notes Standard)")
    
    indices_principaux = ["ICV", "IVS", "IRF", "IMT", "IVT"]
    
    for idx in indices_principaux:
        info = WISC_V_STRUCTURE[idx]
        with st.expander(f"{idx} - {info['nom']}", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                valeur = st.number_input(
                    f"Score {idx}",
                    min_value=40,
                    max_value=160,
                    value=100,
                    step=1,
                    key=f"wisc_v_{idx}"
                )
            
            with col2:
                renseigne = st.checkbox("Renseigné", key=f"wisc_v_{idx}_renseigne")
            
            if renseigne:
                classification, percentile = get_classification(valeur, ScoreType.STANDARD)
                interpretation = interprete_score(valeur, ScoreType.STANDARD, info['domaine'])
                
                score = Score(
                    nom=idx,
                    valeur=valeur,
                    type_score=ScoreType.STANDARD,
                    domaine=info['domaine'],
                    percentile=percentile,
                    classification=classification,
                    interpretation=interpretation
                )
                manager.add_score(score)
                
                st.success(f"**{classification}** (Percentile: {percentile})")
                st.write(interpretation)
            
            # Subtests
            if info['subtests']:
                st.markdown("**Subtests (Notes Scalaires) :**")
                for subtest in info['subtests']:
                    col_s1, col_s2 = st.columns([2, 1])
                    
                    with col_s1:
                        val_sub = st.number_input(
                            subtest,
                            min_value=1,
                            max_value=19,
                            value=10,
                            step=1,
                            key=f"wisc_v_subtest_{subtest.replace(' ', '_')}"
                        )
                    
                    with col_s2:
                        rens_sub = st.checkbox("✓", key=f"wisc_v_subtest_{subtest.replace(' ', '_')}_renseigne")
                    
                    if rens_sub:
                        class_sub, _ = get_classification(val_sub, ScoreType.SCALAIRE)
                        interp_sub = interprete_score(val_sub, ScoreType.SCALAIRE, subtest.lower())
                        
                        score_sub = Score(
                            nom=f"{idx}_{subtest}",
                            valeur=val_sub,
                            type_score=ScoreType.SCALAIRE,
                            domaine=subtest.lower(),
                            classification=class_sub,
                            interpretation=interp_sub
                        )
                        manager.add_score(score_sub)
    
    # Indices complémentaires
    st.subheader("📈 Indices Complémentaires (Notes Standard)")
    
    indices_complementaires = ["IQT", "IRQ", "IMTA", "INV", "IAG", "ICC"]
    
    with st.expander("Indices Complémentaires"):
        for idx in indices_complementaires:
            info = WISC_V_STRUCTURE[idx]
            col1, col2 = st.columns([2, 1])
            
            with col1:
                valeur = st.number_input(
                    f"{idx} - {info['nom']}",
                    min_value=40,
                    max_value=160,
                    value=100,
                    step=1,
                    key=f"wisc_v_{idx}"
                )
            
            with col2:
                renseigne = st.checkbox("Renseigné", key=f"wisc_v_{idx}_renseigne")
            
            if renseigne:
                classification, percentile = get_classification(valeur, ScoreType.STANDARD)
                interpretation = interprete_score(valeur, ScoreType.STANDARD, info['domaine'])
                
                score = Score(
                    nom=idx,
                    valeur=valeur,
                    type_score=ScoreType.STANDARD,
                    domaine=info['domaine'],
                    percentile=percentile,
                    classification=classification,
                    interpretation=interpretation
                )
                manager.add_score(score)
    
    # Analyse de l'homogénéité
    if manager.has_scores():
        st.subheader("🔍 Analyse du Profil")
        
        hetero = manager.calculate_profile_heterogeneity(indices_principaux)
        
        if hetero['is_homogeneous']:
            st.success(f"✅ **Profil homogène** (écart maximal: {hetero['ecart_max']:.0f} points)")
        else:
            st.warning(f"⚠️ **Profil hétérogène** (écart maximal: {hetero['ecart_max']:.0f} points)")
            
            if hetero['scores_min'] and hetero['scores_max']:
                min_scores = ", ".join([s.nom for s in hetero['scores_min']])
                max_scores = ", ".join([s.nom for s in hetero['scores_max']])
                st.write(f"- **Points faibles :** {min_scores} ({hetero['scores_min'][0].valeur:.0f})")
                st.write(f"- **Points forts :** {max_scores} ({hetero['scores_max'][0].valeur:.0f})")
        
        # Tableau récapitulatif
        st.subheader("📋 Tableau Récapitulatif")
        
        valid_scores = [s for s in manager.get_valid_scores() if s.type_score == ScoreType.STANDARD]
        
        if valid_scores:
            df_data = []
            for score in valid_scores:
                df_data.append({
                    "Indice": score.nom,
                    "Score": int(score.valeur),
                    "Classification": score.classification,
                    "Percentile": score.percentile or "-"
                })
            
            df = pd.DataFrame(df_data)
            st.dataframe(df, use_container_width=True)
    
    st.session_state.wisc_v_manager = manager
    
    if manager.has_scores():
        st.success("✅ Scores WISC-V enregistrés")
