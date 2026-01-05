# NeuroPsy Assist 🧠

Application complète d'aide à la rédaction de comptes-rendus neuropsychologiques pour enfants et adolescents.

## Description

**NeuroPsy Assist** est une application développée avec **Python** et **Streamlit** qui permet aux neuropsychologues de :
- Saisir les données d'anamnèse et les informations patient
- Enregistrer les scores de tests psychométriques
- Générer automatiquement une pré-rédaction de compte-rendu clinique de haute qualité

## Fonctionnalités

### 📋 Saisie de l'anamnèse
- Informations patient complètes (identité, classe, école)
- Histoire développementale (grossesse, développement moteur et langagier)
- Parcours scolaire et aménagements existants
- Antécédents médicaux et familiaux
- Observations cliniques durant l'examen

### 🧠 Tests Cognitifs
- **WISC-V** : Échelle d'Intelligence de Wechsler pour Enfants (5e édition)
  - ICV, IVS, IRF, IMT, IVT
  - Indices complémentaires (IQT, IRQ, IMTA, INV, IAG, ICC)
  - Analyse de l'homogénéité du profil

- **KABC-II** : Batterie d'Évaluation de Kaufman pour Enfants
  - IFC, ISQ, ISI, IPL, IAP, ICO

### 👁️ Attention & Fonctions Exécutives
- **TEA-Ch** : Test d'Évaluation de l'Attention chez l'Enfant
  - Attention sélective, soutenue, contrôle attentionnel

- **NEPSY-II** (partiel)
  - Attention/Fonctions exécutives
  - Fonctions sensorimotrices

### 📝 Évaluation Comportementale
- **Échelle Brown** de Déficit d'Attention
- **Conners-3** (versions Parent ET Enseignant)
  - Analyse croisée multi-informateurs
  - Détection automatique des scores cliniquement significatifs

### 📄 Génération de Rapport
- Rapport structuré en Markdown
- Interprétations sémantiques automatiques des scores
- Tableaux récapitulatifs
- Graphiques Plotly interactifs
- Recommandations personnalisées selon le profil
- Téléchargement au format Markdown

## Architecture

```
neuropsy_assist/
├── app.py                      # Point d'entrée Streamlit
├── requirements.txt            # Dépendances Python
├── config/
│   └── constants.py            # Normes, seuils, structures des tests
├── models/
│   ├── __init__.py
│   ├── patient.py              # Modèles Patient et Anamnèse
│   ├── scores.py               # Gestion des scores
│   └── interpretations.py      # Algorithmes d'interprétation
├── modules/
│   ├── __init__.py
│   ├── anamnese.py             # Module UI anamnèse
│   ├── wisc_v.py               # Module UI WISC-V
│   ├── kabc_ii.py              # Module UI KABC-II
│   ├── attention.py            # Module UI TEA-Ch, NEPSY-II
│   ├── comportement.py         # Module UI Brown, Conners
│   └── rapport.py              # Module UI génération rapport
└── utils/
    ├── __init__.py
    └── semantic_engine.py      # Moteur de génération du rapport
```

## Installation

### Prérequis
- Python 3.9 ou supérieur
- pip

### Installation des dépendances

```bash
pip install -r requirements.txt
```

## Utilisation

### Lancer l'application

```bash
streamlit run app.py
```

L'application sera accessible à l'adresse : `http://localhost:8501`

### Guide d'utilisation

1. **Anamnèse** : Commencez par renseigner les informations du patient et l'histoire anamnestique
2. **Tests Cognitifs** : Saisissez les scores obtenus aux différents tests (WISC-V, KABC-II)
3. **Attention & Exécutif** : Complétez les évaluations attentionnelles (TEA-Ch, NEPSY-II)
4. **Comportement** : Renseignez les questionnaires comportementaux (Brown, Conners)
5. **Rapport** : Générez et téléchargez le rapport clinique complet

💡 **Astuce** : Les données sont sauvegardées automatiquement pendant la session. Vous pouvez naviguer librement entre les sections.

## Système de Classification des Scores

### Notes Standard (M=100, ET=15)
- **130+** : Très Supérieur (>98e percentile)
- **120-129** : Supérieur (91-98e percentile)
- **110-119** : Moyen Fort (75-90e percentile)
- **90-109** : Moyen (25-74e percentile)
- **80-89** : Moyen Faible (9-24e percentile)
- **70-79** : Limite / Zone Frontière (2-8e percentile)
- **<70** : Très Faible (<2e percentile)

### Notes Scalaires (M=10, ET=3)
- **16-19** : Très Supérieur
- **14-15** : Supérieur
- **12-13** : Moyen Fort
- **8-11** : Moyen
- **6-7** : Moyen Faible
- **4-5** : Limite
- **1-3** : Très Faible

### Scores T (M=50, ET=10)
- **70+** : Très Élevé ⚠️ (Cliniquement significatif)
- **65-69** : Élevé / À Risque ⚠️ (Cliniquement significatif)
- **60-64** : Moyen Haut
- **40-59** : Moyen
- **35-39** : Moyen Bas
- **<35** : Bas

## Interprétations Sémantiques

L'application traduit automatiquement chaque score en phrases cliniques nuancées et empathiques. Par exemple :

- **Score 125** → "Score situé dans la zone supérieure, témoignant de capacités solides et efficientes en [domaine], constituant un point d'appui significatif."
- **Score 75** → "Score situé en zone frontière, révélant une fragilité importante en [domaine], nécessitant un accompagnement adapté."

## Structure du Rapport Généré

1. En-tête (informations patient)
2. Éléments anamnestiques
3. Observations cliniques durant l'examen
4. Évaluation des fonctions intellectuelles
5. Évaluation des fonctions attentionnelles et exécutives
6. Évaluation comportementale
7. Synthèse clinique
8. Recommandations personnalisées
9. Conclusion

## Dépendances

- `streamlit==1.29.0` : Framework d'interface utilisateur
- `pandas==2.1.3` : Manipulation de données
- `numpy==1.26.2` : Calculs numériques
- `plotly==5.18.0` : Visualisations interactives

## Caractéristiques Techniques

- ✅ Dataclasses pour les modèles de données
- ✅ Enums pour les types de scores
- ✅ Gestion de l'état avec `st.session_state`
- ✅ Code documenté avec docstrings en français
- ✅ Respect des conventions PEP 8
- ✅ Architecture modulaire et extensible

## Avertissements et Limitations

⚠️ **Important** : Cette application est un outil d'aide à la rédaction. Le rapport généré doit impérativement être relu, vérifié et adapté par un professionnel qualifié avant toute utilisation clinique.

- Les interprétations sont génériques et doivent être contextualisées
- Le rapport nécessite une révision manuelle par le neuropsychologue
- L'outil ne remplace pas l'expertise clinique du professionnel

## Licence

Cette application est fournie à des fins éducatives et professionnelles.

## Support

Pour toute question ou suggestion d'amélioration, veuillez ouvrir une issue sur le dépôt GitHub.

---

**NeuroPsy Assist** - Outil d'aide à la rédaction de comptes-rendus neuropsychologiques
© 2024