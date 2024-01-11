import pygame
import sys
from jeu import Jeu
pygame.init()
pygame.font.init()  # Initialisation du module de police

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sound_initialized = False
        self.load_music()
        self.music_playing = False  # Initialisation de la variable music_playing
        self.music_position = 0  # Nouvelle variable pour stocker la position de lecture

    def load_music(self):
        pygame.mixer.music.load("project_pokemon/1hour_pokemon.mp3")
        pygame.mixer.music.set_volume(0.5)
        self.sound_initialized = True

    def play(self):
        if not self.music_playing:
            pygame.mixer.music.play(-1, self.music_position)  # Reprendre à la position sauvegardée
            self.music_playing = True

    def stop(self):
        if self.music_playing:
            self.music_position = pygame.mixer.music.get_pos()  # Sauvegarder la position actuelle
            pygame.mixer.music.stop()
            self.music_playing = False

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def get_volume(self):
        return pygame.mixer.music.get_volume()

    def reset(self):
        if not self.sound_initialized:
            self.load_music()

audio_manager = AudioManager()
audio_manager.play()  # Lancer le son au démarrage

screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
# Charger l'image de fond avec la nouvelle résolution
background = pygame.image.load("project_pokemon/pokémon-ecran-d'accueil.jpg")
background = pygame.transform.scale(background, (800, 600))  # Adapter à la taille de la fenêtre

font = pygame.font.Font(None, 36)
text_new_game = font.render("Nouvelle partie", True, (255, 255, 255))
text_continue_game = font.render("Continuer partie", True, (255, 255, 255))
text_options = font.render("Options", True, (255, 255, 255))
text_quit_game = font.render("Quitter le jeu", True, (255, 255, 255))

fullscreen = True
show_options_menu = False
options_menu_entered = False

options_menu_font = pygame.font.Font(None, 30)
text_volume = options_menu_font.render("Volume", True, (255, 255, 255))
text_back = options_menu_font.render("Retour", True, (255, 255, 255))
back_button_rect = text_back.get_rect(topleft=(200, 350))

# Ajout d'une barre de volume
volume_bar_width = 200
volume_bar_height = 20
volume_bar_x = 300
volume_bar_y = 200
volume_bar_color = (0, 255, 0)
volume_bar_value = audio_manager.get_volume()

running = True
# ... (votre code précédent)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
            else:
                screen = pygame.display.set_mode((800, 600))
            pygame.display.flip()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 350 <= event.pos[0] <= 500 and 350 <= event.pos[1] <= 380:
                running = False
            elif 350 <= event.pos[0] <= 500 and 250 <= event.pos[1] <= 280:
                # L'utilisateur a cliqué sur "Nouvelle partie"
                jeu = Jeu()
                jeu.start_game()
            elif 350 <= event.pos[0] <= 500 and 300 <= event.pos[1] <= 330:
                # L'utilisateur a cliqué sur "Options"
                show_options_menu = True
                if not options_menu_entered:
                    audio_manager.reset()  # Réinitialiser le son seulement la première fois
                    options_menu_entered = True
            elif show_options_menu and back_button_rect.collidepoint(event.pos):
                # L'utilisateur a cliqué sur le bouton "Retour"
                show_options_menu = False
                if audio_manager.music_playing:  # Vérifiez si la musique est en cours de lecture
                    audio_manager.play()  # Reprendre la musique seulement si elle était en cours de lecture
            elif show_options_menu and volume_bar_x <= event.pos[0] <= volume_bar_x + volume_bar_width \
                    and volume_bar_y <= event.pos[1] <= volume_bar_y + volume_bar_height:
                # L'utilisateur a cliqué sur la barre de volume
                volume_bar_value = (event.pos[0] - volume_bar_x) / volume_bar_width
                audio_manager.set_volume(volume_bar_value)



    screen.blit(background, (0, 0))

    if not show_options_menu:
        screen.blit(text_new_game, (350, 200))
        screen.blit(text_continue_game, (350, 250))
        screen.blit(text_options, (350, 300))
        screen.blit(text_quit_game, (350, 350))
    else:
        # Afficher le menu des options
        screen.blit(text_volume, (200, 200))
        pygame.draw.rect(screen, (255, 255, 255), (volume_bar_x, volume_bar_y, volume_bar_width, volume_bar_height))
        pygame.draw.rect(screen, volume_bar_color, (volume_bar_x, volume_bar_y, volume_bar_width * volume_bar_value, volume_bar_height))
        screen.blit(text_back, (200, 350))

    pygame.display.flip()

pygame.quit()
sys.exit()
