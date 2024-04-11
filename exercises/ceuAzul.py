import sys
import pygame


def ceu_azul():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Exercicio 12.1')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 255))
        pygame.display.flip()


ceu_azul()
