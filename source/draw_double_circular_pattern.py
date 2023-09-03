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
    def __init__(self, window, canvas, center, delta=5):
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
        
        self.line1 = self.canvas.create_line(self.x0, self.y0, self.x1, self.y1, width=1, fill='blue')
        self.line2 = self.canvas.create_line(self.x2, self.y2, self.x3, self.y3, width=1, fill='blue')
        
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
        
        
    def get_center(self):
        """Returns the coordinates for the center of the cross"""
        return (self.x2-55, self.y0-55)
        
        
        
class Cluster:
    """Gather all drawing objects and moves them to the same direction as they were only one object"""
    def __init__(self, window, list_of_forms):
        
        self.master = window
        self.the_list = list_of_forms
        
        self.master.bind("<B1-Motion>", self.movement_callback)
        self.master.bind("<ButtonRelease-1>", self.restart_callback)
        
        self.first_movement = True
        self.ex_old = 0
        self.ey_old = 0
        
        # create an array for all crosses coordinates (x, y)
        n = int(len(self.the_list))
        self.coords = np.zeros(shape=(n,2), dtype=int)
        
        # Set var as false to make program hold on until data is available
        self.var = tk.BooleanVar()
        self.var.set(False)
        
        
    def restart_callback(self, event):
        """When mouse button is released, get crosses coordinates"""
        self.first_movement = True
        self.ex_old = 0
        self.ey_old = 0
        
        # when button is released, get all crosses coordinates
        for i, cross in zip(range(len(self.the_list)), self.the_list):
            c = cross.get_center()
            self.coords[i,:] = c
        
        # print(self.coords)
        # when all coordinates were gathered
        self.var.set(True)
        
        
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
        
        
    def get_coordinates(self):
        """Hold on program while data is obtained. crosses coordinates are not
        available when this function is called"""
        self.master.wait_variable(self.var)
        return self.coords
        
        

def circular(window, canvas, width, height):
    
    # print("w: %d, h: %d" % (width, height))
    radius = 50
    center = (int(width/2+55), int(height/2)+55)
    num_points = 8
    
    teta = 0    
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
    # print(cluster.get_coordinates())
  
    
def get_coordinates(window, canvas, width, height, grid_size):
    radius = 50
    center = (int(width/2+55), int(height/2)+55)
    num_points = int(grid_size/3)
    
    teta = 0    
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
    return cluster.get_coordinates()


class SinglePixel:
    
    def __init__(self, window, img):
        window.bind("<Button-1>", self.get_px_value)
        self.img = img
        
        
    def get_px_value(self, event):
        print("pixel value: %d"  % self.img[event.y-55, event.x-55])
    


def main():
    window = tk.Tk()
    
    width=1500
    height=1500
    canvas = tk.Canvas(window, width=width, height=height)
    canvas.pack()
    circular(window, canvas, width, height)
    tk.mainloop()
    

if __name__ == '__main__':
    main()

