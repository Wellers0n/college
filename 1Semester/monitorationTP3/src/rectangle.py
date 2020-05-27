import pygame
from src.utils import WHITE


class Rectangle():
    def __init__(self, x, y, width, height, display, color=WHITE):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.display = display
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def getRect(self):
        return self.rect

    def getDisplay(self):
        return self.display

    def draw(self):
        pygame.draw.rect(self.display, self.color, self.rect)

    def update(self, value=0):
        self.width = value
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
