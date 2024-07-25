
import pygame
from settings import PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_COLOR

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.color = PADDLE_COLOR

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
