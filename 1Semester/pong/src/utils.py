import pygame

# Set up the colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the width and height
window_width = 400
window_height = 300

# Set up the display with width and height
display_surf = pygame.display.set_mode((window_width, window_height))

fps_clock = pygame.time.Clock()
fps = 60  # Number of frames per second