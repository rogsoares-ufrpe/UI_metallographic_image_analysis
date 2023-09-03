# -*- coding: utf-8 -*-
"""
UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
UNIDADE ACADÊMICA DO CABO DE SANTO AGOSTINHO - UACSA

@author(s):
    Rogério Soares (rogerio.soaress@ufrpe.br)
    
Created on Sun Apr 19 12:14:33 2020
"""

# import numpy as np
import cv2
import geometry as geo
import gui_HSCI as rgui
from tkinter import messagebox as msgbox
import tkinter as tk
import moving_circle
        
    
def procedure(width, height, image_analyzer, window, root):
    radius = get_radius(window, root, width, height)
    msgbox.showinfo("Single circle definition", "Move the mouse cursor over the "
                    "image to place the circunference. Then, click once to start "
                    "the grain segmentation")
    
    # coordinates relative to the main window
    center = get_center(radius, window, root, width, height)
    
    # relative to image, we should subtract canvas offset axis-x 55 and xis-y 55
    c = [center[0] - 55, center[1] - 55]
    
    image_analyzer.find_grains()
    image_analyzer.image_cv, intercepted_grains_list = Hilliard(image_analyzer.image_cv, image_analyzer.grains_contours, image_analyzer.grains_area, width, height, c, radius)
    image_analyzer.set_image_for_canvas(image_analyzer.image_cv)    
    window.Canvas1.create_image(55, 55, image=image_analyzer.image_canvas, anchor=tk.NW)    
    
    # for drawing circunference, keep the first center captured
    geo.draw_circle(center, radius, window, offset=False)
    
    return intercepted_grains_list

def Hilliard(image_cv, grains_contours, grains_area, width, height, center, radius):
    
    # inside_grains_list = []
    intercepted_grains_list = []    
    
    # Loop over all grains and find: inetrcepted and inside circle
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    for area, cnt in zip(grains_area, grains_contours):

        # STEP 1: Highlight grains contours intercepted by the cicle
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        ret = geo.circunference_conttour_test(cnt, center, radius)
        if ret==0:
            color = geo.yellow
            # Fill with YELLOW color intercepted grains
            cv2.drawContours(image_cv, [cnt], 0, color, thickness=cv2.FILLED)
            # Contours of intercepted grains is BLACK
            cv2.drawContours(image_cv, [cnt], 0, geo.black, thickness=1)
            intercepted_grains_list.append(area)

    # print("Number of grains intercepted: %d" % len(intercepted_grains_list))
    return image_cv, intercepted_grains_list


def get_radius(window, root, width, height):
    hilliard = rgui.Hilliard(width, height)
    
    # open dialog window to get circunference radius
    top = rgui.create_Toplevel_HSCP(window, hilliard)
    root.wait_window(top.w)
    
    return hilliard.get_radius()
    

def get_center(radius, window, root, width, height):
    gfg = moving_circle.MCAI(radius, width, height, window.Canvas1, root)
    return gfg.get_center()
    
    



    