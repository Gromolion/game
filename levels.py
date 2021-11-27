import pygame

from functions import *
from objects import *

WIDTH = 1024
HEIGHT = 700
FPS = 60


def level_1(screen, clock):
    background = pygame.image.load('images/Background/background.jpg')
    all_sprites = pygame.sprite.Group()
    bricks_group = pygame.sprite.Group()
    player_bricks_group = pygame.sprite.Group()

    for i in range(8):
        for j in range(5):
            brick = Brick('brick_green.png', (i + 2) * 90, (j + 1) * 60)
            all_sprites.add(brick)
            bricks_group.add(brick)
            player_bricks_group.add(brick)

    bat = Bat()
    ball = Ball(2, 4)

    all_sprites.add(bat)
    player_bricks_group.add(bat)
    all_sprites.add(ball)

    running = True
    while running:
        clock.tick(FPS)

        screen.blit(background, (0, 0))
        if ball.rect.y > HEIGHT:
            lose(screen)
            return False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_v:
                    if secret():
                        bricks_group.empty()

            if not bricks_group:
                background = pygame.image.load('images/Background/pass.jpg')
                screen.blit(background, (0, 0))
                all_sprites.empty()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    main_menu = pygame.rect.Rect(450, 350, 150, 160)
                    mouse = pygame.mouse.get_pos()
                    if main_menu.collidepoint(*mouse):
                        return True

        if pygame.key.get_pressed()[K_LEFT]:
            bat.move_left()
        elif pygame.key.get_pressed()[K_RIGHT]:
            bat.move_right()

        hits = pygame.sprite.spritecollide(ball, player_bricks_group, False)
        if hits:
            ball.bounce()

        hited_brick = pygame.sprite.spritecollide(ball, bricks_group, False)
        if hited_brick:
            hited_brick[0].hit()

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()


def level_2(screen, clock):
    background = pygame.image.load('images/Background/background_1.jpg')
    all_sprites = pygame.sprite.Group()
    bricks_group = pygame.sprite.Group()
    player_bricks_group = pygame.sprite.Group()

    for i in range(6):
        brick = Brick('brick_pink.png', (i + 5) * 65, 100)
        all_sprites.add(brick)
        bricks_group.add(brick)
        player_bricks_group.add(brick)
    for i in range(8):
        brick = Brick('brick_violet.png', (i + 4) * 65, 150)
        all_sprites.add(brick)
        bricks_group.add(brick)
        player_bricks_group.add(brick)
    for i in range(10):
        brick = Brick('brick_yellow.png', (i + 3) * 65, 200)
        all_sprites.add(brick)
        bricks_group.add(brick)
        player_bricks_group.add(brick)
    for i in range(8):
        brick = Brick('brick_violet.png', (i + 4) * 65, 250)
        all_sprites.add(brick)
        bricks_group.add(brick)
        player_bricks_group.add(brick)
    for i in range(6):
        brick = Brick('brick_pink.png', (i + 5) * 65, 300)
        all_sprites.add(brick)
        bricks_group.add(brick)
        player_bricks_group.add(brick)
    for i in range(4):
        brick = Brick('brick_yellow.png', (i + 6) * 65, 350)
        all_sprites.add(brick)
        bricks_group.add(brick)
        player_bricks_group.add(brick)

    bat = Bat()
    ball = Ball(3, 6)

    all_sprites.add(bat)
    player_bricks_group.add(bat)
    all_sprites.add(ball)

    running = True
    while running:
        clock.tick(FPS)

        screen.blit(background, (0, 0))
        if ball.rect.y > HEIGHT:
            lose(screen)
            return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_v:
                    if secret():
                        bricks_group.empty()

            if not bricks_group:
                background = pygame.image.load('images/Background/pass.jpg')
                screen.blit(background, (0, 0))
                all_sprites.empty()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    main_menu = pygame.rect.Rect(450, 350, 150, 160)
                    mouse = pygame.mouse.get_pos()
                    if main_menu.collidepoint(*mouse):
                        return True

        if pygame.key.get_pressed()[K_LEFT]:
            bat.move_left()
        elif pygame.key.get_pressed()[K_RIGHT]:
            bat.move_right()

        hits = pygame.sprite.spritecollide(ball, player_bricks_group, False)
        if hits:
            ball.bounce()

        hited_brick = pygame.sprite.spritecollide(ball, bricks_group, False)
        if hited_brick:
            hited_brick[0].hit()

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()


def level_3(screen, clock):
    background = pygame.image.load('images/Background/background_1.jpg')
    all_sprites = pygame.sprite.Group()
    bricks_group = pygame.sprite.Group()
    player_bricks_group = pygame.sprite.Group()

    # for i in range()

    bat = Bat()
    ball = Ball(4, 8)

    all_sprites.add(bat)
    player_bricks_group.add(bat)
    all_sprites.add(ball)

    running = True
    while running:
        clock.tick(FPS)

        screen.blit(background, (0, 0))
        if ball.rect.y > HEIGHT:
            lose(screen)
            return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_v:
                    if secret():
                        bricks_group.empty()

            if not bricks_group:
                background = pygame.image.load('images/Background/game_ends.jpg')
                screen.blit(background, (0, 0))
                all_sprites.empty()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return True

        if pygame.key.get_pressed()[K_LEFT]:
            bat.move_left()
        elif pygame.key.get_pressed()[K_RIGHT]:
            bat.move_right()

        hits = pygame.sprite.spritecollide(ball, player_bricks_group, False)
        if hits:
            ball.bounce()

        hited_brick = pygame.sprite.spritecollide(ball, bricks_group, False)
        if hited_brick:
            hited_brick[0].hit()

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()