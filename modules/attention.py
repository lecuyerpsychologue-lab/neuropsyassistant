"""
Module UI pour les tests d'attention (TEA-Ch et NEPSY-II).
"""

import streamlit as st
import pandas as pd
from models.scores import Score, ScoreManager, ScoreType
from models.interpretations import get_classification, interprete_score
from config.constants import TEACH_STRUCTURE, NEPSY_II_STRUCTURE


def render_attention_module():
    """Affiche le module pour TEA-Ch et NEPSY-II."""
    
    st.title("👁️ Évaluation de l'Attention et des Fonctions Exécutives")
    
    # TEA-Ch
    st.header("🎯 TEA-Ch - Test d'Évaluation de l'Attention chez l'Enfant")
    
    if 'teach_manager' not in st.session_state:
        st.session_state.teach_manager = ScoreManager("TEA-Ch")
    
    teach_manager = st.session_state.teach_manager
    
    for categorie, subtests in TEACH_STRUCTURE.items():
        with st.expander(f"📌 {categorie}", expanded=False):
            for subtest in subtests:
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    valeur = st.number_input(
                        subtest,
                        min_value=1,
                        max_value=19,
                        value=10,
                        step=1,
                        key=f"teach_{subtest.replace(' ', '_')}"
                    )
                
                with col2:
                    renseigne = st.checkbox("✓", key=f"teach_{subtest.replace(' ', '_')}_renseigne")
                
                if renseigne:
                    classification, _ = get_classification(valeur, ScoreType.SCALAIRE)
                    interpretation = interprete_score(valeur, ScoreType.SCALAIRE, subtest.lower())
                    
                    score = Score(
                        nom=subtest,
                        valeur=valeur,
                        type_score=ScoreType.SCALAIRE,
                        domaine=subtest.lower(),
                        classification=classification,
                        interpretation=interpretation
                    )
                    teach_manager.add_score(score)
                    
                    st.info(f"{classification}")
    
    if teach_manager.has_scores():
        st.success("✅ Scores TEA-Ch enregistrés")
        
        # Tableau récapitulatif
        with st.expander("📋 Tableau Récapitulatif TEA-Ch"):
            valid_scores = teach_manager.get_valid_scores()
            if valid_scores:
                df_data = []
                for score in valid_scores:
                    df_data.append({
                        "Subtest": score.nom,
                        "Score": int(score.valeur),
                        "Classification": score.classification
                    })
                df = pd.DataFrame(df_data)
                st.dataframe(df, use_container_width=True)
    
    st.session_state.teach_manager = teach_manager
    
    # NEPSY-II
    st.header("🧩 NEPSY-II - Bilan Neuropsychologique de l'Enfant")
    
    if 'nepsy_ii_manager' not in st.session_state:
        st.session_state.nepsy_ii_manager = ScoreManager("NEPSY-II")
    
    nepsy_manager = st.session_state.nepsy_ii_manager
    
    for categorie, subtests in NEPSY_II_STRUCTURE.items():
        with st.expander(f"📌 {categorie}", expanded=False):
            for subtest in subtests:
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    valeur = st.number_input(
                        subtest,
                        min_value=1,
                        max_value=19,
                        value=10,
                        step=1,
                        key=f"nepsy_{subtest.replace(' ', '_')}"
                    )
                
                with col2:
                    renseigne = st.checkbox("✓", key=f"nepsy_{subtest.replace(' ', '_')}_renseigne")
                
                if renseigne:
                    classification, _ = get_classification(valeur, ScoreType.SCALAIRE)
                    interpretation = interprete_score(valeur, ScoreType.SCALAIRE, subtest.lower())
                    
                    score = Score(
                        nom=subtest,
                        valeur=valeur,
                        type_score=ScoreType.SCALAIRE,
                        domaine=subtest.lower(),
                        classification=classification,
                        interpretation=interpretation
                    )
                    nepsy_manager.add_score(score)
                    
                    st.info(f"{classification}")
    
    if nepsy_manager.has_scores():
        st.success("✅ Scores NEPSY-II enregistrés")
        
        # Tableau récapitulatif
        with st.expander("📋 Tableau Récapitulatif NEPSY-II"):
            valid_scores = nepsy_manager.get_valid_scores()
            if valid_scores:
                df_data = []
                for score in valid_scores:
                    df_data.append({
                        "Subtest": score.nom,
                        "Score": int(score.valeur),
                        "Classification": score.classification
                    })
                df = pd.DataFrame(df_data)
                st.dataframe(df, use_container_width=True)
    
    st.session_state.nepsy_ii_manager = nepsy_manager
