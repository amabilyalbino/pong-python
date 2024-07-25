# ball.py

import pygame
from settings import BALL_WIDTH, BALL_COLOR, INITIAL_BALL_SPEED_X, INITIAL_BALL_SPEED_Y

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_WIDTH, BALL_WIDTH)
        self.color = BALL_COLOR
        self.speed_x = INITIAL_BALL_SPEED_X
        self.speed_y = INITIAL_BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.speed_x = INITIAL_BALL_SPEED_X
        self.speed_y = INITIAL_BALL_SPEED_Y
