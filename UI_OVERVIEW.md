# NeuroPsy Assist - Aperçu de l'Interface Utilisateur

## 🎨 Design Global

L'application utilise **Streamlit** pour offrir une interface web moderne et professionnelle accessible via navigateur.

### Palette de Couleurs
- **Bleu principal** (#1f77b4) : Titre, branding
- **Vert** : Scores positifs, validations
- **Orange** : Avertissements, scores moyens-faibles
- **Rouge** : Scores critiques, alertes
- **Gris** : Informations secondaires

## 📱 Structure de l'Interface

### En-tête Principal
```
🧠 NeuroPsy Assist
Assistant de rédaction de comptes-rendus neuropsychologiques
---
```

### Sidebar (Menu Latéral)

```
┌─────────────────────────────────────┐
│ [Logo] NeuroPsy Assist              │
├─────────────────────────────────────┤
│ 🗂️ Navigation                       │
│                                     │
│ ⦿ 🏠 Accueil & Anamnèse            │
│ ○ 🧠 Tests Cognitifs - WISC-V      │
│ ○ 🎯 Tests Cognitifs - KABC-II     │
│ ○ 👁️ Attention & Exécutif          │
│ ○ 📝 Évaluation Comportementale    │
│ ○ 📄 Génération du Rapport         │
├─────────────────────────────────────┤
│ �� Données Sauvegardées             │
│                                     │
│ ✅ Patient: Lucas Dupont            │
│ ✅ Anamnèse complétée               │
│ ✅ 4 test(s) complété(s)            │
│   • WISC-V                          │
│   • TEA-Ch                          │
│   • Conners Parent                  │
│   • Conners Enseignant              │
├─────────────────────────────────────┤
│ [🔄 Nouvelle Évaluation]            │
├─────────────────────────────────────┤
│ ▼ ℹ️ À propos                       │
│ ▼ 📖 Guide d'utilisation            │
└─────────────────────────────────────┘
```

## 📄 Pages de l'Application

### 1. 🏠 Accueil & Anamnèse

#### Layout
```
📋 Anamnèse et Informations Patient
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

▼ 👤 Informations Patient [Ouvert]
┌──────────────────────────────────────────┐
│ [Nom]        [Prénom]       [Classe]     │
│ [École]      [Date nais.]   [Date exam.] │
│ ℹ️ Âge à l'examen : 10 ans               │
└──────────────────────────────────────────┘

▼ 🎯 Motif de Consultation [Ouvert]
┌──────────────────────────────────────────┐
│ [Zone de texte multi-lignes]             │
│ [Demandeur]                              │
└──────────────────────────────────────────┘

▶ 👶 Histoire Développementale
▶ 🎓 Parcours Scolaire
▶ 🏥 Antécédents
▶ 🔍 Observations Cliniques Durant l'Examen

✅ Données anamnestiques enregistrées
```

### 2. 🧠 Tests Cognitifs - WISC-V

#### Layout
```
🧠 WISC-V - Échelle d'Intelligence de Wechsler pour Enfants
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Saisissez les scores obtenus...

📊 Indices Principaux (Notes Standard)

▼ ICV - Indice de Compréhension Verbale
┌──────────────────────────────────────────┐
│ Score ICV:  [105] ▼     [✓] Renseigné   │
│ ✅ Moyen (Percentile: 25-74)             │
│ Score situé dans la zone moyenne...      │
│                                          │
│ Subtests (Notes Scalaires) :            │
│ Similitudes:      [12] ▼  [✓]           │
│ Vocabulaire:      [11] ▼  [✓]           │
│ Information:      [10] ▼  [ ]           │
│ Compréhension:    [10] ▼  [ ]           │
└──────────────────────────────────────────┘

▶ IVS - Indice Visuospatial
▶ IRF - Indice de Raisonnement Fluide
▶ IMT - Indice de Mémoire de Travail
▶ IVT - Indice de Vitesse de Traitement

📈 Indices Complémentaires (Notes Standard)
▶ Indices Complémentaires

🔍 Analyse du Profil
⚠️ Profil hétérogène (écart maximal: 27 points)
  • Points faibles : IVT (78)
  • Points forts : ICV (105)

📋 Tableau Récapitulatif
┌─────────┬───────┬─────────────────┬────────────┐
│ Indice  │ Score │ Classification  │ Percentile │
├─────────┼───────┼─────────────────┼────────────┤
│ ICV     │ 105   │ Moyen          │ 25-74      │
│ IVS     │ 98    │ Moyen          │ 25-74      │
│ IRF     │ 102   │ Moyen          │ 25-74      │
│ IMT     │ 85    │ Moyen Faible   │ 9-24       │
│ IVT     │ 78    │ Limite         │ 2-8        │
│ IQT     │ 94    │ Moyen          │ 25-74      │
└─────────┴───────┴─────────────────┴────────────┘

✅ Scores WISC-V enregistrés
```

### 3. 🎯 Tests Cognitifs - KABC-II

Similar layout to WISC-V with 6 indices

### 4. 👁️ Attention & Exécutif

#### Layout
```
👁️ Évaluation de l'Attention et des Fonctions Exécutives
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 TEA-Ch - Test d'Évaluation de l'Attention chez l'Enfant

▼ 📌 Attention sélective
┌──────────────────────────────────────────┐
│ Recherche dans le Ciel:  [8] ▼  [✓]     │
│ ℹ️ Moyen                                 │
│ Carte Géographique:      [7] ▼  [✓]     │
│ ℹ️ Moyen Faible                          │
└──────────────────────────────────────────┘

▶ 📌 Attention soutenue
▶ 📌 Contrôle attentionnel

✅ Scores TEA-Ch enregistrés

▶ 📋 Tableau Récapitulatif TEA-Ch

🧩 NEPSY-II - Bilan Neuropsychologique de l'Enfant

▶ 📌 Attention/Fonctions exécutives
▶ 📌 Fonctions sensorimotrices
```

### 5. 📝 Évaluation Comportementale

#### Layout
```
📝 Évaluation Comportementale
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔵 Échelle Brown de Déficit d'Attention

▼ Échelles Brown (Scores T)
┌──────────────────────────────────────────┐
│ Activation:                [50] ▼  [ ]   │
│ Attention:                 [50] ▼  [ ]   │
│ ...                                      │
└──────────────────────────────────────────┘

🔴 Échelle Conners-3

💡 Renseignez les scores pour les versions Parent ET Enseignant

👨‍👩‍👧 Version Parent

▼ Échelles Conners-3 Parent (Scores T)
┌──────────────────────────────────────────┐
│ Inattention:               [72] ▼  [✓]  │
│ ⚠️ Très Élevé - Cliniquement significatif│
│ Hyperactivité/Impulsivité: [68] ▼  [✓]  │
│ ⚠️ Élevé (À Risque) - Cliniquement...   │
└──────────────────────────────────────────┘

✅ Scores Conners-3 Parent enregistrés

👨‍🏫 Version Enseignant
[Similar layout]

🔍 Comparaison Parent / Enseignant

▼ Analyse Croisée
┌────────────────┬──────────┬─────────────┬───────┬─────────────┐
│ Échelle        │ Parent(T)│ Enseignant(T)│ Écart │ Convergence │
├────────────────┼──────────┼─────────────┼───────┼─────────────┤
│ Inattention    │ 72       │ 75          │ 3     │ ✅ Convergent│
│ Hyperactivité  │ 68       │ 62          │ 6     │ ✅ Convergent│
└────────────────┴──────────┴─────────────┴───────┴─────────────┘

✅ Bonne convergence entre les informateurs
```

### 6. 📄 Génération du Rapport

#### Layout
```
📄 Génération du Rapport Clinique
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Données Disponibles

▼ Voir le résumé [Ouvert]
┌──────────────────────────┬──────────────────────────┐
│ Patient:                 │ Tests attentionnels:     │
│ ✅ Lucas Dupont          │ ✅ TEA-Ch (5 scores)     │
│                          │                          │
│ Tests cognitifs:         │ Questionnaires:          │
│ ✅ WISC-V (6 scores)     │ ✅ Brown (7 scores)      │
│                          │ ✅ Conners Parent        │
│                          │ ✅ Conners Enseignant    │
└──────────────────────────┴──────────────────────────┘

📈 Visualisations

▼ Profil WISC-V [Ouvert]
┌──────────────────────────────────────────┐
│ [Graphique Plotly interactif]            │
│ Barres horizontales colorées par zone    │
│ ICV  ████████████████ 105                │
│ IVS  ████████████ 98                     │
│ IRF  █████████████ 102                   │
│ IMT  ████████ 85                         │
│ IVT  ██████ 78                           │
│                                          │
│ [Zones de référence colorées]           │
└──────────────────────────────────────────┘

▼ Comparaison Parent / Enseignant (Conners)
┌──────────────────────────────────────────┐
│ [Graphique Plotly comparatif]            │
│ Barres groupées Parent vs Enseignant     │
└──────────────────────────────────────────┘

📝 Rapport Clinique

┌────────────────────────────────────────┐
│ [🔄 Générer le Rapport]                │
└────────────────────────────────────────┘

✅ Rapport généré avec succès !

───

▶ 👁️ Aperçu du Rapport
[Contenu Markdown du rapport]

┌────────────────────────────────────────┐
│ [�� Télécharger le Rapport (Markdown)]  │
└────────────────────────────────────────┘

💡 Le rapport a été généré au format Markdown...
```

## 🎨 Éléments Visuels

### Indicateurs de Statut
- ✅ **Vert** : Validation, données enregistrées
- ℹ️ **Bleu** : Information
- ⚠️ **Orange** : Avertissement, attention
- ❌ **Rouge** : Erreur, score critique

### Codes Couleur des Scores
- 🟢 **Vert** : Scores positifs (Supérieur, Très Supérieur)
- 🟡 **Jaune** : Scores moyens
- 🟠 **Orange** : Scores faibles
- 🔴 **Rouge** : Scores critiques (Limite, Très Faible, Très Élevé pour T-scores)

### Émojis Utilisés
- 🧠 Intelligence / Cognitif
- 👁️ Attention
- 📝 Évaluation comportementale
- 📄 Rapport
- 🎯 Objectif / Test
- 👤 Patient
- 📊 Graphique / Statistiques
- 🔍 Analyse
- ⚡ Important
- 💡 Astuce
- ✅ Succès
- ⚠️ Attention
- 🔄 Actualiser

## 📱 Responsive Design

L'interface s'adapte automatiquement à la taille de l'écran :
- **Desktop** : Sidebar visible + contenu principal large
- **Tablet** : Sidebar réductible + contenu adapté
- **Mobile** : Menu hamburger + affichage optimisé

## 🎯 Points Forts de l'UX

1. **Navigation Intuitive** : Menu latéral clair avec icônes
2. **Feedback Immédiat** : Validation en temps réel des saisies
3. **Organisation Claire** : Expanders pour structurer le contenu
4. **Indicateurs Visuels** : Couleurs et émojis pour guider l'utilisateur
5. **Persistance** : Données sauvegardées automatiquement
6. **Résumé Visible** : État des données toujours affiché dans la sidebar
7. **Visualisations** : Graphiques interactifs Plotly
8. **Téléchargement Simple** : Un clic pour exporter le rapport

## 🔧 Interactions Utilisateur

### Saisie de Scores
1. Ouvrir l'expander de l'indice/échelle
2. Entrer la valeur avec le number input
3. Cocher "Renseigné"
4. → Classification et interprétation s'affichent immédiatement

### Navigation
1. Cliquer sur une section dans la sidebar
2. → Changement de page instantané
3. → Données précédentes conservées

### Génération de Rapport
1. Vérifier les données dans le résumé
2. Consulter les visualisations
3. Cliquer sur "Générer le Rapport"
4. → Rapport créé en quelques secondes
5. Ouvrir l'aperçu pour vérifier
6. Télécharger le fichier Markdown

### Nouvelle Évaluation
1. Cliquer sur "Nouvelle Évaluation" dans la sidebar
2. → Confirmation
3. → Toutes les données effacées
4. → Retour à la page d'accueil

## 🎨 Cohérence Visuelle

- **Police** : Système par défaut de Streamlit (claire et lisible)
- **Espacement** : Consistant entre les éléments
- **Alignement** : Colonnes et grilles bien alignées
- **Hiérarchie** : Titres, sous-titres, texte bien différenciés
- **Boutons** : Style uniforme, full-width pour actions principales
- **Tableaux** : Pandas/Streamlit dataframe avec formatage automatique

---

L'interface est **professionnelle, intuitive et efficace**, permettant aux neuropsychologues de se concentrer sur le contenu clinique plutôt que sur la technique.
