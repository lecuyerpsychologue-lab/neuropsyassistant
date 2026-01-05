"""
Moteur de génération sémantique du rapport clinique.
"""

from typing import Dict, List, Optional
from datetime import date
from models.patient import Patient, Anamnese
from models.scores import ScoreManager, ScoreType
from models.interpretations import est_cliniquement_significatif, get_recommandation
from config.constants import WISC_V_STRUCTURE, KABC_II_STRUCTURE


class SemanticEngine:
    """Moteur de génération du rapport clinique."""
    
    def __init__(self, patient: Patient, anamnese: Anamnese, **managers):
        """
        Initialise le moteur sémantique.
        
        Args:
            patient: Informations patient
            anamnese: Données anamnestiques
            **managers: Gestionnaires de scores (wisc_v, kabc_ii, teach, nepsy_ii, etc.)
        """
        self.patient = patient
        self.anamnese = anamnese
        self.managers = managers
    
    def generate_rapport(self) -> str:
        """Génère le rapport complet en Markdown."""
        
        sections = []
        
        # En-tête
        sections.append(self._generate_header())
        
        # Anamnèse
        if self.anamnese.has_content():
            sections.append(self._generate_anamnese_section())
        
        # Observations cliniques
        sections.append(self._generate_observations_section())
        
        # Évaluation intellectuelle
        if self._has_intellectual_assessment():
            sections.append(self._generate_intellectual_section())
        
        # Évaluation attentionnelle
        if self._has_attention_assessment():
            sections.append(self._generate_attention_section())
        
        # Évaluation comportementale
        if self._has_behavioral_assessment():
            sections.append(self._generate_behavioral_section())
        
        # Synthèse
        sections.append(self._generate_synthese_section())
        
        # Recommandations
        sections.append(self._generate_recommandations_section())
        
        # Conclusion
        sections.append(self._generate_conclusion_section())
        
        return "\n\n".join(sections)
    
    def _generate_header(self) -> str:
        """Génère l'en-tête du rapport."""
        
        lines = ["# COMPTE-RENDU D'EXAMEN NEUROPSYCHOLOGIQUE", ""]
        
        if self.patient.format_nom_complet():
            lines.append(f"**Patient :** {self.patient.format_nom_complet()}")
        
        if self.patient.date_naissance:
            lines.append(f"**Date de naissance :** {self.patient.date_naissance.strftime('%d/%m/%Y')}")
        
        age = self.patient.get_age_at_exam()
        if age:
            lines.append(f"**Âge à l'examen :** {age} ans")
        
        if self.patient.date_examen:
            lines.append(f"**Date d'examen :** {self.patient.date_examen.strftime('%d/%m/%Y')}")
        
        if self.patient.classe:
            lines.append(f"**Classe :** {self.patient.classe}")
        
        if self.patient.ecole:
            lines.append(f"**École :** {self.patient.ecole}")
        
        return "\n".join(lines)
    
    def _generate_anamnese_section(self) -> str:
        """Génère la section anamnestique."""
        
        lines = ["## 1. ÉLÉMENTS ANAMNESTIQUES", ""]
        
        if self.anamnese.motif_consultation:
            lines.append("### Motif de consultation")
            lines.append(self.anamnese.motif_consultation)
            lines.append("")
        
        if self.anamnese.demandeur:
            lines.append(f"**Demandeur :** {self.anamnese.demandeur}")
            lines.append("")
        
        if any([self.anamnese.grossesse_accouchement, self.anamnese.developpement_moteur, 
                self.anamnese.developpement_langagier]):
            lines.append("### Histoire développementale")
            
            if self.anamnese.grossesse_accouchement:
                lines.append(f"**Grossesse et accouchement :** {self.anamnese.grossesse_accouchement}")
            
            if self.anamnese.developpement_moteur:
                lines.append(f"**Développement moteur :** {self.anamnese.developpement_moteur}")
            
            if self.anamnese.developpement_langagier:
                lines.append(f"**Développement langagier :** {self.anamnese.developpement_langagier}")
            
            lines.append("")
        
        if any([self.anamnese.histoire_scolaire, self.anamnese.redoublements, 
                self.anamnese.amenagements_existants]):
            lines.append("### Parcours scolaire")
            
            if self.anamnese.histoire_scolaire:
                lines.append(self.anamnese.histoire_scolaire)
            
            if self.anamnese.redoublements:
                lines.append(f"**Redoublements :** {self.anamnese.redoublements}")
            
            if self.anamnese.amenagements_existants:
                lines.append(f"**Aménagements existants :** {self.anamnese.amenagements_existants}")
            
            lines.append("")
        
        if any([self.anamnese.antecedents_medicaux, self.anamnese.antecedents_familiaux, 
                self.anamnese.suivis_actuels]):
            lines.append("### Antécédents et suivis")
            
            if self.anamnese.antecedents_medicaux:
                lines.append(f"**Antécédents médicaux :** {self.anamnese.antecedents_medicaux}")
            
            if self.anamnese.antecedents_familiaux:
                lines.append(f"**Antécédents familiaux :** {self.anamnese.antecedents_familiaux}")
            
            if self.anamnese.suivis_actuels:
                lines.append(f"**Suivis actuels :** {self.anamnese.suivis_actuels}")
            
            lines.append("")
        
        return "\n".join(lines)
    
    def _generate_observations_section(self) -> str:
        """Génère la section des observations cliniques."""
        
        lines = ["## 2. OBSERVATIONS CLINIQUES DURANT L'EXAMEN", ""]
        
        observations = []
        
        if self.anamnese.comportement:
            observations.append(f"**Comportement général :** {self.anamnese.comportement}")
        
        if self.anamnese.collaboration:
            observations.append(f"**Collaboration :** {self.anamnese.collaboration}")
        
        if self.anamnese.fatigabilite:
            observations.append(f"**Fatigabilité :** {self.anamnese.fatigabilite}")
        
        if self.anamnese.anxiete_performance:
            observations.append(f"**Anxiété de performance :** {self.anamnese.anxiete_performance}")
        
        if self.anamnese.strategies_observees:
            observations.append(f"**Stratégies observées :** {self.anamnese.strategies_observees}")
        
        if self.anamnese.autres_observations:
            observations.append(f"**Autres observations :** {self.anamnese.autres_observations}")
        
        if observations:
            lines.extend(observations)
        else:
            lines.append("L'enfant a collaboré de manière satisfaisante durant l'ensemble de l'examen.")
        
        return "\n".join(lines)
    
    def _generate_intellectual_section(self) -> str:
        """Génère la section d'évaluation intellectuelle."""
        
        lines = ["## 3. ÉVALUATION DES FONCTIONS INTELLECTUELLES", ""]
        
        # WISC-V
        wisc_v = self.managers.get('wisc_v')
        if wisc_v and wisc_v.has_scores():
            lines.append("### WISC-V - Échelle d'Intelligence de Wechsler")
            lines.append("")
            
            # Tableau des indices
            lines.append("| Indice | Score | Classification | Percentile |")
            lines.append("|--------|-------|----------------|------------|")
            
            indices_principaux = ["ICV", "IVS", "IRF", "IMT", "IVT", "IQT"]
            
            for idx in indices_principaux:
                score = wisc_v.get_score(idx)
                if score and score.is_valid():
                    percentile = score.percentile or "-"
                    lines.append(f"| {idx} | {int(score.valeur)} | {score.classification} | {percentile} |")
            
            lines.append("")
            
            # Interprétation narrative
            lines.append("#### Interprétation")
            lines.append("")
            
            for idx in indices_principaux:
                score = wisc_v.get_score(idx)
                if score and score.is_valid():
                    info = WISC_V_STRUCTURE.get(idx, {})
                    nom_complet = info.get('nom', idx)
                    lines.append(f"**{nom_complet} ({idx}) :** {score.interpretation}")
                    lines.append("")
            
            # Analyse de l'homogénéité
            hetero = wisc_v.calculate_profile_heterogeneity(["ICV", "IVS", "IRF", "IMT", "IVT"])
            
            lines.append("#### Analyse du profil")
            lines.append("")
            
            if hetero['is_homogeneous']:
                lines.append(f"Le profil cognitif apparaît **homogène** (écart maximal de {hetero['ecart_max']:.0f} points), "
                           "suggérant un développement harmonieux des différentes composantes de l'intelligence.")
            else:
                lines.append(f"Le profil cognitif présente une **hétérogénéité significative** "
                           f"(écart maximal de {hetero['ecart_max']:.0f} points), révélant des forces et faiblesses contrastées.")
                
                if hetero['scores_min'] and hetero['scores_max']:
                    min_indices = ", ".join([s.nom for s in hetero['scores_min']])
                    max_indices = ", ".join([s.nom for s in hetero['scores_max']])
                    
                    lines.append("")
                    lines.append(f"- **Points forts :** {max_indices} ({hetero['scores_max'][0].valeur:.0f})")
                    lines.append(f"- **Points faibles :** {min_indices} ({hetero['scores_min'][0].valeur:.0f})")
            
            lines.append("")
        
        # KABC-II
        kabc_ii = self.managers.get('kabc_ii')
        if kabc_ii and kabc_ii.has_scores():
            lines.append("### KABC-II - Batterie d'Évaluation de Kaufman")
            lines.append("")
            
            lines.append("| Indice | Score | Classification | Percentile |")
            lines.append("|--------|-------|----------------|------------|")
            
            for score in kabc_ii.get_valid_scores():
                percentile = score.percentile or "-"
                lines.append(f"| {score.nom} | {int(score.valeur)} | {score.classification} | {percentile} |")
            
            lines.append("")
            
            lines.append("#### Interprétation")
            lines.append("")
            
            for score in kabc_ii.get_valid_scores():
                info = KABC_II_STRUCTURE.get(score.nom, {})
                nom_complet = info.get('nom', score.nom)
                lines.append(f"**{nom_complet} ({score.nom}) :** {score.interpretation}")
                lines.append("")
        
        return "\n".join(lines)
    
    def _generate_attention_section(self) -> str:
        """Génère la section d'évaluation attentionnelle."""
        
        lines = ["## 4. ÉVALUATION DES FONCTIONS ATTENTIONNELLES ET EXÉCUTIVES", ""]
        
        # TEA-Ch
        teach = self.managers.get('teach')
        if teach and teach.has_scores():
            lines.append("### TEA-Ch - Test d'Évaluation de l'Attention")
            lines.append("")
            
            lines.append("| Subtest | Score | Classification |")
            lines.append("|---------|-------|----------------|")
            
            for score in teach.get_valid_scores():
                lines.append(f"| {score.nom} | {int(score.valeur)} | {score.classification} |")
            
            lines.append("")
            
            # Interprétation
            fragilites = [s for s in teach.get_valid_scores() 
                         if est_cliniquement_significatif(s.valeur, ScoreType.SCALAIRE)]
            
            if fragilites:
                lines.append(f"L'évaluation révèle des **fragilités attentionnelles** dans {len(fragilites)} domaine(s) :")
                lines.append("")
                for score in fragilites:
                    lines.append(f"- {score.nom} : {score.interpretation}")
            else:
                lines.append("Les capacités attentionnelles apparaissent **préservées** dans l'ensemble.")
            
            lines.append("")
        
        # NEPSY-II
        nepsy = self.managers.get('nepsy_ii')
        if nepsy and nepsy.has_scores():
            lines.append("### NEPSY-II - Bilan Neuropsychologique")
            lines.append("")
            
            lines.append("| Subtest | Score | Classification |")
            lines.append("|---------|-------|----------------|")
            
            for score in nepsy.get_valid_scores():
                lines.append(f"| {score.nom} | {int(score.valeur)} | {score.classification} |")
            
            lines.append("")
        
        return "\n".join(lines)
    
    def _generate_behavioral_section(self) -> str:
        """Génère la section d'évaluation comportementale."""
        
        lines = ["## 5. ÉVALUATION COMPORTEMENTALE", ""]
        
        # Brown
        brown = self.managers.get('brown')
        if brown and brown.has_scores():
            lines.append("### Échelle Brown de Déficit d'Attention")
            lines.append("")
            
            lines.append("| Échelle | Score T | Classification |")
            lines.append("|---------|---------|----------------|")
            
            for score in brown.get_valid_scores():
                lines.append(f"| {score.nom} | {int(score.valeur)} | {score.classification} |")
            
            lines.append("")
            
            # Items significatifs
            significatifs = [s for s in brown.get_valid_scores() 
                           if est_cliniquement_significatif(s.valeur, ScoreType.T_SCORE)]
            
            if significatifs:
                lines.append(f"**{len(significatifs)} échelle(s) cliniquement significative(s) :**")
                lines.append("")
                for score in significatifs:
                    lines.append(f"- {score.nom} : {score.interpretation}")
                lines.append("")
            else:
                lines.append("Aucune échelle ne présente de score cliniquement significatif.")
                lines.append("")
        
        # Conners Parent
        conners_parent = self.managers.get('conners_parent')
        if conners_parent and conners_parent.has_scores():
            lines.append("### Conners-3 - Version Parent")
            lines.append("")
            
            lines.append("| Échelle | Score T | Classification |")
            lines.append("|---------|---------|----------------|")
            
            for score in conners_parent.get_valid_scores():
                lines.append(f"| {score.nom} | {int(score.valeur)} | {score.classification} |")
            
            lines.append("")
            
            # Items significatifs
            significatifs_p = [s for s in conners_parent.get_valid_scores() 
                             if est_cliniquement_significatif(s.valeur, ScoreType.T_SCORE)]
            
            if significatifs_p:
                lines.append(f"**{len(significatifs_p)} échelle(s) cliniquement significative(s) (Parent) :**")
                lines.append("")
                for score in significatifs_p:
                    lines.append(f"- {score.nom} : {score.interpretation}")
                lines.append("")
        
        # Conners Enseignant
        conners_teacher = self.managers.get('conners_teacher')
        if conners_teacher and conners_teacher.has_scores():
            lines.append("### Conners-3 - Version Enseignant")
            lines.append("")
            
            lines.append("| Échelle | Score T | Classification |")
            lines.append("|---------|---------|----------------|")
            
            for score in conners_teacher.get_valid_scores():
                lines.append(f"| {score.nom} | {int(score.valeur)} | {score.classification} |")
            
            lines.append("")
            
            # Items significatifs
            significatifs_t = [s for s in conners_teacher.get_valid_scores() 
                             if est_cliniquement_significatif(s.valeur, ScoreType.T_SCORE)]
            
            if significatifs_t:
                lines.append(f"**{len(significatifs_t)} échelle(s) cliniquement significative(s) (Enseignant) :**")
                lines.append("")
                for score in significatifs_t:
                    lines.append(f"- {score.nom} : {score.interpretation}")
                lines.append("")
        
        # Analyse croisée
        if (conners_parent and conners_parent.has_scores() and 
            conners_teacher and conners_teacher.has_scores()):
            
            lines.append("#### Analyse croisée Parent / Enseignant")
            lines.append("")
            
            convergences = []
            divergences = []
            
            for score_p in conners_parent.get_valid_scores():
                score_t = conners_teacher.get_score(score_p.nom)
                if score_t and score_t.is_valid():
                    diff = abs(score_p.valeur - score_t.valeur)
                    if diff < 10:
                        convergences.append(score_p.nom)
                    else:
                        divergences.append((score_p.nom, diff))
            
            if convergences:
                lines.append(f"**Convergences** observées sur {len(convergences)} échelle(s), "
                           "suggérant une cohérence inter-informateurs.")
            
            if divergences:
                lines.append("")
                lines.append(f"**Divergences** notables (écart ≥10 points) sur {len(divergences)} échelle(s) :")
                for nom, diff in divergences:
                    lines.append(f"- {nom} (écart de {diff:.0f} points)")
                lines.append("")
                lines.append("Ces divergences peuvent refléter des manifestations contextuelles "
                           "différentes selon l'environnement (domicile vs école).")
            
            lines.append("")
        
        return "\n".join(lines)
    
    def _generate_synthese_section(self) -> str:
        """Génère la synthèse clinique."""
        
        lines = ["## 6. SYNTHÈSE CLINIQUE", ""]
        
        # Profil intellectuel
        wisc_v = self.managers.get('wisc_v')
        if wisc_v and wisc_v.has_scores():
            iqt = wisc_v.get_score("IQT")
            if iqt and iqt.is_valid():
                lines.append(f"Le fonctionnement intellectuel global se situe dans la zone **{iqt.classification.lower()}** "
                           f"(QIT = {int(iqt.valeur)}), reflétant {self._get_synthese_iqt(iqt.classification)}.")
            
            hetero = wisc_v.calculate_profile_heterogeneity(["ICV", "IVS", "IRF", "IMT", "IVT"])
            if not hetero['is_homogeneous']:
                lines.append("")
                lines.append("Le profil présente toutefois une **hétérogénéité significative**, "
                           "avec des compétences contrastées selon les domaines cognitifs évalués.")
            
            lines.append("")
        
        # Points forts
        forces = self._identify_forces()
        if forces:
            lines.append("**Points d'appui identifiés :**")
            lines.append("")
            for force in forces:
                lines.append(f"- {force}")
            lines.append("")
        
        # Fragilités
        fragilites = self._identify_fragilites()
        if fragilites:
            lines.append("**Fragilités objectivées :**")
            lines.append("")
            for fragilite in fragilites:
                lines.append(f"- {fragilite}")
            lines.append("")
        
        return "\n".join(lines)
    
    def _generate_recommandations_section(self) -> str:
        """Génère les recommandations personnalisées."""
        
        lines = ["## 7. RECOMMANDATIONS", ""]
        
        recommandations = set()
        
        # Recommandations basées sur les scores
        for manager_name, manager in self.managers.items():
            if manager and manager.has_scores():
                for score in manager.get_valid_scores():
                    if score.type_score == ScoreType.STANDARD:
                        reco = get_recommandation(score.classification)
                        if reco:
                            recommandations.add(reco)
        
        # Recommandations spécifiques
        fragilites = self._identify_fragilites()
        
        if any("attention" in f.lower() for f in fragilites):
            recommandations.add("Prévoir des temps de pause réguliers et limiter les distracteurs environnementaux")
            recommandations.add("Privilégier les consignes courtes et vérifier la compréhension")
        
        if any("mémoire" in f.lower() for f in fragilites):
            recommandations.add("Fournir des supports écrits pour compenser les difficultés mnésiques")
            recommandations.add("Encourager l'utilisation d'outils d'aide à la mémorisation (agenda, pictogrammes)")
        
        if any("vitesse" in f.lower() or "traitement" in f.lower() for f in fragilites):
            recommandations.add("Accorder du temps supplémentaire pour les évaluations et exercices")
            recommandations.add("Réduire la quantité de travail écrit demandé")
        
        # Recommandations comportementales
        conners_parent = self.managers.get('conners_parent')
        conners_teacher = self.managers.get('conners_teacher')
        
        if (conners_parent and conners_parent.has_scores()) or (conners_teacher and conners_teacher.has_scores()):
            significatifs_comportement = []
            
            if conners_parent:
                significatifs_comportement.extend([s for s in conners_parent.get_valid_scores() 
                                                  if est_cliniquement_significatif(s.valeur, ScoreType.T_SCORE)])
            
            if conners_teacher:
                significatifs_comportement.extend([s for s in conners_teacher.get_valid_scores() 
                                                   if est_cliniquement_significatif(s.valeur, ScoreType.T_SCORE)])
            
            if significatifs_comportement:
                recommandations.add("Envisager un accompagnement thérapeutique ciblé (guidance parentale, thérapie cognitivo-comportementale)")
                recommandations.add("Favoriser un cadre structuré et des routines prévisibles")
        
        # Recommandations générales
        recommandations.add("Maintenir une communication régulière entre la famille, l'école et les professionnels suivant l'enfant")
        recommandations.add("Valoriser systématiquement les efforts et les progrès réalisés")
        
        for i, reco in enumerate(sorted(recommandations), 1):
            lines.append(f"{i}. {reco}")
        
        lines.append("")
        
        return "\n".join(lines)
    
    def _generate_conclusion_section(self) -> str:
        """Génère la conclusion."""
        
        lines = ["## 8. CONCLUSION", ""]
        
        lines.append(f"L'évaluation neuropsychologique de {self.patient.prenom or 'l\\'enfant'} "
                    "met en évidence un profil cognitif et comportemental nuancé, "
                    "avec des forces sur lesquelles s'appuyer et des fragilités nécessitant un accompagnement adapté.")
        lines.append("")
        
        lines.append("Les recommandations formulées visent à optimiser le développement de l'enfant "
                    "et à favoriser son épanouissement tant sur le plan scolaire que personnel.")
        lines.append("")
        
        lines.append("Un suivi régulier est préconisé afin d'ajuster les aménagements et accompagnements "
                    "en fonction de l'évolution de l'enfant.")
        lines.append("")
        
        if self.patient.date_examen:
            lines.append(f"Fait le {self.patient.date_examen.strftime('%d/%m/%Y')}")
        
        return "\n".join(lines)
    
    def _get_synthese_iqt(self, classification: str) -> str:
        """Retourne une phrase de synthèse pour le QIT."""
        
        syntheses = {
            "Très Supérieur": "des capacités intellectuelles exceptionnelles",
            "Supérieur": "un fonctionnement intellectuel au-dessus de la moyenne",
            "Moyen Fort": "des compétences cognitives satisfaisantes",
            "Moyen": "un fonctionnement intellectuel dans la norme attendue",
            "Moyen Faible": "un fonctionnement intellectuel fragile",
            "Limite (Zone Frontière)": "des difficultés intellectuelles significatives",
            "Très Faible": "des difficultés intellectuelles majeures"
        }
        
        return syntheses.get(classification, "un profil cognitif particulier")
    
    def _identify_forces(self) -> List[str]:
        """Identifie les points forts du profil."""
        
        forces = []
        
        for manager_name, manager in self.managers.items():
            if manager and manager.has_scores():
                for score in manager.get_valid_scores():
                    if score.type_score == ScoreType.STANDARD and score.valeur >= 110:
                        forces.append(f"{score.nom} : {score.domaine} ({score.classification})")
                    elif score.type_score == ScoreType.SCALAIRE and score.valeur >= 12:
                        forces.append(f"{score.nom} ({score.classification})")
        
        return forces[:5]  # Limiter à 5 forces principales
    
    def _identify_fragilites(self) -> List[str]:
        """Identifie les fragilités du profil."""
        
        fragilites = []
        
        for manager_name, manager in self.managers.items():
            if manager and manager.has_scores():
                for score in manager.get_valid_scores():
                    if score.type_score == ScoreType.STANDARD and score.valeur < 85:
                        fragilites.append(f"{score.nom} : {score.domaine} ({score.classification})")
                    elif score.type_score == ScoreType.SCALAIRE and score.valeur <= 7:
                        fragilites.append(f"{score.nom} ({score.classification})")
                    elif score.type_score == ScoreType.T_SCORE and est_cliniquement_significatif(score.valeur, ScoreType.T_SCORE):
                        fragilites.append(f"{score.nom} ({score.classification})")
        
        return fragilites
    
    def _has_intellectual_assessment(self) -> bool:
        """Vérifie si une évaluation intellectuelle a été réalisée."""
        wisc_v = self.managers.get('wisc_v')
        kabc_ii = self.managers.get('kabc_ii')
        return (wisc_v and wisc_v.has_scores()) or (kabc_ii and kabc_ii.has_scores())
    
    def _has_attention_assessment(self) -> bool:
        """Vérifie si une évaluation attentionnelle a été réalisée."""
        teach = self.managers.get('teach')
        nepsy = self.managers.get('nepsy_ii')
        return (teach and teach.has_scores()) or (nepsy and nepsy.has_scores())
    
    def _has_behavioral_assessment(self) -> bool:
        """Vérifie si une évaluation comportementale a été réalisée."""
        brown = self.managers.get('brown')
        conners_p = self.managers.get('conners_parent')
        conners_t = self.managers.get('conners_teacher')
        return (brown and brown.has_scores()) or (conners_p and conners_p.has_scores()) or \
               (conners_t and conners_t.has_scores())


def generate_rapport_complet(patient: Patient, anamnese: Anamnese, **managers) -> str:
    """
    Fonction utilitaire pour générer un rapport complet.
    
    Args:
        patient: Informations patient
        anamnese: Données anamnestiques
        **managers: Gestionnaires de scores
    
    Returns:
        Rapport complet en Markdown
    """
    engine = SemanticEngine(patient, anamnese, **managers)
    return engine.generate_rapport()
