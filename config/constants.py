"""
Constantes et configurations pour NeuroPsy Assist.
Contient les normes, seuils et structures des tests psychométriques.
"""

from enum import Enum
from typing import Dict, List, Tuple


class ScoreType(Enum):
    """Types de scores psychométriques."""
    STANDARD = "standard"  # M=100, ET=15
    SCALAIRE = "scalaire"  # M=10, ET=3
    T_SCORE = "t_score"    # M=50, ET=10


# Classifications des notes standard (M=100, ET=15)
STANDARD_CLASSIFICATIONS = [
    (130, float('inf'), "Très Supérieur", ">98"),
    (120, 129, "Supérieur", "91-98"),
    (110, 119, "Moyen Fort", "75-90"),
    (90, 109, "Moyen", "25-74"),
    (80, 89, "Moyen Faible", "9-24"),
    (70, 79, "Limite (Zone Frontière)", "2-8"),
    (0, 69, "Très Faible", "<2"),
]

# Classifications des notes scalaires (M=10, ET=3)
SCALAIRE_CLASSIFICATIONS = [
    (16, 19, "Très Supérieur"),
    (14, 15, "Supérieur"),
    (12, 13, "Moyen Fort"),
    (8, 11, "Moyen"),
    (6, 7, "Moyen Faible"),
    (4, 5, "Limite"),
    (1, 3, "Très Faible"),
]

# Classifications des scores T (M=50, ET=10)
T_SCORE_CLASSIFICATIONS = [
    (70, float('inf'), "Très Élevé", True),
    (65, 69, "Élevé (À Risque)", True),
    (60, 64, "Moyen Haut", False),
    (40, 59, "Moyen", False),
    (35, 39, "Moyen Bas", False),
    (0, 34, "Bas", False),
]

# Seuils d'hétérogénéité
HETEROGENEITE_SEUIL = 15  # Différence significative entre indices

# Structure WISC-V
WISC_V_STRUCTURE = {
    "ICV": {
        "nom": "Indice de Compréhension Verbale",
        "subtests": ["Similitudes", "Vocabulaire", "Information", "Compréhension"],
        "domaine": "compréhension verbale et formation de concepts"
    },
    "IVS": {
        "nom": "Indice Visuospatial",
        "subtests": ["Cubes", "Puzzles Visuels"],
        "domaine": "raisonnement visuospatial et analyse perceptive"
    },
    "IRF": {
        "nom": "Indice de Raisonnement Fluide",
        "subtests": ["Matrices", "Balances", "Arithmétique"],
        "domaine": "raisonnement logique et résolution de problèmes"
    },
    "IMT": {
        "nom": "Indice de Mémoire de Travail",
        "subtests": ["Mémoire des Chiffres", "Mémoire des Images", "Séquence Lettres-Chiffres"],
        "domaine": "mémoire de travail et manipulation mentale"
    },
    "IVT": {
        "nom": "Indice de Vitesse de Traitement",
        "subtests": ["Code", "Symboles", "Barrage"],
        "domaine": "vitesse de traitement et attention visuelle"
    },
    "IQT": {
        "nom": "QI Total",
        "subtests": [],
        "domaine": "fonctionnement intellectuel global"
    },
    "IRQ": {
        "nom": "Indice de Raisonnement Quantitatif",
        "subtests": [],
        "domaine": "raisonnement quantitatif"
    },
    "IMTA": {
        "nom": "Indice de Mémoire de Travail Auditif",
        "subtests": [],
        "domaine": "mémoire de travail auditif"
    },
    "INV": {
        "nom": "Indice Non Verbal",
        "subtests": [],
        "domaine": "raisonnement non verbal"
    },
    "IAG": {
        "nom": "Indice d'Aptitude Générale",
        "subtests": [],
        "domaine": "aptitude générale"
    },
    "ICC": {
        "nom": "Indice de Compétence Cognitive",
        "subtests": [],
        "domaine": "compétence cognitive"
    }
}

# Structure KABC-II
KABC_II_STRUCTURE = {
    "IFC": {
        "nom": "Indice de Fonctions Cognitives",
        "subtests": [],
        "domaine": "fonctions cognitives globales"
    },
    "ISQ": {
        "nom": "Indice Séquentiel",
        "subtests": [],
        "domaine": "traitement séquentiel de l'information"
    },
    "ISI": {
        "nom": "Indice Simultané",
        "subtests": [],
        "domaine": "traitement simultané de l'information"
    },
    "IPL": {
        "nom": "Indice de Planification",
        "subtests": [],
        "domaine": "planification et organisation"
    },
    "IAP": {
        "nom": "Indice d'Apprentissage",
        "subtests": [],
        "domaine": "apprentissage et mémorisation"
    },
    "ICO": {
        "nom": "Indice de Connaissances",
        "subtests": [],
        "domaine": "connaissances acquises"
    }
}

# Structure TEA-Ch
TEACH_STRUCTURE = {
    "Attention sélective": [
        "Recherche dans le Ciel",
        "Carte Géographique",
        "Écoute Deux Choses à la Fois"
    ],
    "Attention soutenue": [
        "Coups de Fusil",
        "Marche-Arrêt",
        "Transmission de Codes"
    ],
    "Contrôle attentionnel": [
        "Les Petits Hommes Verts",
        "Mondes Contraires",
        "Faire Deux Choses à la Fois"
    ]
}

# Structure NEPSY-II (Partiel)
NEPSY_II_STRUCTURE = {
    "Attention/Fonctions exécutives": [
        "Attention Auditive",
        "Réponses Associées",
        "Inhibition",
        "Statue"
    ],
    "Fonctions sensorimotrices": [
        "Précision Visuomotrice",
        "Imitation de Positions de Mains",
        "Séquences Motrices Manuelles"
    ]
}

# Échelles Conners-3
CONNERS_3_ECHELLES = [
    "Inattention",
    "Hyperactivité/Impulsivité",
    "Problèmes d'Apprentissage",
    "Fonctions Exécutives",
    "Défiance/Agressivité",
    "Relations avec les Pairs",
    "Indice TDAH Inattentif",
    "Indice TDAH Hyperactif/Impulsif",
    "Indice TDAH Combiné",
    "Indice Global Conners"
]

# Échelles Brown
BROWN_ECHELLES = [
    "Activation",
    "Attention",
    "Effort",
    "Émotion",
    "Mémoire",
    "Action",
    "Score Total"
]

# Interprétations sémantiques par niveau de score (notes standard)
INTERPRETATIONS_SEMANTIQUES = {
    "Très Supérieur": {
        "phrase": "Score situé dans la zone très supérieure, attestant de capacités exceptionnelles en {domaine}, représentant une force majeure du profil cognitif.",
        "couleur": "#2E7D32",
        "recommandation": "Stimuler et enrichir ces capacités exceptionnelles"
    },
    "Supérieur": {
        "phrase": "Score situé dans la zone supérieure, témoignant de capacités solides et efficientes en {domaine}, constituant un point d'appui significatif.",
        "couleur": "#388E3C",
        "recommandation": "S'appuyer sur ces capacités pour faciliter les apprentissages"
    },
    "Moyen Fort": {
        "phrase": "Score situé dans la zone moyenne forte, indiquant des compétences satisfaisantes en {domaine}, permettant un fonctionnement adapté.",
        "couleur": "#66BB6A",
        "recommandation": "Maintenir et consolider ces compétences"
    },
    "Moyen": {
        "phrase": "Score situé dans la zone moyenne, reflétant un fonctionnement attendu en {domaine}, sans difficulté particulière.",
        "couleur": "#FFA726",
        "recommandation": "Accompagner le développement de ces compétences"
    },
    "Moyen Faible": {
        "phrase": "Score situé dans la zone moyenne faible, suggérant une relative fragilité en {domaine}, pouvant impacter le fonctionnement dans certaines situations exigeantes.",
        "couleur": "#F57C00",
        "recommandation": "Proposer un accompagnement ciblé pour soutenir ces compétences"
    },
    "Limite (Zone Frontière)": {
        "phrase": "Score situé en zone frontière, révélant une fragilité importante en {domaine}, nécessitant un accompagnement adapté et des aménagements spécifiques.",
        "couleur": "#E64A19",
        "recommandation": "Mettre en place des aménagements et un suivi spécialisé"
    },
    "Très Faible": {
        "phrase": "Score situé dans la zone très faible, objectivant une difficulté majeure en {domaine}, requérant un soutien thérapeutique intensif et des adaptations pédagogiques substantielles.",
        "couleur": "#C62828",
        "recommandation": "Intervention intensive et aménagements pédagogiques importants nécessaires"
    }
}

# Interprétations pour scores T (comportement)
INTERPRETATIONS_T_SCORE = {
    "Très Élevé": {
        "phrase": "Score très élevé, cliniquement significatif, indiquant des difficultés marquées en {domaine}, nécessitant une attention clinique immédiate.",
        "couleur": "#C62828",
        "significatif": True
    },
    "Élevé (À Risque)": {
        "phrase": "Score élevé, dans la zone à risque, suggérant des difficultés notables en {domaine}, méritant une attention particulière.",
        "couleur": "#E64A19",
        "significatif": True
    },
    "Moyen Haut": {
        "phrase": "Score dans la zone moyenne haute en {domaine}, sans caractère cliniquement significatif.",
        "couleur": "#FFA726",
        "significatif": False
    },
    "Moyen": {
        "phrase": "Score dans la zone moyenne en {domaine}, ne révélant pas de difficulté particulière.",
        "couleur": "#66BB6A",
        "significatif": False
    },
    "Moyen Bas": {
        "phrase": "Score dans la zone moyenne basse en {domaine}.",
        "couleur": "#66BB6A",
        "significatif": False
    },
    "Bas": {
        "phrase": "Score bas en {domaine}.",
        "couleur": "#2E7D32",
        "significatif": False
    }
}
