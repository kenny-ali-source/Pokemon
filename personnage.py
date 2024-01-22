# personnage.py
import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Chargez l'image du sprite
        sprite_path = os.path.join("project_pokemon/sprite2.png")
        sprite_sheet = pygame.image.load(sprite_path)

        # Sélectionnez la partie du sprite que vous souhaitez afficher
        sprite_width = 62  # Largeur de la partie du sprite à afficher
        sprite_height = 62  # Hauteur de la partie du sprite à afficher
        sprite_rect = pygame.Rect(0, 0, sprite_width, sprite_height)
        self.image = sprite_sheet.subsurface(sprite_rect)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, keys):
        # Déplacez le joueur en fonction des touches de direction
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
