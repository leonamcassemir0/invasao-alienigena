import pygame
import sys


"""
Este código mostrará a sequência numérica correspondete a tecla pressionada
"""


def run_game():
    pygame.init()
    pygame.display.set_mode((500, 500))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key)
                pygame.display.flip()

            if event.type == pygame.QUIT:
                sys.exit()


run_game()
