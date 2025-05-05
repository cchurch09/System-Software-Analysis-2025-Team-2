import pygame

class Ball(pygame.sprite.Sprite):
    VEL = 5

    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.x = self.center_x = x
        self.y = self.center_y = y
        self.image = pygame.surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.width = width
        self.height = height
        self.color = color

    def render(self, window, color):
        if color:
            self.image.fill(color)
        else:
            self.image.fill(self.color)
        window.blit(self.image, self.rect)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def restart(self):
        self.x = self.center_x
        self.y = self.center_y
        self.y_vel = 0
        self.x_vel *= -1