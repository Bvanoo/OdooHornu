from models.animal import Animal


class Oiseau(Animal):
    def __init__(
        self,
        nom,
        poids,
        taille,
        sexe,
        age,
        date_arrivee,
        couleur,
        besoin_voliere,
    ):
        super().__init__(
            nom, poids, taille, sexe, age, date_arrivee, proba_deces=0.03
        )
        self.couleur = couleur
        self.besoin_voliere = besoin_voliere

    @property
    def age_humain(self):
        return round(self.age * 9, 1)

    def crier(self):
        return "Cui cui !"

    def __str__(self):
        habitat = "Volière" if self.besoin_voliere else "Petite cage"
        return (
            f"[OISEAU] {super().__str__()} | Couleur: {self.couleur} | "
            f"Habitat: {habitat}"
        )
