import pygame
#import paddle
import paddle2
import ball2
from player import players
from customMenu import customGame
from ball2 import ball_sprites

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

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 70

class Game:
    def render(window, paddles, player1_score, player2_score, rally_score):
        window.fill(BLACK)

        if customGame.rallyMode == True:
            rally_score_text = GAME_FONT_2.render(f"{rally_score}", 1, WHITE)
            window.blit(rally_score_text, (GAME_WIDTH//2, 20))
        if customGame.singleRally == True:
            rally_score_text = GAME_FONT_2.render(f"{rally_score}", 1, WHITE)
            window.blit(rally_score_text, (GAME_WIDTH//2, 20))
        elif customGame.rallyMode == False & customGame.singleRally == False:
            player1_score_text = GAME_FONT_2.render(f"{player1_score}", 1, players[0].color)
            player2_score_text = GAME_FONT_2.render(f"{player2_score}", 1, players[1].color)
            window.blit(player1_score_text, (50, 20))
            window.blit(player2_score_text, (625, 20))

        """
        player1_text = player.player1.name
        player2_text = player.player2.name
        player1_score_text = pygame.font.Font('fonts\ozone\Ozone-xRRO.ttf', 50).render(f"{player1_score}", 1, (255, 255, 255))
        player2_score_text = pygame.font.Font('fonts\ozone\Ozone-xRRO.ttf', 50).render(f"{player2_score}", 1, (255, 255, 255))
        """

        p = 0
        for paddle in paddles:
            """print("Calling render paddles")"""
            paddle.render(window, players[p].color)
            if p == 0:
                p = 1
            if p == 1:
                p = 0
            else:
                print("i index error")

        ball_sprites.draw(GAME_WIN)
        pygame.display.update()

    def paddle_movement(keys, left_paddle, right_paddle):
        if keys[pygame.K_w] and left_paddle.rect.y - left_paddle.VELOCITY >= 0:
            left_paddle.move(up=True)
        if keys[pygame.K_s] and left_paddle.rect.y + left_paddle.VELOCITY + left_paddle.height <= GAME_HEIGHT:
            left_paddle.move(up=False)

        if customGame.singleRally == False:
            if keys[pygame.K_UP] and right_paddle.rect.y - right_paddle.VELOCITY >= 0:
                right_paddle.move(up=True)
            if keys[pygame.K_DOWN] and right_paddle.rect.y + right_paddle.VELOCITY + right_paddle.height <= GAME_HEIGHT:
                right_paddle.move(up=False)
        
        # Rotation    
        if customGame.paddleRotation == True:
            if keys[pygame.K_a]: 
                left_paddle.rotate(-5)
            if keys[pygame.K_d]:
                left_paddle.rotate(5)

            if customGame.singleRally == False:
                if keys[pygame.K_LEFT]:
                    right_paddle.rotate(-5)
                if keys[pygame.K_RIGHT]:
                    right_paddle.rotate(5)


    def main(self):
        run = True
        clock = pygame.time.Clock()

        if customGame.singleRally == True:
            right_paddle = paddle2.Paddle(630, 0, 20, GAME_HEIGHT, players[1].color)
            left_paddle = paddle2.Paddle(50, 225, 20, 70, players[0].color)
        elif customGame.rallyMode == True:
            right_paddle = paddle2.Paddle(630, 225, 20, 70, players[1].color)
            left_paddle = paddle2.Paddle(50, 225, 20, 70, players[0].color)
        else:
            right_paddle = paddle2.Paddle(630, 225, 20, 70, players[1].color)
            left_paddle = paddle2.Paddle(50, 225, 20, 70, players[0].color)
        """
        balls = []
        left_paddle = paddle2.Paddle(50, (GAME_HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT, players[0].color)
        right_paddle = paddle2.Paddle(GAME_WIDTH - 50 - PADDLE_WIDTH, (GAME_HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT, players[1].color)
        ballProto = ball2.Ball(GAME_WIDTH//2, GAME_HEIGHT//2, 5, customGame.ballColor)
        """
        for i in range(customGame.ballCount):
            ball = ball2.Ball(GAME_WIDTH//2, GAME_HEIGHT//2, 5, customGame.ballColor)
            ball_sprites.add(ball)

        player1_score = 0
        player2_score = 0
        rally_score = 0

        while run:
            clock.tick(100)
            self.render(GAME_WIN, [left_paddle, right_paddle], player1_score, player2_score, rally_score)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            
            keys = pygame.key.get_pressed()
            self.paddle_movement(keys, left_paddle, right_paddle)

            for ball in ball_sprites:
                ball.move()
           
           # Collision     
            for paddle in [left_paddle, right_paddle]:
                    offset = (paddle.rect.x - ball.rect.x, paddle.rect.y - ball.rect.y)
                    if ball.mask.overlap(paddle.mask, offset):
                        print("Collision detected with paddle!")
                        ball.x_velocity *= -1
                        # Where is the ball hitting the paddle?
                        relative_intersect = (ball.rect.centery - paddle.rect.centery) / (paddle.height / 2)
                        bounce_strength = 2
                        ball.y_velocity = int(relative_intersect * bounce_strength)
            ball_sprites.draw(GAME_WIN)
            GAME_WIN.fill((BLACK))

game1 = Game
Game.main(game1)
