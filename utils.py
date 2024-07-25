# utils.py

import pygame

def draw_center_line(screen):
    pygame.draw.line(screen, (255, 255, 255), (640, 0), (640, 720), 5)

def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

