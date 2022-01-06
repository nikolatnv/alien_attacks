import pygame


class Ship():
    def __init__(self, aa_game):
        self.screen = aa_game.screen
        self.settings = aa_game.settings
        self.screen_rect = aa_game.screen.get_rect()
        self.img_ship = pygame.image.load('images/ship100.bmp').convert()
        self.img_ship.set_colorkey((255, 255, 255))
        self.rect = self.img_ship.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def biltme(self):
        self.screen.blit(self.img_ship, self.rect)

