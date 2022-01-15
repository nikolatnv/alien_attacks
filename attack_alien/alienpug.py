import pygame
from pygame.sprite import Sprite


class AlienPug(Sprite):
    def __init__(self, aa_game):
        super().__init__()
        self.screen = aa_game.screen
        self.image = pygame.image.load('images/pugov.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.settings = aa_game.settings

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alienpug_speed * self.settings.flot_direction)
        self.rect.x = self.x