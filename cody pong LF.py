"""
Pong

Coded By Cody Ross

Originally By Nick Sarbiki

Tutorial Here: https://nick.sarbicki.com/blog/learn-pygame-with-pong/
"""
import random
import sys

import pygame


class Paddle(pygame.Rect):
    def __init__(self, velocity, up_key, down_key, *args, **kwargs):
        self.velocity = velocity
        self.up_key = up_key
        self.down_key = down_key
        super().__init__(*args, **kwargs)

    def move_paddle(self, board_height):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.up_key]: #if you press up
            if self.velocity>-5:
                self.velocity = self.velocity -0.2 

        if keys_pressed[self.down_key]:
            if self.velocity<5:
                self.velocity = self.velocity +0.2

        if (keys_pressed[self.up_key]==False) and (keys_pressed[self.down_key]==False):
            self.velocity = 0.97*self.velocity


         

        #if paddle hits top
        if self.top<1:
            self.velocity=0
            self.top = 2

        #if paddle hits top
        if self.bottom>pong.HEIGHT-1:
            self.velocity=0
            self.bottom = pong.HEIGHT-2


        #move paddle
        self.y = self.y+ self.velocity 


    def reset(self):
        self.velocity=0
        self.y= (pong.HEIGHT/2 - pong.PADDLE_HEIGHT/2)


class Ball(pygame.Rect):
    def __init__(self, velocity, *args, **kwargs):
        self.velocity = velocity
        self.angle = 0
        super().__init__(*args, **kwargs)

    def move_ball(self):
        self.x += self.velocity
        self.y += self.angle
        
    def reset(self):
        #change the x coordinate of the ball to half of the game width.
        self.centerx=pong.WIDTH/2
        self.centery=pong.HEIGHT/2


class Pong:
    HEIGHT = 400
    WIDTH = 800

    PADDLE_WIDTH = 5
    PADDLE_HEIGHT = 50

    BALL_WIDTH = 5
    BALL_VELOCITY = 5
    BALL_ANGLE = 0

    COLOUR = (255, 255, 255)

    def __init__(self):
        pygame.init()  # Start the pygame instance.

        # Setup the screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        # Create the player objects.

        self.paddles = []
        self.balls = []
        self.paddles.append(Paddle(  # The left paddle
            self.BALL_VELOCITY,
            pygame.K_w,
            pygame.K_s,
            0,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT
        ))

        self.paddles.append(Paddle(  # The right paddle
            self.BALL_VELOCITY,
            pygame.K_UP,
            pygame.K_DOWN,
            self.WIDTH - self.PADDLE_WIDTH,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT
        ))

        self.balls.append(Ball(
            self.BALL_VELOCITY,
            self.WIDTH / 2 - self.BALL_WIDTH / 2,
            self.HEIGHT / 2 - self.BALL_WIDTH / 2,
            self.BALL_WIDTH,
            self.BALL_WIDTH
        ))

        self.central_line = pygame.Rect(self.WIDTH/2, 0, 1, self.HEIGHT)

    def check_ball_hits_wall(self):
        for ball in self.balls:
            
            #vertical walls
            if ball.x > self.WIDTH or ball.x<1:
                ball.reset()
            #horizontal walls
            if ball.y > self.HEIGHT - self.BALL_WIDTH or ball.y < 0:
                ball.angle = -ball.angle
                
        

    def check_ball_hits_paddle(self):
        for ball in self.balls:
            for paddle in self.paddles:
                if ball.colliderect(paddle):
                    ball.velocity = -ball.velocity
                    ball.angle = random.randint(-3, 3)
                    

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                # Add some extra ways to exit the game.
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            self.check_ball_hits_paddle()
            self.checNk_ball_hits_wall()

            # Redraw the screen. --------------------------Disabled for debug-----------------------------
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(0, 0, 10, 400))
            pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(790, 0, 10, 400))

            #update the paddles
            for paddle in self.paddles:
                paddle.move_paddle(self.HEIGHT) #move
                pygame.draw.rect(self.screen, self.COLOUR, paddle) #draw

            #update the balls
            for ball in self.balls:
                ball.move_ball() #move
                pygame.draw.rect(self.screen, self.COLOUR, ball) #draw the ball

            pygame.draw.rect(self.screen, self.COLOUR, self.central_line) # draw the central line

            pygame.display.flip() #"update the contents of the entire display." Probably a double buffer screen blit for smooth redraw.
            self.clock.tick(60)


if __name__ == '__main__':
    pong = Pong()
    pong.game_loop()
