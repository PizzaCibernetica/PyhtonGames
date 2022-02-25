# This is my first Python Game
from termios import VEOL
import pygame
import sys
import os       # to define path to import hte images

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 400
BLUE_COLOR = (0,100,200)        # constant for color 
BLACK_COLOR = (0,0,0)           # constant for black color
FPS = 60                        # constant for refresh rate 
BORDER = pygame.Rect(SCREEN_WIDTH/2-5 ,0 , 10 , SCREEN_HEIGHT)         # position a rectagle to limit movement of rockets
# ROCKET = pygame.image.load('Assets/rocket.png')  this is the direct refernce 
ROCKET = pygame.image.load(os.path.join('Assets', 'rocket.png')) # this way it will ensure cross compatibility with different OSs
ROCKET_H, ROCKET_W = 40 ,60
ROCKET_RIGHT = pygame.transform.rotate(pygame.transform.scale(ROCKET, (ROCKET_H,ROCKET_W)), 90)
ROCKET_LEFT = pygame.transform.rotate(pygame.transform.scale(ROCKET, (ROCKET_H,ROCKET_W)), 270)
VELOCITY = 5

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("My first Game")


# defining the draw window
def draw_window(left_rocket,right_rocket):
    window.fill(BLUE_COLOR)     # draw this first for avoind covering the rest
    pygame.draw.rect(window, BLACK_COLOR, BORDER)
    window.blit(ROCKET_RIGHT, (right_rocket.x,right_rocket.y))         # blit is a surface on top of the screen
    window.blit(ROCKET_LEFT, (left_rocket.x,left_rocket.y))
    pygame.display.update()         # update an area of the screen if given coordinates
    # or pygame.display.flip()      # refresh the entire screen

def right_rocket_movement(keys_pressed, rocket):
    if keys_pressed[pygame.K_LEFT] and rocket.x - VELOCITY > (SCREEN_WIDTH/2):
            rocket.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and rocket.x + VELOCITY < (SCREEN_WIDTH - ROCKET_W):
            rocket.x += VELOCITY
    if keys_pressed[pygame.K_DOWN] and rocket.y + VELOCITY < (SCREEN_HEIGHT - ROCKET_H):
            rocket.y += VELOCITY
    if keys_pressed[pygame.K_UP] and rocket.y - VELOCITY > 0:
            rocket.y -= VELOCITY

def left_rocket_movement(keys_pressed, rocket):
    if keys_pressed[pygame.K_a] and rocket.x - VELOCITY > 0:
            rocket.x -= VELOCITY
    if keys_pressed[pygame.K_d] and rocket.x + VELOCITY < (SCREEN_WIDTH/2 - ROCKET_W):
            rocket.x += VELOCITY
    if keys_pressed[pygame.K_s] and rocket.y + VELOCITY < (SCREEN_HEIGHT - ROCKET_H):
            rocket.y += VELOCITY
    if keys_pressed[pygame.K_w] and rocket.y - VELOCITY > 0:
            rocket.y -= VELOCITY


# defining main function
def main():
    right_rocket = pygame.Rect(900, 150, ROCKET_W, ROCKET_H)
    left_rocket = pygame.Rect(50, 150, ROCKET_W, ROCKET_H) # to identify rectangle to track the movement of the rocket
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)             # to make sure refresh rate is at 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        # left_rocket.x += 1      # to check movement - will add 1 pixel to the x, moving at 60 FPS = 60 pixels/second 
        # right_rocket.x += -1    # to check movement
        keys_pressed = pygame.key.get_pressed()
        left_rocket_movement(keys_pressed, left_rocket)
        right_rocket_movement(keys_pressed, right_rocket)
      


        draw_window(left_rocket,right_rocket) # add rectagles  to pass to draw window function 


# to make sure main comes from this program and not from a differnt module/library
if __name__ == "__main__":
    main()
