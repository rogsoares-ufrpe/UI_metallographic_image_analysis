# -*- coding: utf-8 -*-
"""
UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
UNIDADE ACADÊMICA DO CABO DE SANTO AGOSTINHO - UACSA

@author(s):
    Rogério Soares (rogerio.soaress@ufrpe.br)
    
Created on Fri Apr 17 21:50:27 2020
"""

import numpy as np
from tkinter import messagebox as msgbox
import tkinter as tk
import cv2
import geometry as geo


def procedure(width, height, image_analyzer, window):
    # print("Heyn_linear_Intercept(width, height, image_analyzer, gs_procedure, window):")
    nlines = int(window.Spinbox_number_lines.get())
    
    ll = float(window.Entry_line_length.get()) # get line legth
    line_length = int(2.83464566929133*ll)     # convert line length to pixels
    
    
    if line_length > width:
        msgbox.showerror("Invalid Value", "Line length value must be less than image width.")
    else:        
        # print("Number of lines: %d\nLength: %d mm" % (nlines, convert_pixel_to_mm(line_length)))
        image_analyzer.find_grains()
        image_analyzer.image_cv, intercepted_list = Heyn(image_analyzer.image_cv, image_analyzer.grains_contours, image_analyzer.grains_area, width, height, nlines, line_length)
        image_analyzer.set_image_for_canvas(image_analyzer.image_cv)
        window.Canvas1.create_image(55, 55, image=image_analyzer.image_canvas, anchor=tk.NW)
        start_points, end_points = create_horizontal_lines(width, height, nlines, line_length)
        geo.draw_intercepting_lines(start_points, end_points, window)
        return intercepted_list
        
        
def Heyn(image_cv, grains_contours, grains_area, width, height, nlines, line_length):
        """
        Intercept Procedure —The intercept method involves an actual count of the number of grains intercepted
        by a test line or the number of grain boundary intersections with a test line, per unit length of test
        line, used to calculate the mean lineal intercept length, ℓ¯. ℓ¯ is used to determine the ASTM grain 
        size number, G.
        """
        
        yellow = (0, 255, 255)
        blue = (255, 0, 0)
        black = (0, 0, 0)
        color = [black, blue, yellow]
        
        # List of grains intercepted
        intercepted_list = []
        
        # Draw horizontal lines over image
        h = 0
        delta_h = int(height/(nlines+1))
        x0 = int(0.5*(width - line_length))
        x1 = int(0.5*(width + line_length))
        j=0
        for i in range(nlines):
            h = h + delta_h
            
            grains_counter = 0
            # for each line, check which grains are intercepted by it highlight them
            # Loop over all grains and find: inetrcepted and inside circle
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            for area, cnt in zip(grains_area, grains_contours):
                
                leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
                rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
                bottommost = tuple(cnt[cnt[:,:,1].argmin()][0])
                topmost = tuple(cnt[cnt[:,:,1].argmax()][0])
               
                
               # Check if grain is completely intercepted by horizontal line
                check1 = bottommost[1] <= h <= topmost[1]
                check2 = x1 >= rightmost[0]
                check3 = x0 <= leftmost[0]
                if check1 and check2  and check3:
                    j = 2                
                # The leftmost/right end of straight test lines lies inside grains
                elif check1 and leftmost[0] < x0 < rightmost[0] or check1 and leftmost[0] < x1 < rightmost[0]:
                    # # check if grain contour is really intercepted by line
                    if cv2.pointPolygonTest(cnt,(x0,h),False) > 0:
                        j = 1
                    else:
                        continue
                else:
                    continue
                    
                grains_counter += 1
                intercepted_list.append(area)
                cv2.drawContours(image_cv, [cnt], 0, color[j], thickness=cv2.FILLED)
                cv2.drawContours(image_cv, [cnt], 0, black, thickness=1)
            
        return image_cv, intercepted_list
    
    
def create_horizontal_lines(width, height, nlines, line_length):
    h = 0
    delta_h = int(height/(nlines+1))

    start_points = []
    end_points = []
    
    x0 = int(0.5*(width - line_length)) + 55
    x1 = x0 + line_length
    
    for i in range(nlines):
        h = h + delta_h
        y0 = h + 55
        y1 = y0
        start_points.append((x0,y0))
        end_points.append((x1,y1))
        
    return start_points, end_points
