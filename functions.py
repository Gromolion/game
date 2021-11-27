import pygame
from pygame.locals import *

WIDTH = 1024
HEIGHT = 700
FPS = 60


def lose(screen):
    font_obj = pygame.font.Font('freesansbold.ttf', 100)
    text_surface_obj = font_obj.render('YOU LOSE!', True, (255, 255, 255), (0, 0, 0))
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (500, 400)
    screen.fill((0, 0, 0))
    screen.blit(text_surface_obj, text_rect_obj)
    if pygame.key.get_pressed()[K_SPACE]:
        running = False


def button(img, x, y, screen):
    image = pygame.image.load(img)
    image_rect = image.get_rect()
    image_rect.topright = (x, y)
    screen.blit(image, image_rect)
    return img, image_rect


def secret():
    mods = pygame.key.get_mods()
    if mods & pygame.KMOD_CTRL:
        return True
    else:
        return False
