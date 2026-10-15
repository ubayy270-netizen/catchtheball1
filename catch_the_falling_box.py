import random

import pygame


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Box")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 200, 100)
YELLOW = (255, 210, 0)
BACKGROUND = (20, 20, 40)
RED = (255, 60, 60)

player_width, player_height = 80, 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 8

box_size = 30
box_x = random.randint(0, WIDTH - box_size)
box_y = 0
box_speed = 5

score = 0
game_over = False


def draw_text(text, font_size, color, pos):
    font = pygame.font.SysFont(None, font_size)
    rendered_text = font.render(text, True, color)
    text_rect = rendered_text.get_rect(center=pos)
    screen.blit(rendered_text, text_rect)


def reset_game():
    global player_x, box_x, box_y, box_speed, score, game_over

    player_x = WIDTH // 2 - player_width // 2
    box_x = random.randint(0, WIDTH - box_size)
    box_y = 0
    box_speed = 5
    score = 0
    game_over = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                reset_game()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        player_x = max(0, min(WIDTH - player_width, player_x))

        box_y += box_speed

        player_box = pygame.Rect(player_x, player_y, player_width, player_height)
        falling_box = pygame.Rect(box_x, box_y, box_size, box_size)

        if player_box.colliderect(falling_box):
            score += 1
            box_y = 0
            box_x = random.randint(0, WIDTH - box_size)
            box_speed = min(15, 5 + score // 5)

        if box_y > HEIGHT:
            game_over = True

    screen.fill(BACKGROUND)

    if not game_over:
        pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(screen, YELLOW, (box_x, box_y, box_size, box_size))
        draw_text(f"Score: {score}", 36, WHITE, (80, 30))
    else:
        draw_text("GAME OVER", 64, RED, (WIDTH // 2, HEIGHT // 2 - 40))
        draw_text(f"Final score: {score}", 40, WHITE, (WIDTH // 2, HEIGHT // 2 + 20))
        draw_text("Press R to play again", 28, WHITE, (WIDTH // 2, HEIGHT // 2 + 70))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
