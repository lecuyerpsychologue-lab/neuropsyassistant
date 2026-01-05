"""
Gestion des scores psychométriques.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum


class ScoreType(Enum):
    """Types de scores psychométriques."""
    STANDARD = "standard"  # M=100, ET=15
    SCALAIRE = "scalaire"  # M=10, ET=3
    T_SCORE = "t_score"    # M=50, ET=10


@dataclass
class Score:
    """Représente un score psychométrique."""
    
    nom: str
    valeur: Optional[float]
    type_score: ScoreType
    domaine: str = ""
    percentile: Optional[str] = None
    classification: str = ""
    interpretation: str = ""
    
    def is_valid(self) -> bool:
        """Vérifie si le score est valide (valeur renseignée)."""
        return self.valeur is not None
    
    def __str__(self) -> str:
        """Représentation textuelle du score."""
        if not self.is_valid():
            return f"{self.nom}: Non renseigné"
        return f"{self.nom}: {self.valeur} ({self.classification})"


@dataclass
class ScoreManager:
    """Gestionnaire de scores pour un test ou une batterie."""
    
    nom_test: str
    scores: Dict[str, Score] = field(default_factory=dict)
    
    def add_score(self, score: Score) -> None:
        """Ajoute un score au gestionnaire."""
        self.scores[score.nom] = score
    
    def get_score(self, nom: str) -> Optional[Score]:
        """Récupère un score par son nom."""
        return self.scores.get(nom)
    
    def get_valid_scores(self) -> List[Score]:
        """Retourne la liste des scores valides."""
        return [s for s in self.scores.values() if s.is_valid()]
    
    def has_scores(self) -> bool:
        """Vérifie si au moins un score est renseigné."""
        return len(self.get_valid_scores()) > 0
    
    def get_scores_by_type(self, score_type: ScoreType) -> List[Score]:
        """Retourne les scores d'un type donné."""
        return [s for s in self.get_valid_scores() if s.type_score == score_type]
    
    def calculate_profile_heterogeneity(self, score_names: List[str]) -> Dict[str, any]:
        """
        Calcule l'hétérogénéité d'un profil à partir d'une liste de scores.
        
        Returns:
            Dict contenant 'is_homogeneous', 'ecart_max', 'scores_min', 'scores_max'
        """
        from config.constants import HETEROGENEITE_SEUIL
        
        valid_scores = []
        for nom in score_names:
            score = self.get_score(nom)
            if score and score.is_valid():
                valid_scores.append(score)
        
        if len(valid_scores) < 2:
            return {
                'is_homogeneous': True,
                'ecart_max': 0,
                'scores_min': [],
                'scores_max': []
            }
        
        valeurs = [s.valeur for s in valid_scores]
        min_val = min(valeurs)
        max_val = max(valeurs)
        ecart = max_val - min_val
        
        scores_min = [s for s in valid_scores if s.valeur == min_val]
        scores_max = [s for s in valid_scores if s.valeur == max_val]
        
        return {
            'is_homogeneous': ecart < HETEROGENEITE_SEUIL,
            'ecart_max': ecart,
            'scores_min': scores_min,
            'scores_max': scores_max
        }
    
    def to_dict(self) -> Dict:
        """Convertit le gestionnaire en dictionnaire."""
        return {
            'nom_test': self.nom_test,
            'scores': {nom: {
                'valeur': score.valeur,
                'classification': score.classification,
                'percentile': score.percentile,
                'interpretation': score.interpretation
            } for nom, score in self.scores.items() if score.is_valid()}
        }
