# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:53:06 2020

@author: roger_000
"""

# Canvas class of Tkinter supports a functions which is used to move objects 
# from one position to another in any canvas or tkinter toplevel.
# Syntax: Canvas.move(canvas_object, x, y)

# imports every file form tkinter and tkinter.ttk 
from tkinter import *
# import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import cv2

class GFG: 
    def __init__(self, master = None): 
        self.master = master 
        self.x = 5
        self.y = 5
        self.x_old = self.x
        self.y_old = self.y
        
        self.canvas = Canvas(master) 
        self.image_original = cv2.imread("images/microstructure-02.jpg")    
        self.image_canvas = cv2.cvtColor(self.image_original, cv2.COLOR_BGR2RGB)
        self.image_canvas = Image.fromarray(self.image_canvas)
        self.image_canvas = ImageTk.PhotoImage(self.image_canvas)
        self.canvas.create_image(0,0, image=self.image_canvas, anchor=NW)
         
        self.circle = self.canvas.create_oval(5,5,100,100, outline="red")
        self.canvas.pack()
        
        self.stop_move = False
        self.movement() 
      
    def movement(self):
        if not self.stop_move:
            x = self.x - self.x_old
            y = self.y - self.y_old 
            self.canvas.move(self.circle, x, y) 
            print("%d, %d" % (self.x, self.y))
            self.x_old = self.x
            self.y_old = self.y
        
    def callback(self, event):
        self.x = event.x
        self.y = event.y
        self.movement()
        
    def callback2(self, event):
        self.stop_move = True
        print("The last position was: (%d,%d)" % (self.x, self.y))
    
    
if __name__ == "__main__":
    
    master = Tk() 
    gfg = GFG(master)
    master.bind("<Motion>", lambda e: gfg.callback(e))
    master.bind("<ButtonRelease-1>", lambda e: gfg.callback2(e))
    
    mainloop()
    