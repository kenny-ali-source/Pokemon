# jeu.py
import pygame
import os
from personnage import Player
import subprocess

class Screen:
    def __init__(self):
        pygame.init()
        self.screen = None

    def set_mode(self, chemin_image):
        info_ecran = pygame.display.Info()
        self.screen = pygame.display.set_mode((info_ecran.current_w, info_ecran.current_h), pygame.FULLSCREEN)

        pygame.display.set_caption("Mon jeu avec une image PNG")

        image = pygame.image.load(chemin_image)
        image_redimensionnee = pygame.transform.scale(image, (info_ecran.current_w, info_ecran.current_h))

        return self.screen, image_redimensionnee.get_size(), image_redimensionnee

    def get_display(self):
        return self.screen

    def get_size(self):
        return self.screen.get_size()

class Map:
    def __init__(self, ecran: Screen):
        self.ecran = ecran
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(50, 50)
        self.all_sprites.add(self.player)

    def switch_map(self, chemin_image):
        pass

    def update(self, keys):
        self.all_sprites.update(keys)

    def draw(self):
        self.all_sprites.draw(self.ecran.get_display())

    def draw_background(self, image):
        self.ecran.get_display().blit(image, (0, 0))

# Variable pour contrôler le processus du Pokedex
pokedex_process = None

# Initialisez l'écran
instance_ecran = Screen()
screen, background_size, background_image = instance_ecran.set_mode("project_pokemon/map/mapherbe.png")

# Initialisez la carte
carte_jeu = Map(instance_ecran)

# Variable pour contrôler l'affichage du Pokedex
afficher_pokedex = False

# Boucle principale
en_cours = True
clock = pygame.time.Clock()

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if not afficher_pokedex:
                    # Créer un processus pour exécuter la fonction activer_pokedex
                    pokedex_process = subprocess.Popen(["python", "project_pokemon/pokedex.py"])
                    afficher_pokedex = True
                else:
                    # Fermer la fenêtre du Pokedex
                    if pokedex_process and pokedex_process.poll() is None:
                        pokedex_process.terminate()
                        pokedex_process.wait()
                    afficher_pokedex = False

    keys = pygame.key.get_pressed()

    instance_ecran.get_display().fill((0, 0, 0))
    carte_jeu.draw_background(background_image)
    carte_jeu.update(keys)
    carte_jeu.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
