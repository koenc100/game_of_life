# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 18:37:34 2021

@author: koen6
"""

import numpy as np
from scipy.ndimage import convolve
import scipy
import time

A = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

print(A.shape)

def next_generation(MAP):
     
    # kernel used for convolution
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    
    # Matrix with sum of neighbors as entities 
    MAP_mask = scipy.ndimage.convolve(MAP, kernel, mode='constant')
    
    # Empty matrix used to fill
    MAP_next = np.zeros((MAP.shape[0], MAP.shape[1]))
    
    # itterate over every item in the MAP, possible faster way: Fancy indexing
    for x in range(MAP.shape[1]):
        for y in range(MAP.shape[0]):
            old_cell = MAP[y, x]
            neighbors_cell = MAP_mask[y, x]
            
            # Cell lives on 
            if 3 >= neighbors_cell >= 2 and old_cell == 1:
                MAP_next[y, x] = 1
                
            # Cell rebirth
            elif neighbors_cell == 3 and old_cell == 0:
                MAP_next[y, x] = 1
                
            # All else dies
            else:
                MAP_next[y, x] = 0 
                
    return MAP_next
                
            
def protocol(MAP):
    
    run = True
    
    # run the protocol
    while run:
        
        time.sleep(1)
        
        MAP = next_generation(MAP)
        
        print(MAP)
        
            
protocol(A)




