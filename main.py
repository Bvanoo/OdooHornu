from datetime import date, timedelta
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
        """Calcul de l'âge humain équivalent (comportement par défaut)"""
        return round(self.age * 7, 1)

    def crier(self):
        """Comportement commun à tous les animaux"""
        return "fait un bruit"

    def tester_deces_nuit(self):
        """Vérifie si l'animal est décédé pendant la nuit selon sa probabilité"""
        return random.random() < self.proba_deces

    def __str__(self):
        age_affiche = (
            int(self.age) if self.age.is_integer() else round(self.age, 2)
        )
        return (
            f"Nom: {self.nom} | Poids: {self.poids}kg | Taille: {self.taille}cm | "
            f"Sexe: {self.sexe} | Âge: {age_affiche} ans (Équiv. humain: {self.age_humain} ans) | "
            f"Arrivée: {self.date_arrivee}"
        )


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
        else:
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
        else:
            return round(24 + (self.age - 2) * 5, 1)

    def crier(self):
        return "Wouaf !"

    def __str__(self):
        dresse_str = "Oui" if self.dresse else "Non"
        return (
            f"[CHIEN] {super().__str__()} | Race: {self.race} | "
            f"Collier: {self.couleur_collier} | Dressé: {dresse_str}"
        )


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


class Animalerie:

    def __init__(self):
        self.animaux = []
        self.date_actuelle = date.today()

    def encoder_animal(self, animal):
        """Ajoute un animal dans le registre de l'animalerie"""
        self.animaux.append(animal)
        print(f"\n-> {animal.nom} a été ajouté avec succès !")

    def lister_animaux(self):
        """Affiche les caractéristiques de tous les animaux encodés"""
        print(
            f"\n=== LISTE DES ANIMAUX (Date du jour : {self.date_actuelle}) ==="
        )
        if not self.animaux:
            print("Aucun animal dans l'animalerie.")
            return

        for animal in self.animaux:
            print(f"{animal} | Cri: {animal.crier()}")

    def afficher_statistiques(self):
        """Affiche le nombre total de chats, chiens et oiseaux"""
        nb_chats = sum(1 for a in self.animaux if isinstance(a, Chat))
        nb_chiens = sum(1 for a in self.animaux if isinstance(a, Chien))
        nb_oiseaux = sum(1 for a in self.animaux if isinstance(a, Oiseau))

        print("\n=== COMPTAGE DE LA POPULATION ===")
        print(f"Chats   : {nb_chats}")
        print(f"Chiens  : {nb_chiens}")
        print(f"Oiseaux : {nb_oiseaux}")
        print(f"Total   : {len(self.animaux)}")

    def passer_jours(self, nombre_jours):
        """Simule le passage de N jours (vieillissement + tests de décès quotidiens)"""
        print(
            f"\n=== SIMULATION DE {nombre_jours} JOUR(S) QUI PASSE(NT) ==="
        )

        for j in range(1, nombre_jours + 1):
            self.date_actuelle += timedelta(days=1)

            for animal in self.animaux:
                animal.age += 1 / 365

            morts_du_jour = []
            for animal in self.animaux:
                if animal.tester_deces_nuit():
                    morts_du_jour.append(animal)

            # Retrait des animaux décédés
            for animal in morts_du_jour:
                print(
                    f"  [Nuit du jour {j}] Triste nouvelle : {animal.nom} ({animal.__class__.__name__}) est décédé(e)."
                )
                self.animaux.remove(animal)

        print(
            f"\nSimulation terminée. Nouvelle date de l'animalerie : {self.date_actuelle}"
        )


# ==========================================
# INTERFACE CONSOLE INTERACTIVE
# ==========================================
def saisir_donnees_communes():
    nom = input("Nom de l'animal : ")
    poids = float(input("Poids (kg) : "))
    taille = float(input("Taille (cm) : "))
    sexe = input("Sexe (M/F) : ").upper()
    age = float(input("Âge (en années) : "))
    date_arrivee = str(date.today())
    return nom, poids, taille, sexe, age, date_arrivee


def menu():
    animalerie = Animalerie()

    while True:
        print("\n=================================")
        print("     GESTION DE L'ANIMALERIE     ")
        print("=================================")
        print("1. Encoder un nouvel animal")
        print("2. Lister tous les animaux")
        print("3. Afficher les statistiques de population")
        print("4. Faire passer des jours")
        print("5. Quitter")

        choix = input("Choisissez une option (1-5) : ")

        if choix == "1":
            print("\n--- Type d'animal à ajouter ---")
            print("1. Chat | 2. Chien | 3. Oiseau")
            type_anim = input("Choix (1-3) : ")

            if type_anim in ["1", "2", "3"]:
                nom, poids, taille, sexe, age, date_arr = (
                    saisir_donnees_communes()
                )

                if type_anim == "1":
                    caractere = input("Caractère (ex: câlin, farouche) : ")
                    griffes = (
                        input("Griffes coupées ? (o/n) : ").lower() == "o"
                    )
                    poil = input("Poil long ? (o/n) : ").lower() == "o"
                    nouvel_animal = Chat(
                        nom,
                        poids,
                        taille,
                        sexe,
                        age,
                        date_arr,
                        caractere,
                        griffes,
                        poil,
                    )

                elif type_anim == "2":
                    couleur = input("Couleur du collier : ")
                    dresse = input("Est-il dressé ? (o/n) : ").lower() == "o"
                    race = input("Race : ")
                    nouvel_animal = Chien(
                        nom,
                        poids,
                        taille,
                        sexe,
                        age,
                        date_arr,
                        couleur,
                        dresse,
                        race,
                    )

                elif type_anim == "3":
                    couleur = input("Couleur : ")
                    voliere = (
                        input("Doit vivre en volière ? (o/n) : ").lower()
                        == "o"
                    )
                    nouvel_animal = Oiseau(
                        nom,
                        poids,
                        taille,
                        sexe,
                        age,
                        date_arr,
                        couleur,
                        voliere,
                    )

                animalerie.encoder_animal(nouvel_animal)
            else:
                print("Type d'animal invalide.")

        elif choix == "2":
            animalerie.lister_animaux()

        elif choix == "3":
            animalerie.afficher_statistiques()

        elif choix == "4":
            try:
                nb = int(
                    input("Combien de jours voulez-vous faire passer ? : ")
                )
                if nb > 0:
                    animalerie.passer_jours(nb)
                else:
                    print("Le nombre de jours doit être supérieur à 0.")
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

        elif choix == "5":
            print("Fermeture du programme. Au revoir !")
            break
        else:
            print("Option invalide, réessayez.")


if __name__ == "__main__":
    menu()