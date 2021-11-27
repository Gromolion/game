import os
import random
import re

import pygame

WIDTH = 1024
HEIGHT = 700


class Bat(pygame.sprite.Sprite):
    DIR = 'images/Bats'

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(Bat.DIR, random.choice(os.listdir(Bat.DIR))))
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 40
        self.rect.left = (WIDTH - self.image.get_width()) / 2

    def move_left(self):
        if self.rect.left > 0:
            self.rect.move_ip(-8, 0)

    def move_right(self):
        if self.rect.right < WIDTH:
            self.rect.move_ip(8, 0)


class Ball(pygame.sprite.Sprite):
    DIR = 'images/Balls'

    def __init__(self, speed_x, speed_y):
        r = random.randint(1, 2)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(Ball.DIR, random.choice(os.listdir(Ball.DIR))))
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 26 * 3
        self.rect.left = WIDTH / 2
        self.speed_x = speed_x if r == 1 else -speed_x
        self.speed_y = speed_y
        self.c_speed_x = self.speed_x
        self.c_speed_y = speed_y

    def update(self):
        self.rect = self.rect.move(self.speed_x, self.speed_y)
        if self.rect.x > WIDTH - self.image.get_width() or self.rect.x < 0:
            self.speed_x *= -1
        if self.rect.y < 0:
            self.speed_y *= -1

    def bounce(self):
        self.speed_y = -self.speed_y
        # if hits_rect.x <= self.rect.x and self.rect.x <= hits_rect.x - 10:
        #     self.speed_x = -abs(self.c_speed_x)
        #     self.speed_y = -self.c_speed_y
        # elif hits_rect.x - 10 < self.rect.x and hits_rect.x + 10 > self.rect.x:
        #     self.speed_x = 0
        #     self.speed_y = -self.speed_y
        # elif hits_rect.centerx + 10 <= self.rect.left:
        #     self.speed_x = abs(self.c_speed_x)
        #     self.speed_y = -self.speed_y


class Brick(pygame.sprite.Sprite):
    DIR = 'images/Bricks'
    DIR_cracked = 'images/Bricks_cracked'

    def __init__(self, image, x, y, breakable=True):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(Brick.DIR, image))
        self.type = re.match(r'(.*)(.png)', image).group(1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.breakable = breakable
        self.cracked = False

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def hit(self):
        if not self.cracked and self.breakable:
            self.type += '_cracked.png'
            self.image = pygame.image.load(os.path.join(Brick.DIR_cracked, self.type))
            self.cracked = True
        else:
            self.kill()
