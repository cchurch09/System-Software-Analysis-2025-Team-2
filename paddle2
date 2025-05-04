import pygame

class Paddle(pygame.sprite.Sprite):
    VEL = 5 

    def __init__(self, x, y, width, height, color=(255, 255, 255)):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.width = width
        self.height = height
        self.color = color

    def render(self, window, color=None):
        if color:
            self.image.fill(color)
        else:
            self.image.fill(self.color)
        window.blit(self.image, self.rect)

    def move(self, up=True):
        if up:
            self.rect.y -= self.VEL
        else:
            self.rect.y += self.VEL