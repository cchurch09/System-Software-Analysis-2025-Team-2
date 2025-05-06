import pygame

class Ball(pygame.sprite.Sprite):
    VEL = 10

    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.width = height
        self.height = width
        self.x = self.center_x = x
        self.y = self.center_y = y
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.x_velocity = self.VEL
        self.y_velocity = 0

    def render(self, window):
        print("render ball called")
        pygame.draw.circle(window, self.color, (self.center_x, self.center_y), self.width)


    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    def restart(self):
        self.x = self.center_x
        self.y = self.center_y
        self.y_vel = 0
        self.x_vel *= -1