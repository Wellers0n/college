from src import helpers
import pygame, sys
from pygame.locals import *
from src.utils import fps, fps_clock, display_surf
from src.monitoring import Monitoring


class main():
    pygame.init()
    pygame.display.set_caption('Monitoring')
    monitoring = Monitoring()

    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        display_surf.fill((0, 0, 0))
        monitoring.update()
        pygame.display.update()
        fps_clock.tick(fps)


if __name__ == '__main__':
    main()
