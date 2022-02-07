import pygame
from pygame.sprite import Sprite
from settings import Settings


class Player(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.Surface(
            (self.settings.rec_width, self.settings.rec_height))
        self.image.fill(self.settings.rec_color)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def rec_update(self):
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.rec_speed
        elif self.moving_left and self.rect.left >= self.screen_rect.left:
            self.x -= self.settings.rec_speed

        self.rect.x = self.x
