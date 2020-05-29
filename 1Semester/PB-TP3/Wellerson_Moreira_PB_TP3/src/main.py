import pygame, sys
from pygame.locals import *
from src.utils import fps, fps_clock, display_surf
from src.rectangle import Rectangle
from src.monitoring import Monitoring


class main():
    pygame.init()
    count = 0

    monitoring = Monitoring()
    title = ['CPU', 'Memory', 'Disk', 'IP', 'Infos']
    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if count != 0:
                        count -= 1
                    count
                if event.key == pygame.K_RIGHT:
                    if count != 3 and count <= 3:
                        count += 1
                    count
                if event.key == pygame.K_SPACE:
                    count = 4

        display_surf.fill((0, 0, 255))
        monitoring.update(count)
        pygame.display.set_caption(title[count])

        pygame.display.update()
        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == '__main__':
    main()
