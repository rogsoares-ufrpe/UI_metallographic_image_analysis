# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:57:00 2020

@author: roger
"""
import tkinter as tk

'''
CanvasManager constrols all modifications on the MainCanvas from tkinter MainWindow
'''
class CanvasManager:
    
    def __init__(self, canvas):
        # print("Construtor vazio")
        self.canvas = canvas
        self.canvas_id = None
        
    def update(self, image_analyzer):
        # update canvas
        
        cv_img = image_analyzer.image_cv            
        cimg = image_analyzer.set_image_for_canvas(cv_img)
        self.display_image_on_canvas(cimg)

    def display_image_on_canvas(self, img):
        """Called everytime image displayed on canvas is modified."""
        self.canvas_id = self.canvas.create_image(55, 55, image=img, anchor=tk.NW)
        
    '''
    Remove all graphical material from canvas. Make it new.
    '''
    def cleanup(self):
        print("Cleaning image...")
        self.canvas.delete('all')
        self.canvas.configure(background="#ffffd9")
    
    ''' 
    Define x-axis and y-axis for canvas
    
    Convert to millimeters: We are adopting a 72dpi resolution
    DPI = Dot Per Inches
    1 inch = 25,4mm
    For each 25.4mm there are 72 pixels, or 2.83464566929133 pixels/mm
    Converting from Pixels to mm: MM = 2.83464566929133*P
    global w
    self.canvas.delete('all')
    self.canvas.configure(background="#ffffd9")
    '''
    def draw_xy_axis(self, width, height, image_prop):
        
        # image off from canvas origin
        global x_origin, y_origin
        
        # to plot axis-x
        # ---------------------------------------------------------------------
        x_origin = 55
        y_origin = 40
    
        x_step = int(width/5)
        y_step = int(height/5)
        
        # x axis
        x_axis_length = width + x_origin
        self.canvas.create_line(x_origin, y_origin, x_axis_length, y_origin, fill="black")
    
        l = int(x_step/2)
        # create ticks and labels
        for pos in range(0, x_axis_length-l, l):
            self.canvas.create_line(x_origin+pos, y_origin, x_origin+pos, y_origin-3, fill="black")
    
        
        for pos in range(0, x_axis_length, x_step):
            self.canvas.create_line(x_origin+pos, y_origin, x_origin+pos, y_origin-5, fill="black")
            
            """Returns the integer part"""
            tick_label = str(image_prop.px_to_um(pos)//1)
            self.canvas.create_text(x_origin+pos, y_origin-10, text=tick_label, font=('Arial',8,'bold italic'))
            
    
        # to plot axis-y
        # ---------------------------------------------------------------------
        x_origin = 40
        y_origin = 55
        y_axis_length = height + y_origin
        self.canvas.create_line(x_origin, y_origin, x_origin, y_axis_length, fill="black")
        # create ticks
        l = int(y_step/2)
        for pos in range(0, y_axis_length-l, l):
            self.canvas.create_line(x_origin, y_origin+pos, x_origin-3, y_origin+pos, fill="black")
    
        for pos in range(0, y_axis_length, y_step):
            self.canvas.create_line(x_origin, y_origin+pos, x_origin-5, y_origin+pos, fill="black")
            
            """Returns the integer part"""
            tick_label = str(image_prop.px_to_um(pos)//1)
            self.canvas.create_text(x_origin-20, y_origin+pos, text=tick_label, font=('Arial',8,'bold italic'))