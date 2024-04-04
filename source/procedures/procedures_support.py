# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:32:58 2024

@author: roger
"""

import numpy as np

def get_G_number(procedure, N_intercepted, length=1, M=100, N_inside=0):
    
    if procedure=="Jeffries":
        f = 0.0002*M**2
        N_A = f*(N_inside + 0.5*N_intercepted)
        return (3.321928 * np.log10(N_A) ) - 2.954
    elif procedure=="Heyns":
        l_0 = 32.00 # mm
        
        L = length           # the total test line length
        N_i = N_intercepted  # the number of intercepts
        N_bar = N_i/(M*L)    # mean number of intercepts per unit length of test line
        l_bar = 1/N_bar
        
        return 2*np.log2(l_0/l_bar)
    
    

def draw_lines(canvas, width, height, line_length, nlines=1):
    """
    Draw horizontal parallel lines equally spaced and vertically centered.
    """
    h = 0
    delta_h = int(height/(nlines+1))
    
    x0 = int(0.5*(width - line_length)) + 55
    x1 = x0 + line_length
    
    for i in range(nlines):
        h = h + delta_h
        y0 = h + 55
        y1 = y0        
        canvas.create_line(x0,y0,x1,y1,width=2, fill="red")
        

def draw_circunference(canvas, circunference):
    """Draws a circunference on canvas"""
    
    # print("Draws a circunference")
    radius = circunference[0]
    center = circunference[1]
    delta = 55
    x0 = center[0] - radius + delta
    y0 = center[1] - radius + delta
    x1 = center[0] + radius + delta
    y1 = center[1] + radius + delta
    # print("radius: ", radius)
    # print("center: ", center)
    canvas.create_oval(x0, y0, x1, y1, width=2, outline="red")