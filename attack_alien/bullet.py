import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, aa_game):
        super.__init__()
        self.screen = aa_game.screen
        self.settings = aa_game.settings
        self.collor = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = aa_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self,):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.collor, self.rect)
