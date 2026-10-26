import random


class Animal:
    def __init__(self, nom, poids, taille, sexe, age, date_arrivee, proba_deces):
        self.nom = nom
        self.poids = poids
        self.taille = taille
        self.sexe = sexe
        self.age = age
        self.date_arrivee = date_arrivee
        self.proba_deces = proba_deces

    @property
    def age_humain(self):
        """Calcul de l'âge humain équivalent (comportement par défaut)."""
        return round(self.age * 7, 1)

    def crier(self):
        """Comportement commun à tous les animaux."""
        return "fait un bruit"

    def tester_deces_nuit(self):
        """Vérifie si l'animal est décédé pendant la nuit."""
        return random.random() < self.proba_deces

    def __str__(self):
        age_affiche = (
            int(self.age) if self.age.is_integer() else round(self.age, 2)
        )
        return (
            f"Nom: {self.nom} | Poids: {self.poids}kg | Taille: {self.taille}cm | "
            f"Sexe: {self.sexe} | Âge: {age_affiche} ans "
            f"(Équiv. humain: {self.age_humain} ans) | "
            f"Arrivée: {self.date_arrivee}"
        )
