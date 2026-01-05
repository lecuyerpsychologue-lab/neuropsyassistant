# Guide d'Utilisation - NeuroPsy Assist

## Démarrage Rapide

### 1. Installation

```bash
# Cloner le dépôt
git clone https://github.com/lecuyerpsychologue-lab/neuropsyassistant.git
cd neuropsyassistant

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app.py
```

L'application s'ouvre automatiquement dans votre navigateur à l'adresse `http://localhost:8501`

## Navigation

L'application est organisée en **6 sections principales** accessibles via la sidebar (menu latéral) :

### 🏠 Accueil & Anamnèse
**Objectif** : Collecter les informations du patient et son histoire

**Sections à compléter :**
- **Informations Patient** : Nom, prénom, date de naissance, date d'examen, classe, école
- **Motif de Consultation** : Raison de la demande, demandeur
- **Histoire Développementale** : Grossesse, développement moteur et langagier
- **Parcours Scolaire** : Histoire scolaire, redoublements, aménagements existants
- **Antécédents** : Médicaux, familiaux, suivis actuels
- **Observations Cliniques** : Comportement durant l'examen, collaboration, fatigabilité, anxiété, stratégies observées

💡 **Astuce** : Tous les champs sont optionnels mais plus vous renseignez d'informations, plus le rapport sera complet.

### 🧠 Tests Cognitifs - WISC-V
**Objectif** : Saisir les scores du WISC-V (Échelle d'Intelligence de Wechsler)

**Indices principaux à renseigner :**
- **ICV** (Indice de Compréhension Verbale)
  - Subtests : Similitudes, Vocabulaire, Information, Compréhension
- **IVS** (Indice Visuospatial)
  - Subtests : Cubes, Puzzles Visuels
- **IRF** (Indice de Raisonnement Fluide)
  - Subtests : Matrices, Balances, Arithmétique
- **IMT** (Indice de Mémoire de Travail)
  - Subtests : Mémoire des Chiffres, Mémoire des Images, Séquence Lettres-Chiffres
- **IVT** (Indice de Vitesse de Traitement)
  - Subtests : Code, Symboles, Barrage

**Indices complémentaires :**
- IQT (QI Total), IRQ, IMTA, INV, IAG, ICC

**Fonctionnalités :**
- ✅ Classification automatique de chaque score
- ✅ Calcul du percentile
- ✅ Interprétation sémantique en temps réel
- ✅ Analyse de l'homogénéité du profil (détecte les écarts >15 points)
- ✅ Tableau récapitulatif des scores

**Comment saisir un score :**
1. Cliquez sur l'expander de l'indice concerné
2. Entrez la valeur du score (notes standard : 40-160)
3. Cochez la case "Renseigné"
4. L'interprétation apparaît automatiquement

### 🎯 Tests Cognitifs - KABC-II
**Objectif** : Saisir les scores du KABC-II (Batterie d'Évaluation de Kaufman)

**Indices disponibles :**
- **IFC** (Indice de Fonctions Cognitives)
- **ISQ** (Indice Séquentiel)
- **ISI** (Indice Simultané)
- **IPL** (Indice de Planification)
- **IAP** (Indice d'Apprentissage)
- **ICO** (Indice de Connaissances)

Fonctionne de la même manière que le WISC-V avec classification et analyse du profil.

### 👁️ Attention & Exécutif
**Objectif** : Évaluer l'attention et les fonctions exécutives

**Tests disponibles :**

#### TEA-Ch (Test d'Évaluation de l'Attention chez l'Enfant)
Organisé par catégorie :
- **Attention sélective** : Recherche dans le Ciel, Carte Géographique, Écoute Deux Choses à la Fois
- **Attention soutenue** : Coups de Fusil, Marche-Arrêt, Transmission de Codes
- **Contrôle attentionnel** : Les Petits Hommes Verts, Mondes Contraires, Faire Deux Choses à la Fois

#### NEPSY-II (Bilan Neuropsychologique de l'Enfant) - Partiel
- **Attention/Fonctions exécutives** : Attention Auditive, Réponses Associées, Inhibition, Statue
- **Fonctions sensorimotrices** : Précision Visuomotrice, Imitation de Positions de Mains, Séquences Motrices Manuelles

**Type de scores** : Notes scalaires (1-19, moyenne 10)

### 📝 Évaluation Comportementale
**Objectif** : Évaluer les aspects comportementaux et attentionnels

#### Échelle Brown de Déficit d'Attention
**Échelles** :
- Activation
- Attention
- Effort
- Émotion
- Mémoire
- Action
- Score Total

**Type de scores** : Scores T (20-80, moyenne 50)

#### Conners-3
**Particularité** : Deux versions disponibles (Parent ET Enseignant)

**Échelles communes** :
- Inattention
- Hyperactivité/Impulsivité
- Problèmes d'Apprentissage
- Fonctions Exécutives
- Défiance/Agressivité
- Relations avec les Pairs
- Indices TDAH (Inattentif, Hyperactif/Impulsif, Combiné)
- Indice Global Conners

**Fonctionnalités spéciales :**
- ⚠️ Détection automatique des scores cliniquement significatifs (T ≥ 65)
- 🔍 Analyse croisée Parent/Enseignant
- ✅ Identification des convergences et divergences entre informateurs

### 📄 Génération du Rapport
**Objectif** : Créer le compte-rendu clinique final

**Prérequis** :
- Au moins les informations patient renseignées
- Au moins un test complété

**Contenu du rapport :**

1. **En-tête** : Informations patient
2. **Éléments Anamnestiques** : Histoire complète si renseignée
3. **Observations Cliniques** : Comportement durant l'examen
4. **Évaluation Intellectuelle** : Résultats WISC-V et/ou KABC-II avec tableaux et interprétations
5. **Évaluation Attentionnelle** : Résultats TEA-Ch et NEPSY-II
6. **Évaluation Comportementale** : Résultats Brown et Conners avec analyse croisée
7. **Synthèse Clinique** : Vue d'ensemble du profil, forces et fragilités
8. **Recommandations** : Personnalisées selon le profil identifié
9. **Conclusion** : Synthèse finale

**Visualisations incluses :**
- 📊 Graphique du profil WISC-V avec zones colorées
- 📊 Comparaison Parent/Enseignant (Conners)

**Comment générer le rapport :**
1. Vérifiez le résumé des données disponibles
2. Consultez les visualisations si disponibles
3. Cliquez sur "🔄 Générer le Rapport"
4. Consultez l'aperçu dans l'expander
5. Téléchargez le fichier Markdown avec le bouton "📥 Télécharger"

**Format de sortie** : Markdown (.md)
- Lisible dans n'importe quel éditeur de texte
- Convertible en PDF avec Pandoc
- Éditable facilement pour ajustements manuels

## Conseils d'Utilisation

### Ordre Recommandé
1. Commencez **toujours** par l'anamnèse (informations patient essentielles)
2. Complétez les tests dans l'ordre de passation réelle
3. Générez le rapport en dernier

### Sauvegarde des Données
- ✅ Les données sont **automatiquement sauvegardées** pendant la session
- ✅ Vous pouvez naviguer librement entre les sections
- ⚠️ Les données sont **perdues** si vous fermez l'application
- 💡 Pour un nouveau patient, cliquez sur "🔄 Nouvelle Évaluation" dans la sidebar

### Bonnes Pratiques

**Pour les scores :**
- Ne cochez "Renseigné" que pour les scores réellement passés
- Vérifiez les valeurs saisies (elles doivent être cohérentes avec les normes du test)
- Consultez les interprétations automatiques pour valider vos saisies

**Pour le rapport :**
- Le rapport est une **pré-rédaction** à adapter
- Relisez et personnalisez **impérativement** le contenu
- Ajoutez des nuances cliniques spécifiques au cas
- Vérifiez la cohérence des interprétations avec votre analyse clinique

## Interprétation des Classifications

### Zones de Fonctionnement (Notes Standard)
- 🟢 **Très Supérieur** (130+) : Capacités exceptionnelles
- 🟢 **Supérieur** (120-129) : Points forts significatifs
- 🟡 **Moyen Fort** (110-119) : Compétences satisfaisantes
- 🟡 **Moyen** (90-109) : Fonctionnement attendu
- 🟠 **Moyen Faible** (80-89) : Fragilité relative
- 🔴 **Limite** (70-79) : Fragilité importante nécessitant aménagements
- 🔴 **Très Faible** (<70) : Difficulté majeure nécessitant soutien intensif

### Scores Comportementaux (Scores T)
- 🔴 **Très Élevé** (70+) : Cliniquement significatif - Attention immédiate
- 🔴 **Élevé/À Risque** (65-69) : Cliniquement significatif - Attention particulière
- 🟡 **Moyen Haut** (60-64) : Sans caractère clinique
- 🟢 **Moyen** (40-59) : Pas de difficulté
- 🟢 **Moyen Bas** / **Bas** (<40) : Pas de difficulté

## Dépannage

### L'application ne démarre pas
```bash
# Vérifier l'installation de Streamlit
pip show streamlit

# Réinstaller si nécessaire
pip install --upgrade streamlit
```

### Les scores ne se sauvegardent pas
- Vérifiez que vous avez bien coché "Renseigné" après avoir saisi le score
- Le message "✅ Scores ... enregistrés" doit apparaître

### Le rapport ne se génère pas
- Vérifiez qu'au moins les informations patient sont renseignées
- Vérifiez qu'au moins un test est complété
- Consultez les messages d'erreur affichés

### Réinitialiser l'application
- Cliquez sur "🔄 Nouvelle Évaluation" dans la sidebar
- Ou rafraîchissez la page du navigateur (F5)

## Support

Pour toute question, suggestion ou signalement de bug :
- Consultez d'abord cette documentation
- Ouvrez une issue sur GitHub
- Contactez le développeur

---

**Bonne utilisation !** 🎉
