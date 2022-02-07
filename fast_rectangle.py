import sys
import pygame
from pygame.constants import FULLSCREEN, K_LEFT, K_RIGHT, KEYDOWN
from major_rec import Player
from Second_rect import Target
from settings import Settings
from bullet import Bullet


class Rectangle:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # pygame.FULLSCREEN
        self.settings.screen_height = self.screen.get_rect().height  # update Object settings
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Sniper!")  # Crazy rectangle
        self.rectangles = pygame.sprite.Group()
        self.targets = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = Player(self)
        self.rectangles.add(self.player)
        self.target = Target(self)
        self.targets.add(self.target)

    def run_game(self):
        while True:
            self._check_events()
            self.target.tar_update()
            self.player.rec_update()
            self.update_bullet()
            self._check_target_edges()
            self.update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False

    def _check_target_edges(self):
        if self.target._check_tar_edges():
            self._change_target_direction()

    def _change_target_direction(self):
        self.settings.tar_direction *= -1

    def _fire_bullet(self):
        if len(self.bullets) <= self.settings.bullet_alowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.check_target_collision()

    def create_target(self):
        target = Target(self)
        self.targets.add(target)

    def check_target_collision(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.targets, True, True)
        if not self.targets:
            self.bullets.empty()
            self.targets.empty()
            self.create_target()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rectangles.draw(self.screen)
        self.targets.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    rec = Rectangle()
    rec.run_game()
