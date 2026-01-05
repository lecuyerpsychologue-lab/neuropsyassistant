"""
Algorithmes d'interprétation sémantique des scores.
"""

from typing import Tuple, Optional
from config.constants import (
    STANDARD_CLASSIFICATIONS,
    SCALAIRE_CLASSIFICATIONS,
    T_SCORE_CLASSIFICATIONS,
    INTERPRETATIONS_SEMANTIQUES,
    INTERPRETATIONS_T_SCORE,
    ScoreType
)


def get_classification(valeur: float, score_type: ScoreType) -> Tuple[str, Optional[str]]:
    """
    Détermine la classification d'un score selon son type.
    
    Args:
        valeur: Valeur du score
        score_type: Type de score (STANDARD, SCALAIRE, T_SCORE)
    
    Returns:
        Tuple (classification, percentile) où percentile peut être None
    """
    if score_type == ScoreType.STANDARD:
        for min_val, max_val, label, percentile in STANDARD_CLASSIFICATIONS:
            if min_val <= valeur <= max_val:
                return label, percentile
        return "Non classifié", None
    
    elif score_type == ScoreType.SCALAIRE:
        for min_val, max_val, label in SCALAIRE_CLASSIFICATIONS:
            if min_val <= valeur <= max_val:
                return label, None
        return "Non classifié", None
    
    elif score_type == ScoreType.T_SCORE:
        for min_val, max_val, label, significatif in T_SCORE_CLASSIFICATIONS:
            if min_val <= valeur <= max_val:
                return label, None
        return "Non classifié", None
    
    return "Type de score invalide", None


def interprete_score(valeur: float, score_type: ScoreType, domaine: str = "") -> str:
    """
    Génère une interprétation sémantique d'un score.
    
    Args:
        valeur: Valeur du score
        score_type: Type de score
        domaine: Domaine évalué (ex: "compréhension verbale")
    
    Returns:
        Phrase d'interprétation clinique
    """
    classification, _ = get_classification(valeur, score_type)
    
    if score_type == ScoreType.T_SCORE:
        interp_data = INTERPRETATIONS_T_SCORE.get(classification)
        if interp_data:
            phrase = interp_data["phrase"]
            if domaine:
                phrase = phrase.replace("{domaine}", domaine)
            return phrase
        return f"Score de {valeur} ({classification})."
    
    else:  # STANDARD ou SCALAIRE
        interp_data = INTERPRETATIONS_SEMANTIQUES.get(classification)
        if interp_data:
            phrase = interp_data["phrase"]
            if domaine:
                phrase = phrase.replace("{domaine}", domaine)
            return phrase
        return f"Score de {valeur} ({classification})."


def est_cliniquement_significatif(valeur: float, score_type: ScoreType) -> bool:
    """
    Détermine si un score est cliniquement significatif.
    
    Args:
        valeur: Valeur du score
        score_type: Type de score
    
    Returns:
        True si cliniquement significatif
    """
    if score_type == ScoreType.T_SCORE:
        # Significatif si T >= 65
        return valeur >= 65
    
    elif score_type == ScoreType.STANDARD:
        # Significatif si en zone limite ou très faible
        return valeur < 80
    
    elif score_type == ScoreType.SCALAIRE:
        # Significatif si en zone limite ou très faible
        return valeur <= 5
    
    return False


def get_couleur_score(classification: str, score_type: ScoreType) -> str:
    """
    Retourne le code couleur associé à une classification.
    
    Args:
        classification: Classification du score
        score_type: Type de score
    
    Returns:
        Code couleur hexadécimal
    """
    if score_type == ScoreType.T_SCORE:
        interp_data = INTERPRETATIONS_T_SCORE.get(classification)
        if interp_data:
            return interp_data.get("couleur", "#808080")
    else:
        interp_data = INTERPRETATIONS_SEMANTIQUES.get(classification)
        if interp_data:
            return interp_data.get("couleur", "#808080")
    
    return "#808080"  # Gris par défaut


def get_recommandation(classification: str) -> str:
    """
    Retourne une recommandation basée sur la classification.
    
    Args:
        classification: Classification du score
    
    Returns:
        Texte de recommandation
    """
    interp_data = INTERPRETATIONS_SEMANTIQUES.get(classification)
    if interp_data:
        return interp_data.get("recommandation", "")
    return ""


def calculer_percentile(valeur: float, moyenne: float = 100, ecart_type: float = 15) -> float:
    """
    Calcule le percentile approximatif d'un score selon une distribution normale.
    
    Args:
        valeur: Valeur du score
        moyenne: Moyenne de la distribution
        ecart_type: Écart-type de la distribution
    
    Returns:
        Percentile (0-100)
    """
    import numpy as np
    from scipy import stats
    
    try:
        z_score = (valeur - moyenne) / ecart_type
        percentile = stats.norm.cdf(z_score) * 100
        return round(percentile, 1)
    except:
        # Si scipy n'est pas disponible, approximation simple
        if valeur >= moyenne + 2 * ecart_type:
            return 98
        elif valeur >= moyenne + ecart_type:
            return 84
        elif valeur >= moyenne:
            return 50
        elif valeur >= moyenne - ecart_type:
            return 16
        else:
            return 2
