import pygame
from pygame.sprite import Sprite
from settings import Settings
import time


class Target(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.tar_screen = ai_game.screen
        self.tar_settings = ai_game.settings
        self.tar_screen_rect = ai_game.screen.get_rect()
        self.image = pygame.Surface(
            (self.tar_settings.tar_width, self.tar_settings.tar_height))
        self.image.fill(self.tar_settings.tar_color)
        self.rect = self.image.get_rect()
        self.rect.midtop = self.tar_screen_rect.midtop
        self.x = float(self.rect.x)
        self.tar_moving_right = True
        self.tar_moving_left = True

    def tar_update1(self):
        if self.tar_moving_right and self.rect.right <= self.tar_screen_rect.right:
            if self.rect.right == self.tar_screen_rect.right:
                self.x -= self.tar_settings.tar_speed
            else:
                self.x += self.tar_settings.tar_speed
# elif self.rect.left > self.tar_screen_rect.left:
# self.x -= self.tar_settings.tar_speed
# self.rect.x = self.x

    def tar_update2(self):
        if self.rect.right <= self.tar_screen_rect.right:
            if self.rect.right == self.tar_screen_rect.right:
                self.x -= self.tar_settings.tar_speed
            else:
                self.x += self.tar_settings.tar_speed
        elif self.rect.left >= self.tar_screen_rect.left:
            if self.rect.left == self.tar_screen_rect.left:
                self.x += self.tar_settings.tar_speed
            else:
                self.x -= self.tar_settings.tar_speed

    def tar_update3(self):
        if self.rect.right <= self.tar_screen_rect.right:
            if self.rect.right < self.tar_screen_rect.right:
                self.x += self.tar_settings.tar_speed
            else:
                self.x -= self.tar_settings.tar_speed
        elif self.rect.left >= self.tar_screen_rect.left:
            if self.rect.left > self.tar_screen_rect.left:
                self.x -= self.tar_settings.tar_speed
            else:
                self.x += self.tar_settings.tar_speed

    def _check_tar_edges(self):
        if self.rect.right >= self.tar_screen_rect.right or self.rect.left <= 0:
            return True

    def tar_update(self):
        self.x += float(self.tar_settings.tar_speed *
                        self.tar_settings.tar_direction)

        self.rect.x = self.x
        '''if self.rect.right >= self.tar_screen_rect.right or self.rect.left <= 0:
            self.time = time.perf_counter()
            if self.tar_settings.tar_direction == 1:
                self.i = self.time
            if self.tar_settings.tar_direction != 1:
                b = self.time'''
        # print(f"{self.time} ",
        # (-1*(self.tar_settings.screen_width*0.000264)/(self.i-b)))
        # (self.tar_screen_rect.left + self.tar_screen_rect.right)
        # self.moving_speed = self.tar_settings.screen_width/self.time
        # print(f"{self.moving_speed} km/h")
