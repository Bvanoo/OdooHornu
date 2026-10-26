from models.animal import Animal


class Chat(Animal):
    def __init__(
        self,
        nom,
        poids,
        taille,
        sexe,
        age,
        date_arrivee,
        caractere,
        griffes_coupees,
        poil_long,
    ):
        super().__init__(
            nom, poids, taille, sexe, age, date_arrivee, proba_deces=0.005
        )
        self.caractere = caractere
        self.griffes_coupees = griffes_coupees
        self.poil_long = poil_long

    @property
    def age_humain(self):
        if self.age <= 1:
            return round(self.age * 15, 1)
        elif self.age <= 2:
            return round(15 + (self.age - 1) * 9, 1)
        return round(24 + (self.age - 2) * 4, 1)

    def crier(self):
        return "Miaou !"

    def __str__(self):
        griffes = "Oui" if self.griffes_coupees else "Non"
        poil = "Long" if self.poil_long else "Court"
        return (
            f"[CHAT] {super().__str__()} | Caractère: {self.caractere} | "
            f"Griffes coupées: {griffes} | Poil: {poil}"
        )
