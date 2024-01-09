import json
class Pokedex:
    def __init__(self, save_file="C:/ken/Pokemon/fichier/pokedex.json"):
        self.pokemon_list = []
        self.total_pokemon_count = 0
        self.save_file = "pokedex.json"

        try:
            with open(self.save_file, "r") as file:
                self.pokemon_list = json.load(file)
                self.total_pokemon_count = len(self.pokemon_list)
        except FileNotFoundError:
            with open(self.save_file, "w") as file:
                json.dump([], file)

    def enregistrer_pokemon(self, nouveau_pokemon):
        for pokemon_existant in self.pokemon_list:
            if pokemon_existant["nom"] == nouveau_pokemon["nom"]:
                print("Ce Pokémon est déjà dans votre Pokedex.")
                return False

        self.pokemon_list.append(nouveau_pokemon)
        self.total_pokemon_count += 1
        print("Nouveau Pokémon enregistré dans votre Pokedex.")
        self.sauvegarde_pokemon()  
        return True

    def sauvegarde_pokemon(self):
        with open(self.save_file, "w") as file:
            json.dump(self.pokemon_list, file)



