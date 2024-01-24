import os
import json
import random

class Combat:
    def __init__(self):
        self.pokemonJoueur = None
        self.pokemonAdversaire = None

    def charger_donnees(self, fichier):
        chemin_fichier = os.path.join(os.path.dirname(__file__), fichier)
        with open(chemin_fichier, 'r') as file:
            return json.load(file)

    def charger_pokemon(self, nom_pokemon):
        data = self.charger_donnees('attaques-pokemon.json')
        pokemon_info = next((p for p in data if p["nom"] == nom_pokemon), None)

        if pokemon_info:
            return Pokemon(pokemon_info)
        else:
            print(f"Pokemon {nom_pokemon} non trouvé dans le fichier attaques-pokemon.json.")
            return None

    def charger_donnees_attaques_pokemon(self):
        return self.charger_donnees('attaques-pokemon.json')

    def get_puissance_attaque_joueur(self, attaque_joueur, level, nom_pokemon):
        data = self.charger_donnees_attaques_pokemon()

        for pokemon in data:
            if pokemon["nom"] == nom_pokemon:
                attaques_pokemon = pokemon["attaques"]
                for attaque in attaques_pokemon:
                    if attaque["nom"] == attaque_joueur:
                        level = int(level)
                        puissance_attaque_joueur = (attaque["puissance"])
                        return puissance_attaque_joueur
                print(f"Attaque {attaque_joueur} non trouvée pour le Pokémon {nom_pokemon}.")
                return 0

        print(f"Pokémon {nom_pokemon} non trouvé dans le fichier attaques-pokemon.json.")
        return 0

    def random_pokemon_adverse(self):
        data = self.charger_donnees_attaques_pokemon()
        pokemon_adverse_info = random.choice(data)
        return Pokemon(pokemon_adverse_info)

    def enlever_points_de_vie(self, attaque_adverse, pokemon_cible):
        stab = 1.5 if attaque_adverse.type == pokemon_cible.type else 1.0
        modificateur_aleatoire = random.uniform(0.85, 1.00)
        degats = (((2 * attaque_adverse.niveau / 5 + 2) * attaque_adverse.puissance * attaque_adverse.attaque / pokemon_cible.defense) / 50 + 2) * stab * modificateur_aleatoire
        return int(degats)

    def determiner_vainqueur(self):
        if self.pokemonJoueur.pointsDeVie <= 0:
            return f"{self.pokemonAdversaire.nom} remporte la victoire!"
        elif self.pokemonAdversaire.pointsDeVie <= 0:
            return f"{self.pokemonJoueur.nom} remporte la victoire!"
        else:
            return "Le combat se poursuit."

    def enregistrer_dans_pokedex(self, pokedex, pokemon):
        if pokemon.nom not in pokedex:
            pokedex[pokemon.nom] = {
                "type": pokemon.type,
                "defense": pokemon.defense,
                "puissance_attaque": pokemon.puissance_attaque,
                "points_de_vie": pokemon.pointsDeVie
            }
            print(f"{pokemon.nom} a été ajouté à votre Pokédex.")
        else:
            print(f"{pokemon.nom} est déjà dans votre Pokédex.")

class Pokemon:
    def __init__(self, pokemon_info):
        self.nom = pokemon_info["nom"]
        self.type = pokemon_info["type"]
        self.attaques = [Attaque(a) for a in pokemon_info["attaques"]]
        self.pointsDeVie = 100

class Attaque:
    def __init__(self, attaque_info):
        self.nom = attaque_info["nom"]
        self.type = attaque_info["type"]
        self.puissance = attaque_info["puissance"]
        self.precision = attaque_info["precision"]

combat_instance = Combat()


resultat_puissance = combat_instance.get_puissance_attaque_joueur("Damoclès", 90, "Tortank")
pokemon_adverse = combat_instance.random_pokemon_adverse()
print(f"Puissance d'attaque pour l'attaque Damoclès : {resultat_puissance}")

