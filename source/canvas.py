# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:57:00 2020

@author: roger
"""
import tkinter as tk

def update(window, image_analyzer):
    """Called everytime image displayed on canvas is modified."""
    window.Canvas1.create_image(55, 55, image=image_analyzer.image_canvas, anchor=tk.NW)   
    


def setup(window, image_analyzer, image_prop):
    """ Set up canvas cleaning it and creating x-y axis  """

    # Convert to millimeters: We are adopting a 72dpi resolution
    # DPI = Dot Per Inches
    # 1 inch = 25,4mm
    # For each 25.4mm there are 72 pixels, or 2.83464566929133 pixels/mm
    # Converting from Pixels to mm: MM = 2.83464566929133*P
    global w
    window.Canvas1.delete('all')
    window.Canvas1.configure(background="#ffffd9")
    "Define x-axis and y-axis for canvas"
    
    
    width, height = image_analyzer.get_image_dimensions()
    
    # image off from canvas origin
    global x_origin, y_origin
    
    # to plot axis-x
    # ************************************************************************
    x_origin = 55
    y_origin = 40

    x_step = int(width/5)
    y_step = int(height/5)
    
    # x axis
    x_axis_length = width + x_origin
    window.Canvas1.create_line(x_origin, y_origin, x_axis_length, y_origin, fill="black")

    l = int(x_step/2)
    # create ticks and labels
    for pos in range(0, x_axis_length-l, l):
        window.Canvas1.create_line(x_origin+pos, y_origin, x_origin+pos, y_origin-3, fill="black")

    
    for pos in range(0, x_axis_length, x_step):
        window.Canvas1.create_line(x_origin+pos, y_origin, x_origin+pos, y_origin-5, fill="black")
        
        """Returns the integer part"""
        tick_label = str(image_prop.px_to_um(pos)//1)
        window.Canvas1.create_text(x_origin+pos, y_origin-10, text=tick_label, font=('Arial',8,'bold italic'))
        

    # to plot axis-y
    # ************************************************************************
    x_origin = 40
    y_origin = 55
    y_axis_length = height + y_origin
    window.Canvas1.create_line(x_origin, y_origin, x_origin, y_axis_length, fill="black")
    # create ticks
    l = int(y_step/2)
    for pos in range(0, y_axis_length-l, l):
        window.Canvas1.create_line(x_origin, y_origin+pos, x_origin-3, y_origin+pos, fill="black")

    for pos in range(0, y_axis_length, y_step):
        window.Canvas1.create_line(x_origin, y_origin+pos, x_origin-5, y_origin+pos, fill="black")
        
        """Returns the integer part"""
        tick_label = str(image_prop.px_to_um(pos)//1)
        window.Canvas1.create_text(x_origin-20, y_origin+pos, text=tick_label, font=('Arial',8,'bold italic'))
    
    window.Label_FNP.configure(text=image_analyzer.path)
    window.Canvas1.create_image(55, 55, image=image_analyzer.image_canvas, anchor=tk.NW)
    
    # update magnification entry
    window.Entry_Magnification.delete(0, 'end')
    window.Entry_Magnification.insert(0,str(image_prop.M))
    
    # update label for scale
    # window.Label5.delete(0,'end')
    window.Label5.configure(text="Scale: " + str(image_prop.er)+u'''\u03BC'''+'''m''')


# def convert_pixel_to_mm(pixel):
#     """Returns the integer part"""
#     global pixels_mu_ratio
#     a = float(pixel/pixels_mu_ratio)
#     return a//1