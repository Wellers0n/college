import pygame
from src.utils import WHITE
class Text():
    def __init__(self, x, y, display, size=20):
        self.x = x
        self.y = y
        self.display = display
        self.font = pygame.font.Font('freesansbold.ttf', size)


    def draw(self, text):
        self.text = text
        result_surf = self.font.render(self.text, True, WHITE)
        rect = result_surf.get_rect()
        rect.topleft = (self.x, self.y)
        self.display.blit(result_surf, rect)
