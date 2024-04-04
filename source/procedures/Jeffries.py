# -*- coding: utf-8 -*-

"""
UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
UNIDADE ACADÊMICA DO CABO DE SANTO AGOSTINHO - UACSA

@author(s):
    Rogério Soares (rogerio.soaress@ufrpe.br)
    
Created on Fri Apr 17 21:39:12 2020
"""

import numpy as np
import cv2

import sys
sys.path.append('../source')
import geometry as geo

def jeffries_procedure(circunference, grains_area, grains_contours):
    """
    Planimetric Procedure—The planimetric method involves an actual count
    of the number of grains within a known area. The number of  grains per
    unit area, NA , is used to determine the ASTM grain size number, G. The 
    precision of the method is a function of the number of grains counted. 
    A precision of 60.25 grain size units can be attained with a reasonable
    amount of effort. Results are free of bias and repeatability and reproduci-
    bility are less than 60.5 grain size units. An accurate count does require
    marking off of the grains as they are counted. Standard Test Methods for 
    Determining Average Grain Size
    """
    
    intcpd_area = []
    intcpd_contours = []
    inside_area = []    
    inside_contours = []
    
    # First of all, inscribe a circle (or rectangle) of known area 
    # (usually 5000 mm2 to simplify the calculations) on a micrograph image 
    radius = circunference[0]
    center = circunference[1]       # center coordinates
    
    # check = np.array([False, False, False, False])
    
    
    # Loop over all grains and find:
        # 1. the intercepted by the circunference
        # 2. grains inside inside the circunference        
    for area, cnt in zip(grains_area, grains_contours):

        # STEP 1: Highlight grains contours intercepted by the cicle
        ret = geo.circunference_contour_test(cnt, center, radius)
        # print('ret = ', ret)
        
        
        if ret==-1:
            continue
        
        if ret==0:
            # over line circunference
            # color = geo.blue
            intcpd_area.append(area)
            intcpd_contours.append(cnt)
        else:
            inside_area.append(area)
            inside_contours.append(cnt)
    
    # print('Procedimento de Jeffries:')
    # print('Graos interceptados: ', len(intcpd_area))
    # print('Graos internos: ', len(inside_area))
    
    return intcpd_area, inside_area, intcpd_contours, inside_contours
    
def draw_Jeffries_grains(intercepted_grains_list, inside_grains_list, image_cv):
    """After the intercepted and inside grains have been detected, fill them with colors."""
    
    yellow = (0, 255, 255)
    for i in range(len(intercepted_grains_list)):
        cv2.drawContours(image_cv, 
                         [intercepted_grains_list[i]], 
                         -1, 
                         yellow, 
                         thickness = cv2.FILLED)
    cian =  (255, 255, 0)    
    for i in range(len(inside_grains_list)):
        cv2.drawContours(image_cv, 
                         [inside_grains_list[i]], 
                         -1, 
                         cian, 
                         thickness = cv2.FILLED)
    
    # image_analyzer.set_image_for_canvas(image_analyzer.image_cv)
    # window.Canvas1.create_image(55, 55, image=image_analyzer.image_canvas, anchor=tk.NW)
    # geo.draw_circle2(circunference, window)

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
    

# def run_jeffries_analysis(image_analyzer, window, image_prop):
#     """Jeffries procedure is applied N times to the same image for different
#     patterns. For each one, a G number is calculated and then an histogram built.
#     N - number of tests"""
    
#     "The ASTM article E-112 suggests a circunfence of 5000mm2 which gives R=39,894228mm"
#     ret = image_analyzer.find_grains()
#     if ret==-1:
#         return
    
#     width, height = image_analyzer.get_image_dimensions()
    
#     # number of tests field
#     n = 60
#     n_bins = int(n/5)
#     w_offset = int(image_prop.width*0)
#     h_offset = int(image_prop.height*0)
    
#     # R = get_radius(image_prop)
#     R = image_prop.um_to_px(39894.228/image_prop.M)
    
#     "Define the region where the center of circunference can be placed."
#     "W: {(x,y): w_offset+R <= x <= width - R - w_offset, h_offset+R <= y <= height - R - h_offset"
#     w_lower = w_offset + R
#     w_upper = image_prop.width - (R + w_offset)
#     h_lower = h_offset + R
#     h_upper = image_prop.height - (R + h_offset)
    
#     # define and initialize circunference
#     circunference = [R, (0,0)]
    
#     G_arr = np.zeros(n)
#     for i in range(n):
#         x = random.randint(w_lower, w_upper)
#         y = random.randint(h_lower, h_upper)
#         circunference[1] = (x,y)
        
#         in_list, inter_list = Jeffries(image_analyzer, circunference)
#         N_inside = len(in_list)
#         N_inter = len(inter_list)
#         # print("grains %d (inside) %d (intercepted)" % (N_inside, N_inter ))
#         Na, A_mean, d_mean, G = get_grain_size_related_parameters(N_inside, N_inter, 
#                                                                   image_prop)
#         # print(G)
#         G_arr[i] = G

#         geo.draw_circle((x,y), R, window)
#         in_list.clear()
#         inter_list.clear()
        
#     return G_arr, n_bins


# def get_radius(image_prop):
#     """Get radius in pixels based on the image scale provided"""
    
#     # Circunference radius over image should have 39.9mm. This value will be 
#     # converted to thw real area through Magnification applied:
#     print("Magnification: ", image_prop.M)
#     radius = 39894.228/image_prop.M
    
#     # Let's convert this value to pixels
#     return image_prop.um_to_px(radius)


