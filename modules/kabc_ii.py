"""
Module UI pour le KABC-II.
"""

import streamlit as st
import pandas as pd
from models.scores import Score, ScoreManager, ScoreType
from models.interpretations import get_classification, interprete_score
from config.constants import KABC_II_STRUCTURE


def render_kabc_ii_module():
    """Affiche le module KABC-II."""
    
    st.title("🎯 KABC-II - Batterie d'Évaluation de Kaufman pour Enfants")
    
    # Initialisation
    if 'kabc_ii_manager' not in st.session_state:
        st.session_state.kabc_ii_manager = ScoreManager("KABC-II")
    
    manager = st.session_state.kabc_ii_manager
    
    st.info("💡 Saisissez les scores obtenus aux différents indices du KABC-II")
    
    # Tous les indices KABC-II
    indices = ["IFC", "ISQ", "ISI", "IPL", "IAP", "ICO"]
    
    for idx in indices:
        info = KABC_II_STRUCTURE[idx]
        with st.expander(f"{idx} - {info['nom']}", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                valeur = st.number_input(
                    f"Score {idx}",
                    min_value=40,
                    max_value=160,
                    value=100,
                    step=1,
                    key=f"kabc_ii_{idx}"
                )
            
            with col2:
                renseigne = st.checkbox("Renseigné", key=f"kabc_ii_{idx}_renseigne")
            
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
    
    # Analyse du profil
    if manager.has_scores():
        st.subheader("🔍 Analyse du Profil")
        
        hetero = manager.calculate_profile_heterogeneity(indices)
        
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
        
        valid_scores = manager.get_valid_scores()
        
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
    
    st.session_state.kabc_ii_manager = manager
    
    if manager.has_scores():
        st.success("✅ Scores KABC-II enregistrés")
