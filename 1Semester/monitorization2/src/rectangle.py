from src.utils import window_height, display_surf, WHITE
from src.text import Text
import pygame


class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w + 200
        self.h = h
        self.color = color

    # Draws the rect
    def draw(self, width=False):
        if width:
            self.w = (width * 300) / 100
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        surface = pygame.Surface((500, 500))
        pygame.draw.rect(surface, self.color, self.rect)
        # Draws rect
        surface.fill((255, 000, 000))
        display_surf.blit(surface, (150,50))

