import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alienpug import AlienPug

class AlienAttack:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # FULLSCREEN
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Вороги напали!")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alienpug = pygame.sprite.Group()
        self._create_flot()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_alienpug()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_alienpug(self, alienpug_number, row_num):
        alien = AlienPug(self)
        alienpug_width, alienpug_height = alien.rect.size
        alien.x = alienpug_width + 2 * alienpug_width * alienpug_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
        self.alienpug.add(alien)

    def _check_flot_edges(self):
        for alien in self.alienpug.sprites():
            if alien.check_edge():
                self.change_flot_direction()
                break

    def _create_flot(self):
        alienpug = AlienPug(self)
        alienpug_width, alienpug_height = alienpug.rect.size
        alienpug_width = alienpug.rect.x
        avialable_space_x = self.settings.screen_width - (alienpug_width * 2)
        avialable_alienpug = avialable_space_x // (alienpug_width * 2)
        ship_height = self.ship.rect.height
        avialable_space_y = (self.settings.screen_height - (3 * alienpug_height) - ship_height)
        num_rows = avialable_space_y // (2 * alienpug_height)
        for row_num in range(num_rows):
            for alien_num_in_space in range(avialable_alienpug):
                self._create_alienpug(alien_num_in_space, row_num)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.biltme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.alienpug.draw(self.screen)
        pygame.display.flip()

    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullets = Bullet(self)
            self.bullets.add(new_bullets)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_alienpug(self):
        self._check_flot_edges()
        self.alienpug.update()

    def change_flot_direction(self):
        for alien in self.alienpug.sprites():
            alien.rect.y += self.settings.flot_drop_speed
        self.settings.flot_direction *= -1


if __name__ == '__main__':
    aa = AlienAttack()
    aa.run_game()
