import pygame
#import paddle
import paddle2
import ball
from player import players
from ball import ball1

GAME_WIDTH = 700
GAME_HEIGHT = 500
GAME_WIN = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Pong")

pygame.font.init()
GAME_FONT_1 = pygame.font.Font('fonts\lcdsolid\LcdSolid-VPzB.ttf', 50)
GAME_FONT_2 = pygame.font.Font('fonts\ozone\Ozone-xRRO.ttf', 50)

WIN_SCORE = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game:
    def render(window, paddles, ball, player1_score, player2_score):
        window.fill(BLACK)

        player1_score_text = GAME_FONT_2.render(f"{player1_score}", 1, players[0].color)
        player2_score_text = GAME_FONT_2.render(f"{player2_score}", 1, players[1].color)

        """
        player1_text = player.player1.name
        player2_text = player.player2.name
        player1_score_text = pygame.font.Font('fonts\ozone\Ozone-xRRO.ttf', 50).render(f"{player1_score}", 1, (255, 255, 255))
        player2_score_text = pygame.font.Font('fonts\ozone\Ozone-xRRO.ttf', 50).render(f"{player2_score}", 1, (255, 255, 255))
        """

        window.blit(player1_score_text, (50, 20))
        window.blit(player2_score_text, (625, 20))

        i = 0
        for paddle in paddles:
            paddle.render(window, players[i].color)
            i += 1

        pygame.display.update()

    def paddle_movement(keys, left_paddle, right_paddle):
        if keys[pygame.K_w] and left_paddle.y - left_paddle.VELOCITY >= 0:
            left_paddle.move(up=True)
        if keys[pygame.K_s] and left_paddle.y + left_paddle.VELOCITY + left_paddle.height <= GAME_HEIGHT:
            left_paddle.move(up=False)

        if keys[pygame.K_UP] and right_paddle.y - right_paddle.VELOCITY >= 0:
            right_paddle.move(up=True)
        if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VELOCITY + right_paddle.height <= GAME_HEIGHT:
            right_paddle.move(up=False)


    def main(self):
        run = True
        clock = pygame.time.Clock()

        right_paddle = paddle2.Paddle(625, 400, 20, 70)
        left_paddle = paddle2.Paddle(50, 400, 20, 70)

        player1_score = 0
        player2_score = 0

        while run:
            clock.tick(100)
            self.render(GAME_WIN, [left_paddle, right_paddle], ball, player1_score, player2_score)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            
            keys = pygame.key.get_pressed()
            self.paddle_movement(keys, left_paddle, right_paddle)

            """ball.Ball.render(GAME_WIN, ball1)"""

game1 = Game
Game.main(game1)
