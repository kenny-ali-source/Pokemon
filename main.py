from typing import List
import json
import random
class Combat:
    def __init__(self, pokemonJoueur, pokemonAdversaire):
        self.pokemonJoueur = pokemonJoueur
        self.pokemonAdversaire = pokemonAdversaire

    def getPuissanceAttaqueAdversaire(self, typeAdversaire,level):
        chemin_fichier = "attaques-pokemon.json"
        with open(chemin_fichier, 'r') as fichier:
            data = json.load(fichier)
        print(data)
        pass
        if typeAdversaire in data:
            level = int(level)
            puissance_attaque_adversaire = ((2*level)/5+2)
            return puissance_attaque_adversaire
        else:
            print(f"Pokémon {typeAdversaire} non trouvé dans le fichier types.json.")
            return 0  
    def enleverPointsDeVie(self, defenseAdversaire,niveau_lanceur, puissance_attaque, attaque_lanceur, defense_cible, type_attaque_lanceur, type_cible):
            stab = 1.5 if type_attaque_lanceur == type_cible else 1.0
            modificateur_type = 1.0 
            modificateur_aleatoire = random.uniform(0.85, 1.00)
            degats = (((2 * niveau_lanceur / 5 + 2) * puissance_attaque * attaque_lanceur / defense_cible) / 50 + 2) * stab * modificateur_type * modificateur_aleatoire
            return int(degats) 
        

    def determinerVainqueur(self):
        if self.pokemonJoueur.pointsDeVie <= 0:
            return f"{self.pokemonAdversaire.nom} remporte la victoire!"
        elif self.pokemonAdversaire.pointsDeVie <= 0:
            return f"{self.pokemonJoueur.nom} remporte la victoire!"
        else:
            return "Le combat se poursuit."

    def enregistrerDansPokedex(self, pokedex):
       
        pass
combat_instance = Combat('Pikachu','Raichu')
resultat_puissance = combat_instance.getPuissanceAttaqueAdversaire("Pikachu", 50)
print(f"Puissance d'attaque: {resultat_puissance}")