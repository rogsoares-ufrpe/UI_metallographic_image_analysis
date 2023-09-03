# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:25:06 2020

@author: Rogerio
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:53:06 2020

@author: roger_000
"""
import threading


# Canvas class of Tkinter supports a functions which is used to move objects 
# from one position to another in any canvas or tkinter toplevel.
# Syntax: Canvas.move(canvas_object, x, y)

# imports every file form tkinter and tkinter.ttk 
from tkinter import *
# import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import cv2

class MCAI:
    """Moving Circle Around Image"""
    def __init__(self, radius, width, height, canvas, master): 
        self.master = master
        self.var = BooleanVar()
        self.var.set(False)
        self.width = width
        self.height = height
        
        self.master.bind("<Motion>", lambda e: self.callback(e))
        self.master.bind("<ButtonRelease-1>", lambda e: self.callback2(e))
        
        self.radius = radius
        self.x = 5
        self.y = 5
        self.x_old = self.x
        self.y_old = self.y
        
        self.stop_move = False
        self.canvas = canvas 
        self.circle = self.canvas.create_oval(5,5,2*radius,2*radius, width=2, outline="red")
        
      
    def movement(self):
        check1 = True #self.x >= 55 and self.x+2*self.radius <= self.width+55
        check2 = True #self.y >= 55 and self.y+2*self.radius <= self.height+55
        
        # do not allow any movement after mouse click
        if not self.stop_move:
            x = self.x - self.x_old
            y = self.y - self.y_old 
            self.canvas.move(self.circle, x, y) 
            # print("%d, %d" % (self.x, self.y))
            self.x_old = self.x
            self.y_old = self.y
            
            # self.canvas.update()
        
        
    def callback(self, event):
        self.x = event.x
        self.y = event.y
        self.movement()
        
    def callback2(self, event):
        # print("The last position was: (%d,%d)" % (self.x, self.y))
        # self.released = True
        self.stop_move = True
        self.var.set(True)
        
    def get_center(self):
        self.movement()
        
        self.master.wait_variable(self.var)
        # print("You've got the center: (%d, %d)" % (self.x+self.radius, self.y+self.radius))
        return (self.x+self.radius, self.y+self.radius)
        