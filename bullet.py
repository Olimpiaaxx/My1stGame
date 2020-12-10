import pygame
from graphics import *
from config import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -7

    def update(self):
        self.rect.y += self.speedy
        # kills if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
