# jeu.py
import pygame
import os
from personnage import Player  # Importez la classe Player depuis le module

# Initialisez la classe Screen
class Screen:
    def __init__(self):
        pygame.init()
        self.screen = None

    def set_mode(self, chemin_image):
        # Créez une fenêtre en mode plein écran avec la meilleure résolution disponible
        info_ecran = pygame.display.Info()
        self.screen = pygame.display.set_mode((info_ecran.current_w, info_ecran.current_h), pygame.FULLSCREEN)

        pygame.display.set_caption("Mon jeu avec une image PNG")

        # Chargez l'image PNG
        image = pygame.image.load(chemin_image)

        # Redimensionnez l'image pour remplir la fenêtre
        image_redimensionnee = pygame.transform.scale(image, (info_ecran.current_w, info_ecran.current_h))

        # Retourne la taille de l'image ajustée, l'image redimensionnée et la surface d'affichage
        return self.screen, image_redimensionnee.get_size(), image_redimensionnee

    def get_display(self):
        return self.screen

    def get_size(self):
        return self.screen.get_size()

# Initialisez la carte
class Map:
    def __init__(self, ecran: Screen):
        self.ecran = ecran
        self.all_sprites = pygame.sprite.Group()  # Groupe pour tous les sprites
        self.player = Player(50, 50)  # Utilisez la classe Player importée
        self.all_sprites.add(self.player)

    def switch_map(self, chemin_image):
        # Pas nécessaire pour une image statique, car il n'y a pas de carte à changer
        pass

    def update(self, keys):
        # Mise à jour de tous les sprites
        self.all_sprites.update(keys)

    def draw(self):
        # Dessinez tous les sprites sur la fenêtre
        self.all_sprites.draw(self.ecran.get_display())

    def draw_background(self, image):
        # Dessinez l'image de fond sur la fenêtre
        self.ecran.get_display().blit(image, (0, 0))

# Initialisez l'écran
instance_ecran = Screen()
screen, background_size, background_image = instance_ecran.set_mode("project_pokemon/map/mapherbe.png")  # Assurez-vous que le chemin est correct

# Initialisez la carte
carte_jeu = Map(instance_ecran)

# Boucle principale
en_cours = True
clock = pygame.time.Clock()

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    keys = pygame.key.get_pressed()
    
    # Effacez l'écran
    instance_ecran.get_display().fill((0, 0, 0))

    # Dessinez l'image de fond
    carte_jeu.draw_background(background_image)

    # Mise à jour de la carte
    carte_jeu.update(keys)

    # Dessinez tous les sprites
    carte_jeu.draw()

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Limitez la vitesse de la boucle
    clock.tick(60)

pygame.quit()

