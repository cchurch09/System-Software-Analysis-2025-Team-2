"""
File Name: customization.py
Author: Team 2
Date last updated: 5/2/2025
Purpose: This module controls the balls and allows them to function in game, also allows the player to customize the ball's color
"""

import pygame
from customization import customGame

class Ball(pygame.sprite.Sprite):
    VEL = 5

    def __init__(self, x, y, radius, color):
        # initializing all values for the ball
        super().__init__()
        self.radius = radius
        self.x = self.center_x = x
        self.y = self.center_y = y
        self.color = color
        self.image = pygame.Surface([radius * 2, radius * 2], pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.mask = pygame.mask.from_surface(self.image)
        self.x_velocity = self.VEL
        self.y_velocity = 0

    # rendering function to allow the balls to be seen
    def render(self, window):
        print("render ball called")
        pygame.draw.circle(self.image, self.color, (self.center_x, self.center_y), self.radius)
        self.rect = self.image.get_rect(center=(self.center_x, self.center_y))
        window.blit(self.image, self.rect)

    # allows the ball to move
    def move(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

    # restarts the ball
    def restart(self):
        self.x = self.center_x
        self.y = self.center_y
        self.y_velocity = 0
        self.x_velocity *= -1


ball_sprites = pygame.sprite.Group()
"""
    self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    pygame.draw.circle(self.image, color, (radius, radius), radius)
    self.rect = self.image.get_rect(center=position)
"""