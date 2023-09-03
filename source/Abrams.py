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
            
    image_analyzer.find_grains()
    image_analyzer.image_cv = Abrams(image_analyzer.image_cv, image_analyzer.grains_contours, image_analyzer.grains_area, width, height, c, radius)
    image_analyzer.set_image_for_canvas(image_analyzer.image_cv)    
    window.Canvas1.create_image(55, 55, image=image_analyzer.image_canvas, anchor=tk.NW)    
    
    # for drawing circunference, keep the first center captured
    geo.draw_circle(center, radius, window, offset=False)
    
"""   """
def Abrams(image_cv, grains_contours, grains_area, width, height, center, radius):
    
    # each one store grains intercepted by the three concentrical circunferences
    C1_list = [] # outer
    C2_list = [] # mid
    C3_list = [] # inner

    sub_list1 = []
    sub_list2 = []
    
    yellow = (0, 255, 255)
    blue = (255, 0, 0)
    black = (0, 0, 0)
    
    center = ((int(width/2), int(height/2)))
    
    # Circles are: Circumference, mm, Diameter, mm
    #                 250.0           79.58
    #                 166.7           53.05
    #                  83.3           26.53
    #                -------
    #         Total   500.0
    
    # get lengths im mm and convert to pixels
    radius = [int(2.83464566929133*79.58/2.), int(2.83464566929133*53.05/2.), int(2.83464566929133*26.53/2.)]
    
    # Loop over all grains and find: inetrcepted and inside circle
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    for area, cnt in zip(grains_area, grains_contours):
        ret = geo.circunference_conttour_test(cnt, center, radius[0])
        if ret==0:
            C1_list.append(area)
            # Fill with YELLOW color intercepted grains
            cv2.drawContours(image_cv, [cnt], 0, yellow, thickness=cv2.FILLED)
            # Contours of intercepted grains is BLACK
            cv2.drawContours(image_cv, [cnt], 0, black, thickness=1)
        elif ret==1:
            sub_list1.append((area,cnt))
            
    for l in sub_list1:
        area = l[0]
        cnt = l[1]
        ret = geo.circunference_conttour_test(cnt, center, radius[1])
        if ret==0:
            C2_list.append(area)
            # Fill with YELLOW color intercepted grains
            cv2.drawContours(image_cv, [cnt], 0, yellow, thickness=cv2.FILLED)
            # Contours of intercepted grains is BLACK
            cv2.drawContours(image_cv, [cnt], 0, black, thickness=1)
        elif ret==1:
            sub_list2.append((area,cnt))
    
    sub_list1.clear()
    
    for l in sub_list2:
        area = l[0]
        cnt = l[1]
        ret = geo.circunference_conttour_test(cnt, center, radius[2])
        if ret==0:
            C1_list.append(area)
            # Fill with YELLOW color intercepted grains
            cv2.drawContours(image_cv, [cnt], 0, yellow, thickness=cv2.FILLED)
            # Contours of intercepted grains is BLACK
            cv2.drawContours(image_cv, [cnt], 0, black, thickness=1)
        elif ret==1:
            sub_list2.append((area,cnt))

    sub_list2.clear()
    print("Number of grains intercepted: %d" % len(intercepted_grains_list))
    return image_cv


def get_radius(window, root, width, height):
    hilliard = rgui.Hilliard(width, height)
    
    # open dialog window to get circunference radius
    top = rgui.create_Toplevel_HSCP(window, hilliard)
    root.wait_window(top.w)
    
    return hilliard.get_radius()
    

def get_center(radius, window, root, width, height):
    gfg = moving_circle.MCAI(radius, width, height, window.Canvas1, root)
    return gfg.get_center()
    
    



    