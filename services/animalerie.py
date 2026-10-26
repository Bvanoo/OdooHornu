from datetime import date, timedelta

from models import Animal, Chat, Chien, Oiseau


class Animalerie:
    def __init__(self):
        self.animaux = []
        self.date_actuelle = date.today()

    def encoder_animal(self, animal):
        """Ajoute un animal au registre de l'animalerie."""
        self.animaux.append(animal)

    def lister_animaux(self):
        """Retourne les animaux enregistrés sans exposer la liste interne."""
        return list(self.animaux)

    def obtenir_statistiques(self):
        """Retourne le nombre d'animaux par espèce et le total."""
        return {
            "chats": sum(1 for animal in self.animaux if isinstance(animal, Chat)),
            "chiens": sum(
                1 for animal in self.animaux if isinstance(animal, Chien)
            ),
            "oiseaux": sum(
                1 for animal in self.animaux if isinstance(animal, Oiseau)
            ),
            "total": len(self.animaux),
        }

    def passer_jours(self, nombre_jours):
        """Simule le vieillissement et retourne les décès avec leur jour."""
        deces = []

        for jour in range(1, nombre_jours + 1):
            self.date_actuelle += timedelta(days=1)

            for animal in self.animaux:
                animal.age += 1 / 365

            morts_du_jour = [
                animal
                for animal in self.animaux
                if animal.tester_deces_nuit()
            ]
            for animal in morts_du_jour:
                deces.append((jour, animal))
                self.animaux.remove(animal)

        return deces
