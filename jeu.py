import pygame
import os
from personnage import Player
import subprocess

# Classe représentant l'écran du jeu
class Screen:
    def __init__(self):
        pygame.init()
        self.screen = None

    def set_mode(self, chemin_image):
        # Initialisation de la fenêtre en mode plein écran avec une image de fond
        info_ecran = pygame.display.Info()
        self.screen = pygame.display.set_mode((info_ecran.current_w, info_ecran.current_h), pygame.FULLSCREEN)
        pygame.display.set_caption("Mon jeu avec une image PNG")

        # Chargement et redimensionnement de l'image de fond
        image = pygame.image.load(chemin_image)
        image_redimensionnee = pygame.transform.scale(image, (info_ecran.current_w, info_ecran.current_h))

        return self.screen, image_redimensionnee.get_size(), image_redimensionnee

    def get_display(self):
        return self.screen

    def get_size(self):
        return self.screen.get_size()

# Classe représentant la carte du jeu
class Map:
    def __init__(self, ecran: Screen):
        self.ecran = ecran
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(50, 50)
        self.all_sprites.add(self.player)

    def switch_map(self, chemin_image):
        # Fonction pour changer la carte du jeu (non implémentée dans ce code)
        pass

    def update(self, keys):
        # Mettre à jour tous les sprites sur la carte
        self.all_sprites.update(keys)

    def draw(self):
        # Dessiner tous les sprites sur la carte
        self.all_sprites.draw(self.ecran.get_display())

    def draw_background(self, image):
        # Dessiner l'image de fond
        self.ecran.get_display().blit(image, (0, 0))

# Variable pour contrôler le processus du Pokedex
pokedex_process = None

# Initialisation de l'écran
instance_ecran = Screen()
screen, background_size, background_image = instance_ecran.set_mode("project_pokemon/map/mapherbe.png")

# Initialisation de la carte
carte_jeu = Map(instance_ecran)

# Variable pour contrôler l'affichage du Pokedex
afficher_pokedex = False

# Boucle principale du jeu
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

    # Effacer l'écran avec une couleur noire
    instance_ecran.get_display().fill((0, 0, 0))

    # Dessiner l'arrière-plan de la carte
    carte_jeu.draw_background(background_image)

    # Mettre à jour et dessiner la carte
    carte_jeu.update(keys)
    carte_jeu.draw()

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter la fréquence d'images à 60 FPS
    clock.tick(60)

# Quitter Pygame
pygame.quit()
