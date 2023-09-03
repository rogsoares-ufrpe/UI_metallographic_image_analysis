# -*- coding: utf-8 -*-
"""
UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
UNIDADE ACADÊMICA DO CABO DE SANTO AGOSTINHO - UACSA

@author(s):
    Rogério Soares (rogerio.soaress@ufrpe.br)
    
Created on Fri Apr 17 21:39:12 2020
"""

import tkinter as tk
# from tkinter import messagebox as msgbox
import numpy as np
import cv2
import geometry as geo
import random


def procedure(image_analyzer, window, image_prop):
    width, height = image_analyzer.get_image_dimensions()
    
    r_px = get_radius(image_prop)
    #circunference at image center
    circunference = [r_px, ((int(width/2), int(height/2)))]
    
    image_analyzer.find_grains()
    inside_list, intercepted_list = Jeffries(image_analyzer, circunference)
    image_analyzer.set_image_for_canvas(image_analyzer.image_cv)
    window.Canvas1.create_image(55, 55, image=image_analyzer.image_canvas, anchor=tk.NW)
    geo.draw_circle2(circunference, window)
    return inside_list, intercepted_list

"""
        Planimetric Procedure—The planimetric method involves an actual count of the number of grains within a known
area. The number of  grains per unit area, NA , is used to determine the ASTM grain size number, G. The precision of
the method is a function of the number of grains counted. A precision of 60.25 grain size units can be attained with a
reasonable amount of effort. Results are free of bias and repeatability and reproducibility are less than 60.5 grain size
units. An accurate count does require marking off of the grains as they are counted.
Standard Test Methods for Determining Average Grain Size
        """
def Jeffries(image_analyzer, circunference):
    
    inside_grains_list = []
    intercepted_grains_list = []
    
    # First of all, inscribe a circle (or rectangle) of known area (usually 5000 mm2 to simplify the calculations) on a micrograph image 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    radius = circunference[0]
    center = circunference[1]       # center coordinates
    
    # check = np.array([False, False, False, False])
    
    
    # Loop over all grains and find: inetrcepted and inside circle
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    for area, cnt in zip(image_analyzer.grains_area, image_analyzer.grains_contours):

        # STEP 1: Highlight grains contours intercepted by the cicle
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        ret = geo.circunference_conttour_test(cnt, center, radius)
        if ret==-1:
            continue
        
        # inside color
        color = geo.yellow
        
        if ret==1:
            # over line circunference
            color = geo.blue
            intercepted_grains_list.append(area)
        else:
            inside_grains_list.append(area)
            
        
        # Fill with YELLOW color intercepted grains
        cv2.drawContours(image_analyzer.image_cv, [cnt], 0, color, thickness=cv2.FILLED)
        # Contours of intercepted grains is BLACK
        cv2.drawContours(image_analyzer.image_cv, [cnt], 0, geo.black, thickness=1)

    return inside_grains_list, intercepted_grains_list


def get_grain_size_related_parameters(N_inside, N_intercepted, M):
    """
    N_inside      - Number of grains inside circunferene
    N_intercepted - NUmber of grains intercepted by circunference
    
    Returns:
        Na      - number of grains per mm2
        A_mean  - mean grain area
        d       - mean grain diamenter
        G       - ASTM grain size number
    """

    f = 0.0002*M                            # Jeffries multiplier
    Na = f*(N_inside + 0.5*N_intercepted)    # Number of grains per square millimetre
    A_mean = 1/Na
    d_mean = np.sqrt(A_mean)
    G = 3.321928*np.log10(Na) - 2.954
    
    return Na, A_mean, d_mean, G
    

def run_jeffries_analysis(image_analyzer, window, image_prop):
    """Jeffries procedure is applied N times to the same image for different
    patterns. For each one, a G number is calculated and then an histogram built.
    N - number of tests"""
    
    "The ASTM article E-112 suggests a circunfence of 5000mm2 which gives R=39,894228mm"
    ret = image_analyzer.find_grains()
    if ret==-1:
        return
    
    width, height = image_analyzer.get_image_dimensions()
    
    # number of tests field
    n = 60
    n_bins = int(n/5)
    w_offset = int(image_prop.width*0)
    h_offset = int(image_prop.height*0)
    
    R = get_radius(image_prop)
    
    "Define the region where the center of circunference can be placed."
    "W: {(x,y): w_offset+R <= x <= width - R - w_offset, h_offset+R <= y <= height - R - h_offset"
    w_lower = w_offset + R
    w_upper = image_prop.width - (R + w_offset)
    h_lower = h_offset + R
    h_upper = image_prop.height - (R + h_offset)
    
    # define and initialize circunference
    circunference = [R, (0,0)]
    
    G_arr = np.zeros(n)
    for i in range(n):
        x = random.randint(w_lower, w_upper)
        y = random.randint(h_lower, h_upper)
        circunference[1] = (x,y)
        
        in_list, inter_list = Jeffries(image_analyzer, circunference)
        N_inside = len(in_list)
        N_inter = len(inter_list)
        # print("grains %d (inside) %d (intercepted)" % (N_inside, N_inter ))
        Na, A_mean, d_mean, G = get_grain_size_related_parameters(N_inside, N_inter, image_prop)
        # print(G)
        G_arr[i] = G

        geo.draw_circle((x,y), R, window)
        in_list.clear()
        inter_list.clear()
        
    return G_arr, n_bins


def get_radius(image_prop):
    """Get radius in pixels based on the image scale provided"""
    
    # Circunference radius over image should have 39.9mm. This value will be convrted
    # to thw real area through Magnification applied:
    print("Magnification: ", image_prop.M)
    radius = 39894.228/image_prop.M
    
    # Let's convert this value to pixels
    return image_prop.um_to_px(radius)

