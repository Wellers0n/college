from src.utils import window_width, WHITE, display_surf
import pygame


class Text():
    def __init__(self, x=25, y=25, font_size=20):
        self.x = x
        self.y = y

        self.font = pygame.font.Font('freesansbold.ttf', font_size)

    # Displays the current score on the screen
    def display(self, text):
        self.text = text
        result_surf = self.font.render(self.text, True, WHITE)
        rect = result_surf.get_rect()
        rect.topleft = (self.x, self.y)
        display_surf.blit(result_surf, rect)
