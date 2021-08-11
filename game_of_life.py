# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:50:44 2021

@author: koen6
"""

# Imports
import pygame, sys

# Constants 
SCREENSIZE = WIDTH, HEIGHT = 600, 400
SCREEN = pygame.display.set_mode(SCREENSIZE)
 

def main():
    
    pygame.init()
    
    run = True 
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                
        pygame.quit()


if __name__ == '__main__':
    main()
    
    
    