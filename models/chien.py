from models.animal import Animal


class Chien(Animal):
    def __init__(
        self,
        nom,
        poids,
        taille,
        sexe,
        age,
        date_arrivee,
        couleur_collier,
        dresse,
        race,
    ):
        super().__init__(
            nom, poids, taille, sexe, age, date_arrivee, proba_deces=0.01
        )
        self.couleur_collier = couleur_collier
        self.dresse = dresse
        self.race = race

    @property
    def age_humain(self):
        if self.age <= 1:
            return round(self.age * 15, 1)
        elif self.age <= 2:
            return round(15 + (self.age - 1) * 9, 1)
        return round(24 + (self.age - 2) * 5, 1)

    def crier(self):
        return "Wouaf !"

    def __str__(self):
        dresse_str = "Oui" if self.dresse else "Non"
        return (
            f"[CHIEN] {super().__str__()} | Race: {self.race} | "
            f"Collier: {self.couleur_collier} | Dressé: {dresse_str}"
        )
