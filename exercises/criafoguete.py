import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += 1

        if self.moving_left and self.rect.left > 0:
            self.center -= 1

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center2 += 1

        if self.moving_up and self.rect.top > 0:
            self.center2 -= 1

        self.rect.centerx = self.center
        self.rect.centery = self.center2

    def blitme(self):
        self.screen.blit(self.image, self.rect)
