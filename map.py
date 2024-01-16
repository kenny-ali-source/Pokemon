import pygame
import pytmx

class Screen:
    def __init__(self):
        pygame.init()
        self.screen = None

    def set_mode(self, map_path):
        # Créez une fenêtre en mode plein écran avec la meilleure résolution disponible
        screen_info = pygame.display.Info()
        self.screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)

        pygame.display.set_caption("Mon jeu avec une carte Tiled")

        tmx_data = pytmx.TiledMap(map_path)
        tile_width = tmx_data.tilewidth
        tile_height = tmx_data.tileheight
        map_width = tmx_data.width * tile_width
        map_height = tmx_data.height * tile_height

        # Ajustez le rendu de votre carte en fonction de la résolution actuelle de l'écran
        screen_width, screen_height = pygame.display.get_surface().get_size()

        # Créez une surface pour la carte
        map_surface = pygame.Surface((map_width, map_height), pygame.SRCALPHA)

        # Dessinez chaque layer de la carte sur la surface
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile_images = tmx_data.get_tile_image_by_gid(gid)
                    if tile_images:
                        image = pygame.image.load(tile_images[0])  # Chargez l'image avec pygame
                        map_surface.blit(image, (x * tile_width, y * tile_height))

        # Redimensionnez la carte pour remplir la fenêtre
        scaled_map_surface = pygame.transform.scale(map_surface, (screen_width, screen_height))

        # Affichez la nouvelle surface sur la fenêtre
        self.screen.blit(scaled_map_surface, (0, 0))
        pygame.display.flip()

        return self.screen, scaled_map_surface.get_size()  # Retourne la taille de la carte ajustée

    def get_display(self):
        return self.screen

    def get_size(self):
        return self.screen.get_size()

class Map:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.tmx_data = None

    def switch_map(self, map_path):
        self.tmx_data = pytmx.load_pygame(map_path)

    def update(self):
        pass  # Ajoutez ici les mises à jour de la carte si nécessaire

# Initialisation de l'écran
screen_instance = Screen()
screen_instance.set_mode("project_pokemon/map/mapherbe.tmx")

# Initialisation de la carte
game_map = Map(screen_instance)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour de la carte
    game_map.update()

    # Mettez à jour l'affichage
    pygame.display.flip()

pygame.quit()
