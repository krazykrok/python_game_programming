"""
Snake

Coded by Cody Ross

Originally by Edureka

"""
#import libraries
import pygame
import time
import random
import math
 
pygame.init()

#put RGB tuples in variables for each colour 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#set display window width variables 
disp_width = 600
disp_height = 400

#make a display object
disp = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption('Snake Game by Edureka')

#set up timer
clock = pygame.time.Clock()

snake_block_width = 30
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#draw score
def render_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    disp.blit(value, [0, 0])

#draw snake 
def render_snake(snake_block_width, snake_list):
    for block in snake_list:
        pygame.draw.rect(disp, black, [block[0], block[1], snake_block_width, snake_block_width]) #
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    disp.blit(mesg, [disp_width / 6, disp_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False

    #initialise snake starting position
    x1 = math.floor(disp_width / snake_block_width/2)*snake_block_width
    y1 = math.floor(disp_height / snake_block_width/2)*snake_block_width

    #initialis speeds to zero
    x1_change = 0
    y1_change = 0

    #declare snake array
    snake_List = []
    Length_of_snake = 1
 
    #set a random location of food (100 possible locations in a grid of 10 by 10)
    foodx = round(random.randrange(0, math.floor(disp_width/snake_block_width))) * snake_block_width
    foody = round(random.randrange(0, math.floor(disp_height/snake_block_width))) * snake_block_width


    #main game loop
    while not game_over:

        #quit loop
        while game_close == True:
            disp.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            render_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True #exit game loop
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop() #restart game

        #sift through pygame events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            #key press events to set direction:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_width
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_width
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_width
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_width
                    x1_change = 0

        #check for collisions with walls
        if x1 >= disp_width or x1 < 0 or y1 >= disp_height or y1 < 0:
            game_close = True
        
        #update position of snake head
        x1 += x1_change
        y1 += y1_change



        #create coordinate array for snake (containing x and y)
        snake_head_coords = []
        snake_head_coords.append(x1)
        snake_head_coords.append(y1)

        #add snake head coordinates to the end of the snake_list; the head is the highest index.
        snake_List.append(snake_head_coords)

        #if snake list is longer than it should be
        if len(snake_List) > Length_of_snake:
            del snake_List[0] #delete the head? - probably chopping off the back of the snake
        
        #check to see if snake bit himself
        for block_coords in snake_List[:-1]: # [start:end] beginning to item -1 (everything in the array except the last 1 item)
            if block_coords == snake_head_coords:
                game_close = True

        #render playing field
        disp.fill(blue)
        #render food
        pygame.draw.rect(disp, green, [foodx, foody, snake_block_width, snake_block_width])

        #Render the snake
        render_snake(snake_block_width, snake_List)
        #render score
        render_score(Length_of_snake - 1)

        #blit display
        pygame.display.update()

        #check collision with food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, math.floor(disp_width/snake_block_width))) * snake_block_width
            foody = round(random.randrange(0, math.floor(disp_height/snake_block_width))) * snake_block_width
            Length_of_snake += 1

        #wait for next clock tick
        clock.tick(snake_speed) #frames per second
 
    pygame.quit()
 
#launch the game loop
gameLoop()