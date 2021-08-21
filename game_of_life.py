# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:50:44 2021

@author: koen6
"""

# Imports of libraries
import pygame
from pygame.locals import *
import numpy as np
import scipy

# Title
pygame.display.set_caption("The Game of Life")

# The main surface to draw on
SCREEN = pygame.display.set_mode(SCREENSIZE)

# Constants 
SCREENSIZE = WIDTH, HEIGHT = 820, 720
GREY = (200, 200, 200)
BLACK = (0, 0, 0)

FPS = 60
divisions = 50
rebirth_rate = 100
    
def draw_grid(divisions):
    
    """
    Function creates and draws (divisions x divisions) grid.
    Returns cellSize in pixels and a numpy zero matrix with the same dimentions
    """

    CONTAINER_WIDTH_HEIGHT = 700  
    cont_x, cont_y = 10, 10  # Top left

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
        
    # Make numpy grid
    MAP = np.zeros((divisions, divisions))   
        
    return cellSize, MAP
   
def draw_startbutton():
    
    # Draw rectangle and text on screen
    pygame.draw.rect(SCREEN, GREEN, (720, 200, 90, 100))
    font = pygame.font.SysFont(None, 40)
    text = font.render('Start', True, BLACK)
    SCREEN.blit(text, (730, 235))
    
def draw_resetbutton():
    
    # Draw rectangle and text on screen
    pygame.draw.rect(SCREEN, RED, (720, 400, 90, 100))
    font = pygame.font.SysFont(None, 40)
    text = font.render('Reset', True, BLACK)
    SCREEN.blit(text, (730, 435))  
    
def fill_square_click(mx, my, cellSize, MAP):
    
    """
    Function fills squares in grid and updates starting matrix
    """
    
    # Get [x, y] location of clicked cell
    x_loc = int((mx - 10)  // cellSize)
    y_loc = int((my - 10)  // cellSize)
    
    # Define corner locations of square to be filled (+10 for padding, +1 for frid)
    x_coor = x_loc * cellSize + 11
    y_coor = y_loc * cellSize + 11
    
    # If not filled
    if  MAP[y_loc, x_loc] == 0:
        
        # Change selected square from 0 to 1. (columns x rows)
        MAP[y_loc, x_loc] = 1
    
        # Draw rectangle on screen (-1 for grid)
        pygame.draw.rect(SCREEN, BLACK, (x_coor, y_coor, cellSize-1, cellSize-1))
        
    else:
        # change selected square from 0 to 1. (columns x rows)
        MAP[y_loc, x_loc] = 0
    
        # Draw rectangle on screen
        pygame.draw.rect(SCREEN, GREY, (x_coor, y_coor, cellSize-1, cellSize-1))
        
def fill_grid(x, y, cellSize, color):
    
    """
    Fills cell on x, y coordinate
    """
    
    x_coor = (x * cellSize) + 11
    y_coor = (y * cellSize) + 11
    
    # Draw rectangle on screen
    pygame.draw.rect(SCREEN, color, (x_coor, y_coor, cellSize-1, cellSize-1))
    
def next_generation(MAP, cellSize):
    
    """
    Function takes the current state of the grid in numpy array
    Returns the new state of the grid after 1 generation
    """
     
    # Kernel used for convolution
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    
    # Matrix with sum of neighbors as entities 
    MAP_mask = scipy.ndimage.convolve(MAP, kernel, mode='constant')
    
    # Empty matrix used to fill
    MAP_next = np.zeros((MAP.shape[0], MAP.shape[1]))
    
    # Itterate over every item in the MAP, possible faster way: Fancy indexing
    for x in range(MAP.shape[1]):
        for y in range(MAP.shape[0]):
            old_cell = MAP[y, x]
            neighbors_cell = MAP_mask[y, x]
            
            # Cell lives on 
            if 3 >= neighbors_cell >= 2 and old_cell == 1:
                MAP_next[y, x] = 1
                fill_grid(x, y, cellSize, BLACK)
                
            # Cell rebirth
            elif neighbors_cell == 3 and old_cell == 0:
                MAP_next[y, x] = 1
                fill_grid(x, y, cellSize, BLACK)
                
            # All else dies
            else:
                MAP_next[y, x] = 0 
                fill_grid(x, y, cellSize, GREY)
                
    return MAP_next
                             
def reset_game(divisions):
    
    """
    Function resets game

    """
    # Draw statics 
    SCREEN.fill(GREY)
    cellSize, MAP = draw_grid(divisions)
    draw_startbutton()
    draw_resetbutton()
    
    return cellSize, MAP
    
def main():
    
    # Initialize the module
    pygame.init()
    clock = pygame.time.Clock() 
    
    # Draw clean game
    cellSize, MAP = reset_game(divisions)
    
    # Make timer
    pygame.time.set_timer(pygame.USEREVENT, rebirth_rate)
    
    run = True
    start = False
    
    while run:
        
        clock.tick(FPS)
        
        # Get x and y coordinates of mouse
        mx, my = pygame.mouse.get_pos()
        
        # Break out of the while loop when game is quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # if left mouse button is pressed and within grid, run fill_square
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and 710 > mx > 10 and 710 > my > 10:
                    fill_square_click(mx, my, cellSize, MAP)
                    
                # Startbutton pressed 
                if event.button == 1 and 810 > mx > 720 and 300 > my > 200:
                    start = True
                    
                # Resetbutton pressed
                if event.button == 1 and 810 > mx > 720 and 500 > my > 400:
                    cellSize, MAP = reset_game(divisions)
                    start = False
            
            # If start button is pressed, start a timed event
            if start == True and event.type == pygame.USEREVENT:
                MAP = next_generation(MAP, cellSize)
                     
        # Update display
        pygame.display.update()
                    
    pygame.quit()

if __name__ == '__main__':
    main()
    
    

    
    