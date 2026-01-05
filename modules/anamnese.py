"""
Module UI pour la saisie de l'anamnèse.
"""

import streamlit as st
from datetime import date
from models.patient import Patient, Anamnese


def render_anamnese_module():
    """Affiche le module de saisie de l'anamnèse."""
    
    st.title("📋 Anamnèse et Informations Patient")
    
    # Initialisation dans session_state
    if 'patient' not in st.session_state:
        st.session_state.patient = Patient()
    if 'anamnese' not in st.session_state:
        st.session_state.anamnese = Anamnese()
    
    patient = st.session_state.patient
    anamnese = st.session_state.anamnese
    
    # Informations patient
    with st.expander("👤 Informations Patient", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            patient.nom = st.text_input("Nom", value=patient.nom, key="patient_nom")
            patient.prenom = st.text_input("Prénom", value=patient.prenom, key="patient_prenom")
            patient.classe = st.text_input("Classe", value=patient.classe, key="patient_classe")
        
        with col2:
            patient.ecole = st.text_input("École", value=patient.ecole, key="patient_ecole")
            patient.date_naissance = st.date_input(
                "Date de naissance",
                value=patient.date_naissance or date.today(),
                key="patient_date_naissance",
                max_value=date.today()
            )
            patient.date_examen = st.date_input(
                "Date d'examen",
                value=patient.date_examen or date.today(),
                key="patient_date_examen",
                max_value=date.today()
            )
        
        # Affichage de l'âge
        age = patient.get_age_at_exam()
        if age is not None:
            st.info(f"**Âge à l'examen :** {age} ans")
    
    # Motif de consultation
    with st.expander("🎯 Motif de Consultation", expanded=True):
        anamnese.motif_consultation = st.text_area(
            "Motif de consultation",
            value=anamnese.motif_consultation,
            height=100,
            key="anamnese_motif",
            help="Pourquoi le patient consulte-t-il ?"
        )
        anamnese.demandeur = st.text_input(
            "Demandeur",
            value=anamnese.demandeur,
            key="anamnese_demandeur",
            help="Qui a demandé cette évaluation ? (parents, école, médecin...)"
        )
    
    # Histoire développementale
    with st.expander("👶 Histoire Développementale"):
        anamnese.grossesse_accouchement = st.text_area(
            "Grossesse et accouchement",
            value=anamnese.grossesse_accouchement,
            height=80,
            key="anamnese_grossesse",
            help="Déroulement de la grossesse et de l'accouchement"
        )
        anamnese.developpement_moteur = st.text_area(
            "Développement moteur",
            value=anamnese.developpement_moteur,
            height=80,
            key="anamnese_dev_moteur",
            help="Acquisitions motrices (marche, préhension, etc.)"
        )
        anamnese.developpement_langagier = st.text_area(
            "Développement langagier",
            value=anamnese.developpement_langagier,
            height=80,
            key="anamnese_dev_langage",
            help="Acquisitions langagières (premiers mots, phrases, etc.)"
        )
    
    # Parcours scolaire
    with st.expander("🎓 Parcours Scolaire"):
        anamnese.histoire_scolaire = st.text_area(
            "Histoire scolaire",
            value=anamnese.histoire_scolaire,
            height=100,
            key="anamnese_scolarite",
            help="Parcours scolaire général, difficultés rencontrées"
        )
        anamnese.redoublements = st.text_input(
            "Redoublements",
            value=anamnese.redoublements,
            key="anamnese_redoublements",
            help="Classes redoublées, le cas échéant"
        )
        anamnese.amenagements_existants = st.text_area(
            "Aménagements existants",
            value=anamnese.amenagements_existants,
            height=80,
            key="anamnese_amenagements",
            help="PAI, PAP, AESH, etc."
        )
    
    # Antécédents
    with st.expander("🏥 Antécédents"):
        anamnese.antecedents_medicaux = st.text_area(
            "Antécédents médicaux",
            value=anamnese.antecedents_medicaux,
            height=80,
            key="anamnese_atcd_medicaux",
            help="Pathologies, hospitalisations, traitements"
        )
        anamnese.antecedents_familiaux = st.text_area(
            "Antécédents familiaux",
            value=anamnese.antecedents_familiaux,
            height=80,
            key="anamnese_atcd_familiaux",
            help="Antécédents familiaux pertinents"
        )
        anamnese.suivis_actuels = st.text_area(
            "Suivis actuels",
            value=anamnese.suivis_actuels,
            height=80,
            key="anamnese_suivis",
            help="Professionnels suivant l'enfant (orthophoniste, psychomotricien, etc.)"
        )
    
    # Observations cliniques
    with st.expander("🔍 Observations Cliniques Durant l'Examen"):
        anamnese.comportement = st.text_area(
            "Comportement général",
            value=anamnese.comportement,
            height=80,
            key="anamnese_comportement",
            help="Attitude générale durant l'examen"
        )
        anamnese.collaboration = st.text_area(
            "Collaboration",
            value=anamnese.collaboration,
            height=80,
            key="anamnese_collaboration",
            help="Qualité de la collaboration, motivation"
        )
        anamnese.fatigabilite = st.text_area(
            "Fatigabilité",
            value=anamnese.fatigabilite,
            height=80,
            key="anamnese_fatigue",
            help="Signes de fatigue observés"
        )
        anamnese.anxiete_performance = st.text_area(
            "Anxiété de performance",
            value=anamnese.anxiete_performance,
            height=80,
            key="anamnese_anxiete",
            help="Manifestations d'anxiété face aux épreuves"
        )
        anamnese.strategies_observees = st.text_area(
            "Stratégies observées",
            value=anamnese.strategies_observees,
            height=80,
            key="anamnese_strategies",
            help="Stratégies de résolution, d'adaptation"
        )
        anamnese.autres_observations = st.text_area(
            "Autres observations",
            value=anamnese.autres_observations,
            height=80,
            key="anamnese_autres",
            help="Toute autre observation pertinente"
        )
    
    # Sauvegarde dans session_state
    st.session_state.patient = patient
    st.session_state.anamnese = anamnese
    
    # Message de confirmation
    if anamnese.has_content():
        st.success("✅ Données anamnestiques enregistrées")
    else:
        st.info("ℹ️ Veuillez renseigner les informations anamnestiques")
