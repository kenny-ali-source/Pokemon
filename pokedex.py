#pokedex.py
import os
import json
import tkinter as tk
from tkinter import messagebox

# Classe représentant l'interface graphique du Pokedex
class PokedexGUI:
    def __init__(self, master):
        self.master = master
        master.title("Pokedex")

        # Configure la fenêtre en plein écran
        master.attributes('-fullscreen', True)

        # Initialise l'objet Pokedex
        self.pokedex = Pokedex()

        # Configure la couleur de fond
        master.configure(bg='black')

        # Crée un label et un champ de saisie pour le nom du Pokémon
        self.label = tk.Label(master, text="Nom du Pokémon:", fg='white', bg='black')  # Texte en blanc sur fond noir
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        # Crée un bouton pour enregistrer le Pokémon
        self.button_enregistrer = tk.Button(master, text="Enregistrer Pokémon", command=self.enregistrer_pokemon, fg='black', bg='white')  # Texte noir sur fond blanc
        self.button_enregistrer.pack()

        # Crée un bouton pour quitter le Pokedex
        self.button_quitter = tk.Button(master, text="Quitter", command=self.quitter_pokedex, fg='black', bg='white')  # Texte noir sur fond blanc
        self.button_quitter.pack()

    def enregistrer_pokemon(self):
        nom_pokemon = self.entry.get()

        if nom_pokemon:
            nouveau_pokemon = {"nom": nom_pokemon, "type": "Inconnu", "niveau": 1}
            if self.pokedex.enregistrer_pokemon(nouveau_pokemon):
                messagebox.showinfo("Succès", "Nouveau Pokémon enregistré dans votre Pokedex.")
            else:
                messagebox.showinfo("Erreur", "Ce Pokémon est déjà dans votre Pokedex.")
        else:
            messagebox.showinfo("Erreur", "Veuillez saisir un nom de Pokémon.")

    def quitter_pokedex(self):
        self.master.destroy()

# Classe représentant le Pokedex
class Pokedex:
    def __init__(self, save_file="fichier/pokedex.json"):
        self.pokemon_list = []
        self.total_pokemon_count = 0
        self.save_file = save_file

        directory = os.path.dirname(self.save_file)
        if not os.path.exists(directory):
            os.makedirs(directory)

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

# Crée une instance de la classe Tkinter et lance l'application
root = tk.Tk()
app = PokedexGUI(root)
root.mainloop()
