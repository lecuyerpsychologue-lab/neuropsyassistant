"""
Modèle de données pour les patients et l'anamnèse.
"""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List


@dataclass
class Patient:
    """Informations sur le patient."""
    
    nom: str = ""
    prenom: str = ""
    date_naissance: Optional[date] = None
    date_examen: Optional[date] = None
    classe: str = ""
    ecole: str = ""
    
    def get_age_at_exam(self) -> Optional[int]:
        """Calcule l'âge du patient à la date d'examen."""
        if self.date_naissance and self.date_examen:
            age = self.date_examen.year - self.date_naissance.year
            # Ajustement si l'anniversaire n'est pas encore passé
            if (self.date_examen.month, self.date_examen.day) < \
               (self.date_naissance.month, self.date_naissance.day):
                age -= 1
            return age
        return None
    
    def format_nom_complet(self) -> str:
        """Retourne le nom complet du patient."""
        return f"{self.prenom} {self.nom}".strip()


@dataclass
class Anamnese:
    """Données anamnestiques du patient."""
    
    # Motif de consultation
    motif_consultation: str = ""
    demandeur: str = ""
    
    # Histoire développementale
    grossesse_accouchement: str = ""
    developpement_moteur: str = ""
    developpement_langagier: str = ""
    
    # Parcours scolaire
    histoire_scolaire: str = ""
    redoublements: str = ""
    amenagements_existants: str = ""
    
    # Antécédents
    antecedents_medicaux: str = ""
    antecedents_familiaux: str = ""
    suivis_actuels: str = ""
    
    # Observations cliniques durant le test
    comportement: str = ""
    collaboration: str = ""
    fatigabilite: str = ""
    anxiete_performance: str = ""
    strategies_observees: str = ""
    autres_observations: str = ""
    
    def has_content(self) -> bool:
        """Vérifie si l'anamnèse contient des données."""
        return any([
            self.motif_consultation,
            self.demandeur,
            self.grossesse_accouchement,
            self.developpement_moteur,
            self.developpement_langagier,
            self.histoire_scolaire,
            self.redoublements,
            self.amenagements_existants,
            self.antecedents_medicaux,
            self.antecedents_familiaux,
            self.suivis_actuels,
            self.comportement,
            self.collaboration,
            self.fatigabilite,
            self.anxiete_performance,
            self.strategies_observees,
            self.autres_observations
        ])
