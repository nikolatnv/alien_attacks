import pygame


class Ship():
    def __init__(self, aa_game):
        self.screen = aa_game.screen
        self.screen_rect = aa_game.screen.get_rect()
        self.img_ship = pygame.image.load('images/ship100.bmp').convert()
        self.img_ship.set_colorkey((255, 255, 255))
        self.rect = self.img_ship.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def biltme(self):
        self.screen.blit(self.img_ship, self.rect)

