# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:10:00 2020

@author: roger
"""


import tkinter as tk
import numpy as np
import math



def draw_cross(c, center, delta):
    x1 = center[0]
    y1 = center[1]
    
    c.create_line(x1, y1+delta, x1, y1-delta, width=2, fill='blue')
    c.create_line(x1+delta, y1, x1-delta, y1, width=2, fill='blue')
    
def define_circular_pattern(canvas):
    width=500
    height=500
    radius = 100
    center = (int(width/2), int(height/2))
    num_points = 8
    
    
    for k in range(1,3):
        radius *= k
        # canvas.create_oval(center[0]-radius,center[1]-radius,center[0]+radius,center[1]+radius)
    
        num_points *= k
        delta_teta = 2*np.pi/num_points
        for i in range(num_points):
            teta = delta_teta*i
            draw_cross(canvas, (center[0]+int(radius*np.cos(teta)), center[1]+int(radius*np.sin(teta))), 10)
            
    
def main():
    window = tk.Tk()
    
    width=500
    height=500
    canvas = tk.Canvas(window, width=width, height=height)
    canvas.pack()

    
    define_circular_pattern(canvas)
    tk.mainloop()
    


