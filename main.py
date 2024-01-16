from typing import List

class Combat:
    def __init__(self, pokemonJoueur, pokemonAdversaire):
        self.pokemonJoueur = pokemonJoueur
        self.pokemonAdversaire = pokemonAdversaire

    def getPuissanceAttaqueAdversaire(self, typeAdversaire):
        # Logique pour obtenir la puissance d'attaque de l'adversaire en fonction du type
        # Vous devez implémenter cette logique en fonction de vos règles de jeu
        pass

    def enleverPointsDeVie(self, defenseAdversaire):
        # Logique pour enlever des points de vie en fonction de la défense de l'adversaire
        # Vous devez implémenter cette logique en fonction de vos règles de jeu
        pass

    def determinerVainqueur(self):
        if self.pokemonJoueur.pointsDeVie <= 0:
            return f"{self.pokemonAdversaire.nom} remporte la victoire!"
        elif self.pokemonAdversaire.pointsDeVie <= 0:
            return f"{self.pokemonJoueur.nom} remporte la victoire!"
        else:
            return "Le combat se poursuit."

    def enregistrerDansPokedex(self, pokedex):
        # Logique pour enregistrer le Pokémon rencontré dans le Pokédex
        # Vous devez implémenter cette logique en fonction de vos règles de jeu
        pass
