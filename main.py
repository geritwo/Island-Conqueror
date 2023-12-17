import pygame

import modules.map

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE

# define colours
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)

MAP_DATA = modules.map.map_terrain


# Class to render map-data to a surface image
class TileMap:
    TILE_SIZE = WINDOW_HEIGHT/8  # size of map elements

    def __init__(self, map_data):
        """ Load in the map data, generating a tiled-image """
        self.map_data = map_data
        map_width = len(self.map_data[0]) - 1
        map_length = len(self.map_data)
        # Create an image to hold all the map tiles
        self.image = pygame.Surface((map_width * TileMap.TILE_SIZE, map_length * TileMap.TILE_SIZE))
        self.rect = self.image.get_rect()
        # iterate over the map data, drawing the tiles to the surface
        y_cursor = 0
        for map_line in map_data:  # for each row of tiles
            x_cursor = 0
            for map_symbol in map_line:  # for each tile in the row
                tile_rect = pygame.Rect(x_cursor, y_cursor, TileMap.TILE_SIZE, TileMap.TILE_SIZE)
                if map_symbol == 0:
                    pygame.draw.rect(self.image, BLUE, tile_rect)
                elif map_symbol == 1:
                    pygame.draw.rect(self.image, GREEN, tile_rect)
                else:
                    pass  # ignore \n etc.
                x_cursor += TileMap.TILE_SIZE
            y_cursor += TileMap.TILE_SIZE

    def draw(self, surface, position=(0, 0)):
        """ Draw the map onto the given surface """
        self.rect.topleft = position
        surface.blit(self.image, self.rect)


# Initialisation
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), SURFACE)
pygame.display.set_caption("Render Tile Map")

# Load the map
tile_map = TileMap(MAP_DATA)

# Main Loop
clock = pygame.time.Clock()
done = False
while not done:

    # Handle user-input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Update the window, but not more than 60fps
    window.fill(BLACK)

    # Draw the map to the window
    tile_map.draw(window)

    pygame.display.flip()
    clock.tick_busy_loop(60)

pygame.quit()
