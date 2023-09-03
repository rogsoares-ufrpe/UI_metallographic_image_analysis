# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:10:00 2020

@author: roger
"""


import tkinter as tk
import numpy as np
import math


class Cross:
    """Defines an object which draws a cross on canvas"""
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
        
    def move(self, dx, dy):
        """ Moves the object from a offset dx and dy """
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
        
        
        
class Cluster:
    """Gather drawing objects and moves all them to the same direction as they were only one object"""
    def __init__(self, window, list_of_forms):
        
        self.the_list = list_of_forms
        
        window.bind("<B1-Motion>", self.movement_callback)
        window.bind("<ButtonRelease-1>", self.restart_callback)
        
        self.first_movement = True
        self.ex_old = 0
        self.ey_old = 0
        
        
    def restart_callback(self, event):
        self.first_movement = True
        self.ex_old = 0
        self.ey_old = 0
        
        
    def movement_callback(self, event):
        if not self.first_movement:
            dx = event.x - self.ex_old
            dy = event.y - self.ey_old    
            for form in self.the_list:
                form.move(dx,dy)
        else:
            self.first_movement = False
            
        self.ex_old = event.x
        self.ey_old = event.y
        
        

def define_circular_pattern(window, canvas, width, height):

    radius = 100
    center = (int(width/2), int(height/2))
    num_points = 8
    
    teta = 0    
    x0 = center[0]+int(radius*np.cos(teta))
    y0 = center[1]+int(radius*np.sin(teta))
    
    crosses = []
    
    # draw 8+16 crosses over two circular concentric patterns
    for k in range(1,3):
        radius *= k    
        num_points *= k
        delta_teta = 2*np.pi/num_points
        
        for i in range(num_points):
            teta = delta_teta*i
            x0 = center[0]+int(radius*np.cos(teta))
            y0 = center[1]+int(radius*np.sin(teta)) 
            crosses.append(Cross(window, canvas, (x0,y0)))  
    
    cluster = Cluster(window, crosses)
    

def main():
    window = tk.Tk()
    
    width=1500
    height=1500
    canvas = tk.Canvas(window, width=width, height=height)
    canvas.pack()
    define_circular_pattern(window, canvas, width, height)
    tk.mainloop()
    

if __name__ == '__main__':
    main()
