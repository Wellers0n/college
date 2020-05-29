import pygame
from src.utils import display_surf, BLUE


class Surface():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = pygame.Surface((self.width, self.height))

    def getSurface(self):
        return self.surface

    def draw(self, color=BLUE):
        display_surf.blit(self.surface, (self.x, self.y))
        self.surface.fill(color)
