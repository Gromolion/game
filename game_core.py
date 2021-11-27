import pygame.mouse

from levels import *

WIDTH = 1024
HEIGHT = 700
FPS = 60
main_background = pygame.image.load('images/Background/main_background.jpg')
logo = pygame.image.load('images/logo.png')

pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

screen.blit(main_background, (0, 0))
screen.blit(logo, (WIDTH / 3.5, 30))
play = button('images/play.png', 600, 300, screen)
quit = button('images/quit.png', 600, 500, screen)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
            if play[1].collidepoint(*mouse):
                play = button('images/play_focused.png', 600, 300, screen)
            else:
                play = button('images/play.png', 600, 300, screen)

            if quit[1].collidepoint(*mouse):
                quit = button('images/quit_focused.png', 600, 500, screen)
            else:
                quit = button('images/quit.png', 600, 500, screen)

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse = pygame.mouse.get_pos()
            if play[1].collidepoint(*mouse):
                running = False
            if quit[1].collidepoint(*mouse):
                running = False
                pygame.quit()
    pygame.display.flip()

_pass = False
while not _pass:
    _pass = level_1(screen, clock)
_pass = False
while not _pass:
    _pass = level_2(screen, clock)
_pass = False
while not _pass:
    _pass = level_3(screen, clock)
pygame.quit()


