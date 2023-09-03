# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:10:00 2020

@author: roger
"""


import tkinter as tk
import numpy as np
import math



class Cross:

    def __init__(self, window, canvas, center, delta=10):
        # horizontal
        self.x0 = center[0] - delta
        self.y0 = center[1]
        self.x1 = center[0] + delta
        self.y1 = self.y0
        
        # vertical
        self.x2 = center[0]
        self.y2 = center[1] + delta
        self.x3 = self.x2
        self.y3 = center[1] - delta
        
        self.delta = delta
        self.canvas = canvas
        
        self.line1 = self.canvas.create_line(self.x0, self.y0, self.x1, self.y1, width=2, fill='blue')
        self.line2 = self.canvas.create_line(self.x2, self.y2, self.x3, self.y3, width=2, fill='blue')
        
        window.bind("<B1-Motion>", self.move2)
        self.first_movement = True
        self.ex_old = 0
        self.ey_old = 0
        
        
    def move(self, event):
        dx = event.x - self.x0
        dy = event.y - self.y0
        
        self.canvas.move(self.line1, dx, dy)
        self.canvas.move(self.line2, dx, dy)
        
        self.x0 = self.x0 + dx
        self.y0 = self.y0 + dy
        # print("dx = %d, dy = %d, x0 = %d, y0 = %d, click: %d, %d" % (dx,dy,x0,y0, event.x, event.x))
    
    def move2(self, event):
        
        if not self.first_movement:
            dx = event.x - self.ex_old
            dy = event.y - self.ey_old
            
            self.x0 = self.x0 + dx
            self.y0 = self.y0 + dy
            self.x1 = self.x1 + dx
            self.y1 = self.y1 + dy
            
            self.x2 = self.x2 + dx
            self.y2 = self.y2 + dy
            self.x3 = self.x3 + dx
            self.y3 = self.y3 + dy
            
            newxy1 = [self.x0, self.y0, self.x1, self.y1]
            newxy2 = [self.x2, self.y2, self.x3, self.y3]
            self.canvas.coords(self.line1, *newxy1)
            self.canvas.coords(self.line2, *newxy2)
            
            
        else:
            self.first_movement = False
            
        self.ex_old = event.x
        self.ey_old = event.y
    

def define_circular_pattern(window, canvas):
    width=500
    height=500
    radius = 100
    center = (int(width/2), int(height/2))
    num_points = 8
    
    teta = 0    
    x0 = center[0]+int(radius*np.cos(teta))
    y0 = center[1]+int(radius*np.sin(teta))
    
    cross1 = Cross(window, canvas, (x0,y0))
    

def main():
    window = tk.Tk()
    
    width=500
    height=500
    canvas = tk.Canvas(window, width=width, height=height)
    canvas.pack()
    define_circular_pattern(window, canvas)
    tk.mainloop()
    


main()
