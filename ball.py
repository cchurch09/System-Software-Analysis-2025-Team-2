import pygame

class Ball:
    VEL_CAP = 10
    color = (255, 255, 255)

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.VEL_CAP
        self.y_vel = 0

    def render(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def newColor(self, color):
        self.color = color

ball1= Ball( 50, 50, 10)
