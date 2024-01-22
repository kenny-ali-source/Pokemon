# personnage.py
import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Chargez toutes les images du sprite dans une liste
        sprite_path = os.path.join("project_pokemon/sprite2.png")
        sprite_sheet = pygame.image.load(sprite_path)

        self.sprite_width = 69
        self.sprite_height = 69
        self.images = []

        for direction in range(4):  # 4 directions (face, gauche, droite, dos)
            direction_images = []
            for frame in range(4):  # Ajoutez le nombre d'images par direction
                frame_x = frame * self.sprite_width + 5  # Ajustez cette valeur pour décaler le personnage un peu vers la droite
                frame_y = direction * self.sprite_height
                try:
                    subsurface = sprite_sheet.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    direction_images.append(subsurface)
                except ValueError as e:
                    print(f"Error in frame {frame}, direction {direction}: {e}")
                    print(f"Frame X: {frame_x}, Frame Y: {frame_y}")

            self.images.append(direction_images)

        # Utilisez la première image comme image par défaut
        self.image = self.images[0][0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Variables pour l'animation
        self.current_frame = 0
        self.animation_speed = 0.15  # Ajustez cette valeur pour régler la vitesse de l'animation
        self.last_update = pygame.time.get_ticks()

    def update(self, keys):
        # Animation du joueur en fonction des touches de direction
        now = pygame.time.get_ticks()
        elapsed_time = now - self.last_update

        if elapsed_time > 1000 * self.animation_speed:  # Vérifiez si le temps écoulé est suffisant pour changer l'image
            self.last_update = now

            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
                self.animate(1)  # Utilisez la fonction d'animation avec le paramètre correspondant
            elif keys[pygame.K_RIGHT]:
                self.rect.x += 5
                self.animate(2)
            elif keys[pygame.K_UP]:
                self.rect.y -= 5
                self.animate(3)
            elif keys[pygame.K_DOWN]:
                self.rect.y += 5
                self.animate(0)
            else:
                # Si aucune touche n'est enfoncée, utilisez l'image par défaut
                self.image = self.images[0][0]

    def animate(self, direction):
        # Fonction d'animation pour changer l'image en fonction de la direction
        self.current_frame = (self.current_frame + 1) % len(self.images[direction])
        self.image = self.images[direction][self.current_frame]

        # Ajustement pour éviter le tremblement en utilisant la même image plusieurs fois
        pygame.time.delay(10)
