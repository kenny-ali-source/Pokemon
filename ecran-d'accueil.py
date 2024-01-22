import pygame
import sys
import subprocess
from personnage import Player


pygame.init()
pygame.font.init()

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sound_initialized = False
        self.load_music()
        self.music_playing = False
        self.music_position = 0

    def load_music(self):
        pygame.mixer.music.load("project_pokemon/1hour_pokemon.mp3")
        pygame.mixer.music.set_volume(0.5)
        self.sound_initialized = True

    def play(self):
        if not self.music_playing:
            pygame.mixer.music.play(-1, self.music_position)
            self.music_playing = True

    def stop(self):
        if self.music_playing:
            self.music_position = pygame.mixer.music.get_pos()
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
audio_manager.play()

class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
        self.background = pygame.image.load("project_pokemon/pokémon-ecran-d'accueil.jpg")
        self.background = pygame.transform.scale(self.background, (800, 600))

    def get_display(self):
        return self.screen

# Initialisez la classe Screen
instance_ecran = Screen()

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

volume_bar_width = 200
volume_bar_height = 20
volume_bar_x = 300
volume_bar_y = 200
volume_bar_color = (0, 255, 0)
volume_bar_value = audio_manager.get_volume()

def launch_game():
    try:
        with open("project_pokemon/jeu.py", "r") as jeu_file:
            jeu_code = jeu_file.read()
            exec(jeu_code)
    except FileNotFoundError:
        print("Le fichier jeu.py n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur lors de l'exécution de jeu.py : {e}")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            fullscreen = not fullscreen
            if fullscreen:
                instance_ecran.get_display().set_mode((800, 600), pygame.FULLSCREEN)
            else:
                instance_ecran.get_display().set_mode((800, 600))
            pygame.display.flip()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 350 <= event.pos[0] <= 500 and 350 <= event.pos[1] <= 380:
                running = False
            elif 350 <= event.pos[0] <= 500 and 250 <= event.pos[1] <= 280:
                # Lorsque "Continuer le jeu" est cliqué, lancez le script de jeu.py
                launch_game()
                running = False  # Arrêtez le script d'écran d'accueil après le lancement du jeu.py
            elif 350 <= event.pos[0] <= 500 and 300 <= event.pos[1] <= 330:
                show_options_menu = True
                if not options_menu_entered:
                    audio_manager.reset()
                    options_menu_entered = True
            elif 350 <= event.pos[0] <= 500 and 200 <= event.pos[1] <= 230:
                # Lorsque "Nouvelle partie" est cliqué, lancez le script de jeu.py
                launch_game()
                running = False  # Arrêtez le script d'écran d'accueil après le lancement du jeu.py

    instance_ecran.get_display().blit(instance_ecran.background, (0, 0))

    if not show_options_menu:
        instance_ecran.get_display().blit(text_new_game, (350, 200))
        instance_ecran.get_display().blit(text_continue_game, (350, 250))
        instance_ecran.get_display().blit(text_options, (350, 300))
        instance_ecran.get_display().blit(text_quit_game, (350, 350))
    else:
        instance_ecran.get_display().blit(text_volume, (200, 200))
        pygame.draw.rect(instance_ecran.get_display(), (255, 255, 255), (volume_bar_x, volume_bar_y, volume_bar_width, volume_bar_height))
        pygame.draw.rect(instance_ecran.get_display(), volume_bar_color, (volume_bar_x, volume_bar_y, volume_bar_width * volume_bar_value, volume_bar_height))
        instance_ecran.get_display().blit(text_back, (200, 350))

    pygame.display.flip()

pygame.quit()
sys.exit()
