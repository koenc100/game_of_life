# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:50:44 2021

@author: koen6
"""

# Imports of libraries
import pygame, sys

# Constants 
SCREENSIZE = WIDTH, HEIGHT = 720, 720

# The main surface to draw on
SCREEN = pygame.display.set_mode(SCREENSIZE)

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
FPS = 60
FPS_GOL = 10

pygame.display.set_caption("The Game of Life")

def color_screen():
    SCREEN.fill(GREY)
    
    
def draw_grid(divisions):

    CONTAINER_WIDTH_HEIGHT = 700  # Not to be confused with SCREENSIZE
    cont_x, cont_y = 10, 10  # TOP LEFT OF CONTAINER

    # DRAW Grid Border:
    # TOP lEFT TO RIGHT
    pygame.draw.line(
      SCREEN, BLACK,
      (cont_x, cont_y),
      (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y), 1)
    # # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
      SCREEN, BLACK,
      (cont_x, CONTAINER_WIDTH_HEIGHT + cont_y),
      (CONTAINER_WIDTH_HEIGHT + cont_x, CONTAINER_WIDTH_HEIGHT + cont_y), 1)
    # # LEFT TOP TO BOTTOM
    pygame.draw.line(
      SCREEN, BLACK,
      (cont_x, cont_y),
      (cont_x, cont_y + CONTAINER_WIDTH_HEIGHT), 1)
    # # RIGHT TOP TO BOTTOM
    pygame.draw.line(
      SCREEN, BLACK,
      (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y),
      (CONTAINER_WIDTH_HEIGHT + cont_x, CONTAINER_WIDTH_HEIGHT + cont_y), 1)

    # Get cell size, just one since its a square grid.
    cellSize = CONTAINER_WIDTH_HEIGHT/divisions

    # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
    for x in range(divisions):
        pygame.draw.line(
           SCREEN, BLACK,
           (cont_x + (cellSize * x), cont_y),
           (cont_x + (cellSize * x), CONTAINER_WIDTH_HEIGHT + cont_y), 1)
    # # HORIZONTAl DIVISIONS
        pygame.draw.line(
          SCREEN, BLACK,
          (cont_x, cont_y + (cellSize*x)),
          (cont_x + CONTAINER_WIDTH_HEIGHT, cont_y + (cellSize*x)), 1)
        
def next_generation():
    return 4

def fill_square():
    # for mouse press, the square gets filled. 
    # Also, the position in the matrix gets from 0 to 1. 
    return 4
        
# The pre function of the game is handled.
def pre_game():
    
    # Initialize the module
    pygame.init()
    clock = pygame.time.Clock()
    
    # Static part 
    color_screen()
    draw_grid(70)
    
    run = True
    
    # While loop for selecting rectangles
    while run:
        
        clock.tick(FPS)
        
        # Break out of the while loop when game is quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        # If mouse gets pressed, fill the rectangle
        fill_square()
        
        # If button "bring to life" is pressed, main function is started
        
        # Update display
        pygame.display.update()
                
                
    pygame.quit()

def main():
    
    clock = pygame.time.Clock()
    
    # Static part 
    color_screen()
    draw_grid(70)
    
    run = True 
    
    # Dynamic part
    while run:
        
        clock.tick(FPS_GOL)
        
        # Break out of the while loop when game is quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                
        # The game of life protecol is run, the cells live 
        next_generation()
        
        # When the reset button is pressed, the grid returns to its empty state
        
        # Update display
        pygame.display.update()
                
                
    pygame.quit()
  

if __name__ == '__main__':
    pre_game()
    
    
    