import pygame, sys
from pygame.locals import *
from src.game import Game
from src.utils import fps, fps_clock


# Main function
def main():
    pygame.init()
    pygame.display.set_caption('Pong')
    pygame.mouse.set_visible(0)  # make cursor invisible

    game = Game(speed=4)

    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # mouse movement commands
            elif event.type == MOUSEMOTION:
                game.paddles['user'].move(event.pos)

        game.update()
        pygame.display.update()
        fps_clock.tick(fps)


if __name__ == '__main__':
    main()
