import pygame

class Paddle(pygame.sprite.Sprite):
    VELOCITY = 3
    
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.original_image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image = self.original_image.copy()
        self.x = self.origin_x = x
        self.y = self.origin_y = y
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.width = width
        self.height = height
        self.color = color

    # allows the paddles to render properly
    def render(self, window):
        pygame.draw.rect(self.original_image, self.color, (0, 0, self.original_image.get_width(), self.original_image.get_height()))
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.mask = pygame.mask.from_surface(self.image)
        window.blit(self.image, self.rect)

    # decides how paddle movement up and down works
    def move(self, up=True):
        if up:
            self.rect.y -= self.VELOCITY
        else:
            self.rect.y += self.VELOCITY

    # restarts the position for the paddles
    def restart(self):
        self.x = self.origin_x
        self.y = self.origin_y
    
    # allows the paddles to rotate
    def rotate(self, angle_change):
        self.angle = (self.angle + angle_change) % 360
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)
        self.mask = pygame.mask.from_surface(self.image)