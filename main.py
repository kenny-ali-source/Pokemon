import random

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.en_cours = True

    def attaquer(self, attaquant, adversaire):
        degats = random.randint(1, 10)
        adversaire.subir_degats(degats)
        print(f"{attaquant.nom} attaque {adversaire.nom} et inflige {degats} dégâts!")

    def tour_de_combat(self):
        self.attaquer(self.pokemon1, self.pokemon2)
        self.attaquer(self.pokemon2, self.pokemon1)

        if self.pokemon1.est_ko() or self.pokemon2.est_ko():
            self.en_cours = False

    def commencer_combat(self):
        print("Le combat commence!")

        while self.en_cours:
            self.tour_de_combat()

        if self.pokemon1.est_ko():
            print(f"{self.pokemon1.nom} a perdu le combat.")
        elif self.pokemon2.est_ko():
            print(f"{self.pokemon2.nom} a perdu le combat.")
        else:
            print("Match nul.")
