import pygame

class Ball(pygame.sprite.Sprite):
    VEL = 5

    def __init__(self, x, y, radius, color):
        super().__init__()
        self.radius = radius
        self.x = self.center_x = x
        self.y = self.center_y = y
        self.color = color
        self.image = pygame.Surface([radius * 2, radius * 2], pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.x_velocity = self.VEL
        self.y_velocity = 0

    def render(self, window):
        print("render ball called")
        pygame.draw.circle(self.image, self.color, (self.center_x, self.center_y), self.radius)
        self.rect = self.image.get_rect(center=(self.center_x, self.center_y))

    def move(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

    def restart(self):
        self.x = self.center_x
        self.y = self.center_y
        self.y_vel = 0
        self.x_vel *= -1


ball_sprites = pygame.sprite.Group()
"""
    self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    pygame.draw.circle(self.image, color, (radius, radius), radius)
    self.rect = self.image.get_rect(center=position)
"""