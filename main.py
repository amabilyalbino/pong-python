import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, FONT_SIZE, PADDLE_SPEED, SPEED_INCREMENT_INTERVAL, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_COLOR, BALL_WIDTH
from paddle import Paddle
from ball import Ball
from utils import draw_center_line, draw_text

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)

paused = False  # Definindo a variável paused

def toggle_pause():
    global paused
    paused = not paused

def reset_game():
    global time_since_last_point, left_paddle, right_paddle, ball
    time_since_last_point = 0
    left_paddle = Paddle(80, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2)
    right_paddle = Paddle(SCREEN_WIDTH - 80 - PADDLE_WIDTH, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2)
    ball = Ball(SCREEN_WIDTH // 2 - BALL_WIDTH // 2, SCREEN_HEIGHT // 2 - BALL_WIDTH // 2)

def reset_scores():
    global left_score, right_score
    left_score = 0
    right_score = 0

left_paddle = Paddle(80, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2)
right_paddle = Paddle(SCREEN_WIDTH - 80 - PADDLE_WIDTH, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2)
ball = Ball(SCREEN_WIDTH // 2 - BALL_WIDTH // 2, SCREEN_HEIGHT // 2 - BALL_WIDTH // 2)

left_score = 0
right_score = 0
time_since_last_point = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Press 'P' to toggle pause
                toggle_pause()
            if event.key == pygame.K_r:  # Press 'R' to reset game and scores
                reset_scores()
                reset_game()

    if not paused:
        keys = pygame.key.get_pressed()

        # Move left paddle
        if keys[pygame.K_w] and left_paddle.rect.top > 0:
            left_paddle.rect.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.rect.bottom < SCREEN_HEIGHT:
            left_paddle.rect.y += PADDLE_SPEED

        # Move right paddle
        if keys[pygame.K_UP] and right_paddle.rect.top > 0:
            right_paddle.rect.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.rect.bottom < SCREEN_HEIGHT:
            right_paddle.rect.y += PADDLE_SPEED

        # Move ball
        ball.move()

        # Ball collision with top and bottom
        if ball.rect.top <= 0 or ball.rect.bottom >= SCREEN_HEIGHT:
            ball.speed_y *= -1

        # Ball collision with paddles
        if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(right_paddle.rect):
            ball.speed_x *= -1

        # Ball out of bounds (left and right)
        if ball.rect.left <= 0:
            right_score += 1  # Right player scores
            ball.reset(SCREEN_WIDTH // 2 - BALL_WIDTH // 2, SCREEN_HEIGHT // 2 - BALL_WIDTH // 2)
            time_since_last_point = 0

        if ball.rect.right >= SCREEN_WIDTH:
            left_score += 1  # Left player scores
            ball.reset(SCREEN_WIDTH // 2 - BALL_WIDTH // 2, SCREEN_HEIGHT // 2 - BALL_WIDTH // 2)
            time_since_last_point = 0

        # Increase ball speed if no one has scored for a while
        time_since_last_point += clock.get_time()
        if time_since_last_point >= SPEED_INCREMENT_INTERVAL:
            ball.speed_x *= 1.1
            ball.speed_y *= 1.1
            time_since_last_point = 0

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BG_COLOR)

    # Draw center line
    draw_center_line(screen)

    # Draw paddles
    left_paddle.draw(screen)
    right_paddle.draw(screen)

    # Draw ball
    ball.draw(screen)

    # Render and draw scores
    draw_text(screen, str(left_score), font, PADDLE_COLOR, 540, 50)
    draw_text(screen, str(right_score), font, PADDLE_COLOR, 700, 50)

    if paused:
        draw_text(screen, "PAUSED", font, (255, 255, 255), 540, 310)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
sys.exit()















