
# -*- coding: utf-8 -*-
"""
UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
UNIDADE ACADÊMICA DO CABO DE SANTO AGOSTINHO - UACSA

@author(s):
    Rogério Soares (rogerio.soaress@ufrpe.br)
    
Created on Fri Apr 17 22:24:12 2020
"""

import numpy as np
import cv2


yellow = (0, 255, 255)
blue = (255, 0, 0)
black = (0, 0, 0)
     

def circunference_contour_test(cnt, center, radius):
    """Returns -1, 0 or 1 if contour is outside, intercepted or inside circunference"""
    
    check = np.array([False, False, False, False])
    # Let (x,y) be the top-left coordinate of the rectangle and (w,h) be its width and height.
    x, y, w, h = cv2.boundingRect(cnt)
    
    bx1_p1 = (x, y)
    bx1_p2 = (x+w, y+h)
    d1 = dist(bx1_p1, center)
    d2 = dist(bx1_p2, center)
    
    bx2_p1 = (x+w, y)
    bx2_p2 = (x, y+h)
    d3 = dist(bx2_p1, center)
    d4 = dist(bx2_p2, center)

    # Box 1: top left corner and botton right corner are outside and inside circle, respectively.
    check[0] =  d1 > radius and  d2 < radius or d1 < radius and d2 > radius

    # Box 2: top right corner and botton left corner are outside and inside circle, respectively.
    if not check[0]:
        # check[1] =  d1 > radius and  d2 < radius or d1 < radius and  d2 > radius
        check[1] =  d3 > radius and  d4 < radius or d3 < radius and  d4 > radius

    # check if one of the box situations is true (grain is intercepted)
    if check[0] or check[1] and line_segment_intercept(cnt, center, radius):
        return 0
    else:
        bool_array = np.array([d1 < radius, d2 < radius, d3 < radius, d4 < radius])
        if np.count_nonzero(bool_array) >= 3 and not line_segment_intercept(cnt, center, radius):
            return 1
        else:
            return -1


def draw_circle2(circunference, window, offset=True):
        """Draws a circle over Canvas, not over image."""
        radius = circunference[0]
        center = circunference[1]
        delta = 55
        if not offset:
            delta=0
        x0 = center[0] - radius + delta
        y0 = center[1] - radius + delta
        x1 = center[0] + radius + delta
        y1 = center[1] + radius + delta
        window.Canvas1.create_oval(x0, y0, x1, y1, width=2, outline="red")


def draw_circle(center, radius, window, offset=True):
        """Draws a circle over Canvas, not over image."""
        delta = 55
        if not offset:
            delta=0
        x0 = center[0] - radius + delta
        y0 = center[1] - radius + delta
        x1 = center[0] + radius + delta
        y1 = center[1] + radius + delta
        window.Canvas1.create_oval(x0, y0, x1, y1, width=2, outline="red")
        

def line_segment_intercept(cnt, center, radius):
        isIntercept = False
        length = len(cnt)
        
        for pos in range(length-1):
            pt1 = cnt[pos][0]
            pt2 = cnt[pos+1][0]
            isIntercept = line_circle_intercept(pt1, pt2, center, radius)
            if isIntercept:
                break
        return isIntercept
    
    
def line_circle_intercept(pt1, pt2, center, radius):
    isIntercept = False
    x0 = center[0]
    y0 = center[1]
    R = radius
    
    x1 = pt1[0]
    y1 = pt1[1]
    x2 = pt2[0]
    y2 = pt2[1]
    
    a = x1 - x2
    b = x2 - x0
    c = y1 - y2
    d = y2 - y0
    
    A = a**2 + c**2
    B = 2*(a*b+c*d)
    C = b**2 + d**2 - R**2
    
    delta = B**2 - 4.*A*C
    if delta > 0:
        t1 = (-B + np.sqrt(delta))/(2.*A)
        t2 = (-B - np.sqrt(delta))/(2.*A)
        if 0 <= t1 <= 1 or 0 <= t2 <= 1:
            isIntercept = True
            
    return isIntercept


# def draw_intercepting_lines(nlines, line_length, width, height):
#     """Draw horizontal lines over image"""
#     h = 0
#     delta_h = int(height/(nlines+1))
#     for i in range(nlines):
#         h = h + delta_h
#         x0 = int(0.5*(width - line_length)) + 55
#         y0 = h + 55
#         x1 = int(0.5*(width + line_length)) + 55
#         y1 = h + 55
#         # window.Canvas1.create_line(x0, y0, x1, y1, width=2, fill="red")
        
        
# def draw_intercepting_lines(start_points, end_points, window):
#     """Draw horizontal lines over image"""
#     for i in range( len(start_points) ):
#         pt1 = start_points[i]
#         pt2 = end_points[i]
#         window.Canvas1.create_line(pt1[0], pt1[1], pt2[0], pt2[1], width=2, fill="red")


def dist(p1, p2):
    return np.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )
