import pygame
pygame.display.init()
screen = pygame.display.set_mode((800, 600))
from pgzero.builtins import Actor
from random import randint
apple = Actor("apple")
score = 0
WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()
    apple.draw()
    
def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
    
def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        print("Good Shot!")
        place_apple()
        score = score + 1
        display_score()
    else:
        print("You Missed! F")
        quit()        
        
def display_score():
    print(score)
    
        

place_apple()
