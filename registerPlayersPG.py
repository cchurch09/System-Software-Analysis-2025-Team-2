import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
from pygame_widgets.slider import Slider
from player import player1
from player import player2


SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

BLACK = (0, 0, 0)

text_font = pygame.font.SysFont("Arial", 10)


class RegisterPlayers():
    def __init__(self):
        pygame.init()
        print("registerPlayersPG was called")
        print(player1.name, player1.color)
        print(player2.name, player2.color)
        pygame.display.set_caption('Register Players')
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        color = (0, 0, 0)
        self.draw_text("Please Register Player Names and Colors", text_font, (0, 0, 0), 220, 150)


        while True:
            screen.fill((color))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()


    def draw_text (text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))