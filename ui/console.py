from datetime import date

from models import Chat, Chien, Oiseau
from services import Animalerie


def saisir_donnees_communes():
    nom = input("Nom de l'animal : ")
    poids = float(input("Poids (kg) : "))
    taille = float(input("Taille (cm) : "))
    sexe = input("Sexe (M/F) : ").upper()
    age = float(input("Âge (en années) : "))
    date_arrivee = str(date.today())
    return nom, poids, taille, sexe, age, date_arrivee


def _saisir_animal():
    print("\n--- Type d'animal à ajouter ---")
    print("1. Chat | 2. Chien | 3. Oiseau")
    type_anim = input("Choix (1-3) : ")

    if type_anim not in ("1", "2", "3"):
        print("Type d'animal invalide.")
        return None

    nom, poids, taille, sexe, age, date_arr = saisir_donnees_communes()

    if type_anim == "1":
        caractere = input("Caractère (ex: câlin, farouche) : ")
        griffes = input("Griffes coupées ? (o/n) : ").lower() == "o"
        poil = input("Poil long ? (o/n) : ").lower() == "o"
        return Chat(
            nom, poids, taille, sexe, age, date_arr, caractere, griffes, poil
        )

    if type_anim == "2":
        couleur = input("Couleur du collier : ")
        dresse = input("Est-il dressé ? (o/n) : ").lower() == "o"
        race = input("Race : ")
        return Chien(
            nom, poids, taille, sexe, age, date_arr, couleur, dresse, race
        )

    couleur = input("Couleur : ")
    voliere = input("Doit vivre en volière ? (o/n) : ").lower() == "o"
    return Oiseau(nom, poids, taille, sexe, age, date_arr, couleur, voliere)


def _afficher_animaux(animalerie):
    print(
        f"\n=== LISTE DES ANIMAUX "
        f"(Date du jour : {animalerie.date_actuelle}) ==="
    )
    animaux = animalerie.lister_animaux()
    if not animaux:
        print("Aucun animal dans l'animalerie.")
        return

    for animal in animaux:
        print(f"{animal} | Cri: {animal.crier()}")


def _afficher_statistiques(animalerie):
    statistiques = animalerie.obtenir_statistiques()
    print("\n=== COMPTAGE DE LA POPULATION ===")
    print(f"Chats   : {statistiques['chats']}")
    print(f"Chiens  : {statistiques['chiens']}")
    print(f"Oiseaux : {statistiques['oiseaux']}")
    print(f"Total   : {statistiques['total']}")


def _faire_passer_jours(animalerie):
    try:
        nombre_jours = int(
            input("Combien de jours voulez-vous faire passer ? : ")
        )
        if nombre_jours <= 0:
            print("Le nombre de jours doit être supérieur à 0.")
            return
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
        return

    print(f"\n=== SIMULATION DE {nombre_jours} JOUR(S) QUI PASSE(NT) ===")
    deces = animalerie.passer_jours(nombre_jours)
    for jour, animal in deces:
        print(
            f"  [Nuit du jour {jour}] Triste nouvelle : {animal.nom} "
            f"({animal.__class__.__name__}) est décédé(e)."
        )
    print(
        f"\nSimulation terminée. Nouvelle date de l'animalerie : "
        f"{animalerie.date_actuelle}"
    )


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
            nouvel_animal = _saisir_animal()
            if nouvel_animal is not None:
                animalerie.encoder_animal(nouvel_animal)
                print(f"\n-> {nouvel_animal.nom} a été ajouté avec succès !")
        elif choix == "2":
            _afficher_animaux(animalerie)
        elif choix == "3":
            _afficher_statistiques(animalerie)
        elif choix == "4":
            _faire_passer_jours(animalerie)
        elif choix == "5":
            print("Fermeture du programme. Au revoir !")
            break
        else:
            print("Option invalide, réessayez.")
