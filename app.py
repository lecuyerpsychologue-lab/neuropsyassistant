"""
NeuroPsy Assist - Application Streamlit principale.
Application complète pour neuropsychologues permettant la saisie de données d'anamnèse,
de scores de tests psychométriques, et la génération automatique de rapports cliniques.
"""

import streamlit as st
from modules.anamnese import render_anamnese_module
from modules.wisc_v import render_wisc_v_module
from modules.kabc_ii import render_kabc_ii_module
from modules.attention import render_attention_module
from modules.comportement import render_comportement_module
from modules.rapport import render_rapport_module


# Configuration de la page
st.set_page_config(
    page_title="NeuroPsy Assist",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)


def main():
    """Fonction principale de l'application."""
    
    # Titre de l'application
    st.markdown('<p class="main-header">🧠 NeuroPsy Assist</p>', unsafe_allow_html=True)
    st.markdown("### Assistant de rédaction de comptes-rendus neuropsychologiques")
    st.markdown("---")
    
    # Sidebar de navigation
    with st.sidebar:
        st.image("https://via.placeholder.com/200x80/1f77b4/ffffff?text=NeuroPsy+Assist", 
                use_column_width=True)
        st.markdown("## 🗂️ Navigation")
        
        # Menu de navigation
        page = st.radio(
            "Sélectionnez une section :",
            [
                "🏠 Accueil & Anamnèse",
                "🧠 Tests Cognitifs - WISC-V",
                "🎯 Tests Cognitifs - KABC-II",
                "👁️ Attention & Exécutif",
                "📝 Évaluation Comportementale",
                "📄 Génération du Rapport"
            ],
            key="navigation"
        )
        
        st.markdown("---")
        
        # Informations sur les données sauvegardées
        st.markdown("### 💾 Données Sauvegardées")
        
        # Patient
        if 'patient' in st.session_state and st.session_state.patient.format_nom_complet():
            st.success(f"✅ Patient: {st.session_state.patient.format_nom_complet()}")
        else:
            st.info("ℹ️ Aucun patient renseigné")
        
        # Anamnèse
        if 'anamnese' in st.session_state and st.session_state.anamnese.has_content():
            st.success("✅ Anamnèse complétée")
        else:
            st.info("ℹ️ Anamnèse non renseignée")
        
        # Tests
        tests_completes = []
        
        if 'wisc_v_manager' in st.session_state and st.session_state.wisc_v_manager.has_scores():
            tests_completes.append("WISC-V")
        
        if 'kabc_ii_manager' in st.session_state and st.session_state.kabc_ii_manager.has_scores():
            tests_completes.append("KABC-II")
        
        if 'teach_manager' in st.session_state and st.session_state.teach_manager.has_scores():
            tests_completes.append("TEA-Ch")
        
        if 'nepsy_ii_manager' in st.session_state and st.session_state.nepsy_ii_manager.has_scores():
            tests_completes.append("NEPSY-II")
        
        if 'brown_manager' in st.session_state and st.session_state.brown_manager.has_scores():
            tests_completes.append("Brown")
        
        if 'conners_parent_manager' in st.session_state and st.session_state.conners_parent_manager.has_scores():
            tests_completes.append("Conners Parent")
        
        if 'conners_teacher_manager' in st.session_state and st.session_state.conners_teacher_manager.has_scores():
            tests_completes.append("Conners Enseignant")
        
        if tests_completes:
            st.success(f"✅ {len(tests_completes)} test(s) complété(s)")
            for test in tests_completes:
                st.write(f"  • {test}")
        else:
            st.info("ℹ️ Aucun test complété")
        
        st.markdown("---")
        
        # Bouton de réinitialisation
        if st.button("🔄 Nouvelle Évaluation", use_container_width=True):
            # Effacer toutes les données de session
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        
        st.markdown("---")
        
        # Informations
        with st.expander("ℹ️ À propos"):
            st.markdown("""
            **NeuroPsy Assist v1.0**
            
            Application d'aide à la rédaction de comptes-rendus 
            neuropsychologiques pour enfants et adolescents.
            
            **Tests supportés :**
            - WISC-V
            - KABC-II
            - TEA-Ch
            - NEPSY-II (partiel)
            - Brown
            - Conners-3
            
            **Fonctionnalités :**
            - Saisie guidée des données
            - Interprétation automatique des scores
            - Génération de rapport structuré
            - Recommandations personnalisées
            """)
        
        with st.expander("📖 Guide d'utilisation"):
            st.markdown("""
            **1. Anamnèse**
            Renseignez les informations du patient et 
            l'histoire développementale.
            
            **2. Tests Cognitifs**
            Saisissez les scores obtenus aux différents 
            tests (WISC-V, KABC-II).
            
            **3. Attention & Exécutif**
            Complétez les évaluations attentionnelles 
            (TEA-Ch, NEPSY-II).
            
            **4. Comportement**
            Renseignez les questionnaires comportementaux 
            (Brown, Conners).
            
            **5. Rapport**
            Générez et téléchargez le rapport clinique 
            complet au format Markdown.
            
            💡 **Astuce :** Les données sont sauvegardées 
            automatiquement pendant la session. Vous pouvez 
            naviguer librement entre les sections.
            """)
    
    # Affichage de la page sélectionnée
    if page == "🏠 Accueil & Anamnèse":
        render_anamnese_module()
    
    elif page == "🧠 Tests Cognitifs - WISC-V":
        render_wisc_v_module()
    
    elif page == "🎯 Tests Cognitifs - KABC-II":
        render_kabc_ii_module()
    
    elif page == "👁️ Attention & Exécutif":
        render_attention_module()
    
    elif page == "📝 Évaluation Comportementale":
        render_comportement_module()
    
    elif page == "📄 Génération du Rapport":
        render_rapport_module()
    
    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; color: gray; font-size: 0.8rem;">'
        '© 2024 NeuroPsy Assist - Application d\'aide à la rédaction de comptes-rendus neuropsychologiques'
        '</p>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
