import pygame
import criafoguete as cf
import jogafoguete as jf


def foguete():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Foguete")
    ship = cf.Ship(screen)

    while True:
        jf.check_events(ship)
        ship.update()
        jf.update_screen(screen, ship)


foguete()
