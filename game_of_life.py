# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:50:44 2021

@author: koen6
"""

# Imports
import pygame, sys

# Constants 
SCREENSIZE = WIDTH, HEIGHT = 1300, 700
SCREEN = pygame.display.set_mode(SCREENSIZE)

WHITE = (255, 255, 255)
GREY = (100, 100, 100)

FPS = 60


pygame.display.set_caption("The Game of Life")

def color_screen():
    SCREEN.fill(GREY)
    pygame.display.update()
    
def draw_grid():
    pygame.draw.line(SCREEN, (1, 1, 1), (10, 10), (10, 590))
    pygame.display.update()
    
def main():
    
    pygame.init()
    clock = pygame.time.Clock()
    
    run = True 
    
    while run:
        
        clock.tick(FPS)
        
        
        for event in pygame.event.get():
            
            # If event is quit end the while loop
            if event.type == pygame.QUIT:
                run = False 
            
            color_screen()
            draw_grid()
                
            
                
    pygame.quit()


if __name__ == '__main__':
    main()
    
    
    