import pygame
#import paddle
import paddle2
import ball2
import math
import random
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
PADDLE_HEIGHT = 90

class Game:
    def render(self, window, paddles, player1_score, player2_score, rally_score):
        window.fill(BLACK)

        # tells the game what to render based on selected game mode
        if customGame.rallyMode == True:
            rally_score_text = GAME_FONT_2.render(f"{players[0].name}    {rally_score}    {players[1].name}", 1, WHITE)
            rally_text_rect = rally_score_text.get_rect(center=(GAME_WIDTH // 2, 20))
            window.blit(rally_score_text, rally_text_rect)
        if customGame.singleRally == True:
            rally_score_text = GAME_FONT_2.render(f"{rally_score}", 1, WHITE)
            window.blit(rally_score_text, (GAME_WIDTH//2, 20))
        elif customGame.rallyMode == False and customGame.singleRally == False:
            # Displaying Player names
            score_text = f"{players[0].name} {player1_score} - {player2_score} {players[1].name}"
            score_display = GAME_FONT_2.render(score_text, 1, WHITE)
            text_rect = score_display.get_rect(center=(GAME_WIDTH // 2, 20))  # Center the text
            window.blit(score_display, text_rect)  # Draw the text in the center

        # tells the game ro render the paddles
        for paddle in paddles:
            """print("Calling render paddles")"""
            paddle.render(window)

        # tells the game to render the balls as a full group of sprites
        ball_sprites.draw(GAME_WIN)
        pygame.display.update()

    # paddle controls
    def paddle_movement(self, keys, left_paddle, right_paddle):
        paddle_controls = {
            pygame.K_w: (left_paddle, True),
            pygame.K_s: (left_paddle, False),
            pygame.K_UP: (right_paddle, True),
            pygame.K_DOWN: (right_paddle, False),
        }

        # paddle movement handling
        for key, (paddle, up) in paddle_controls.items():
            if keys[key]:
                if up and paddle.rect.y - paddle.VELOCITY >= 0:
                    paddle.move(up=True)
                elif not up and paddle.rect.y + paddle.VELOCITY + paddle.height <= GAME_HEIGHT:
                    paddle.move(up=False)

        # paddle rotation handling
        if customGame.paddleRotation == True:
            rotation_controls = {
                pygame.K_a: left_paddle,
                pygame.K_d: left_paddle,
                pygame.K_LEFT: right_paddle,
                pygame.K_RIGHT: right_paddle,
            }
            for key, paddle in rotation_controls.items():
                if keys[key]:
                    angle = -5 if key in (pygame.K_a, pygame.K_LEFT) else 5
                    paddle.rotate(angle)

    # main function that runs the game
    def main(self):
        pygame.init()
        run = True
        clock = pygame.time.Clock()

        # Tells the game which paddles to render based on the game mode
        if customGame.singleRally == True:
            right_paddle = paddle2.Paddle(630, 0, 20, GAME_HEIGHT, players[1].color)
            left_paddle = paddle2.Paddle(50, 225, PADDLE_WIDTH, PADDLE_HEIGHT, players[0].color)
        elif customGame.rallyMode == True:
            right_paddle = paddle2.Paddle(630, 225, PADDLE_WIDTH, PADDLE_HEIGHT, players[1].color)
            left_paddle = paddle2.Paddle(50, 225, PADDLE_WIDTH, PADDLE_HEIGHT, players[0].color)
        else:
            right_paddle = paddle2.Paddle(630, 225, PADDLE_WIDTH, PADDLE_HEIGHT, players[1].color)
            left_paddle = paddle2.Paddle(50, 225, PADDLE_WIDTH, PADDLE_HEIGHT, players[0].color)

        # creates a number of balls depending on how many balls in ballcount
        for i in range(customGame.ballCount):
            ball = ball2.Ball(GAME_WIDTH//2, GAME_HEIGHT//2, 5, customGame.ballColor)
            ball_sprites.add(ball)

        # initial score settings
        player1_score = 0
        player2_score = 0
        rally_score = 0

        # main gameplay loop
        while run:
            clock.tick(100)

            #filling screen black before rendering
            GAME_WIN.fill(BLACK)

            #Rendering paddles and scores
            self.render(GAME_WIN, [left_paddle, right_paddle], player1_score, player2_score, rally_score)

            # allos the game to quit properly
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    break
            
            #pygame movement calls
            keys = pygame.key.get_pressed()
            self.paddle_movement(keys, left_paddle, right_paddle)

            # handles movement for all of the balls and checking whether they are in bounds or not
            for ball in ball_sprites:
                ball.move()

                # Check if the ball goes out of bounds
                if ball.rect.left < 0 or ball.rect.right > GAME_WIDTH:
                    if ball.rect.left < 0:
                        player2_score += 1
                    elif ball.rect.right > GAME_WIDTH:
                        player1_score += 1
                    elif customGame.rallyMode == True:
                        rally_score = 0
                    elif customGame.singleRally == True:
                        rally_score = 0
                    ball.restart()  # Reset the ball position
                    ball.x_velocity = 5
                    ball.y_velocity = 0

                
                # Collision detection
                for paddle in [left_paddle, right_paddle]:
                    offset = (paddle.rect.x - ball.rect.x, paddle.rect.y - ball.rect.y)
                    if ball.mask.overlap(paddle.mask, offset):
                        print("Collision detected with paddle!")
                        rally_score += 1
                        '''
                        # Sticking fix
                        # Basically - if ball is moving right, keep it to the left of the paddle
                        if ball.x_velocity > 0:
                            ball.rect.left = paddle.rect.right
                        else:
                            ball.rect.right = paddle.rect.left
                        '''    
                        # Where is the ball hitting the paddle?
                        relative_intersect = (ball.rect.centery - paddle.rect.centery) / (paddle.rect.height / 2)
                        bounce_strength = 2
                        ball.y_velocity = int(relative_intersect * bounce_strength)

                        # adding randomness to the reflection
                        randomfactor = random.uniform(-1.75, 1.75)
                        ball.y_velocity += int(randomfactor)

                        # reversing x velocity
                        ball.x_velocity *= -1
                
                """
                for paddle in [left_paddle, right_paddle]:
                    offset = (paddle.rect.x - ball.rect.x, paddle.rect.y - ball.rect.y)
                    if ball.mask.overlap(paddle.mask, offset):
                        # Calculate the angle of reflection
                        paddle_center_y = paddle.rect.centery
                        hit_position = ball.rect.centery  # Y position where the ball hit the paddle
                        relative_intersect = (hit_position - paddle_center_y) / (paddle.rect.height / 2)

                        # Calculate the new angle based on the paddle's angle
                        paddle_angle_rad = math.radians(paddle.angle)
                        bounce_strength = 2
                        ball.y_velocity = int(relative_intersect * bounce_strength) + int(math.sin(paddle_angle_rad) * bounce_strength)
                        ball.x_velocity *= -1  # Reverse the x direction
                """
  
                # Keep ball within bounds of screen (Top and bottom)            
                if ball.rect.top <= 0:
                    ball.rect.top = 0
                    ball.y_velocity *= -1

                if ball.rect.bottom >= GAME_HEIGHT:
                    ball.rect.bottom = GAME_HEIGHT
                    ball.y_velocity *= -1

                # Update score and reset ball if paddle misses ball
                if ball.rect.right >= GAME_WIDTH:
                    player1_score += 1
                    ball.rect.center = (GAME_WIDTH // 2, GAME_HEIGHT // 2)
                    ball.x_velocity *= -1
                    ball.y_velocity = 0

                elif ball.rect.left <= 0:
                    player2_score += 1  
                    ball.rect.center = (GAME_WIDTH // 2, GAME_HEIGHT // 2)
                    ball.x_velocity *= -1
                    ball.y_velocity = 0
                    
            # drawing al of the balls in the game
            ball_sprites.draw(GAME_WIN)
            pygame.display.update()

            # determines which player won or prevents the game from ending during free play mode
            won = False
            if customGame.freePlay == False:
                if player1_score >= WIN_SCORE:
                    won = True
                    win_text = (f"{players[0].name} WON!")
                elif player2_score >= WIN_SCORE:
                    won = True
                    win_text = (f"{players[1].name} WON!")

            # the actual win screen
            if won:
                text = GAME_FONT_2.render(win_text, 1, WHITE)
                GAME_WIN.blit(text, (GAME_WIDTH//2 - text.get_width() // 2, GAME_HEIGHT//2 - text.get_height() //2))
                pygame.display.update()
                pygame.time.delay(5000)
                ball.restart()
                for paddle in [left_paddle, right_paddle]:
                    paddle.restart()
                player1_score = 0
                player2_score = 0
        pygame.quit()
        pygame.QUIT

game1 = Game()
