import pygame

# Set up the colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the width and height
window_width = 800
window_height = 600

# Set up the display with width and height
display_surf = pygame.display.set_mode((window_width, window_height))

fps_clock = pygame.time.Clock()
fps = 60  # Number of frames per second