import sys
import pygame


class Imagem():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.screen.blit(self.image, self.rect)


def ceu_azul():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Exercicio 12.1')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 255))
        Imagem(screen)
        pygame.display.flip()


ceu_azul()
