# -*- coding: utf-8 -*-
"""
UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
UNIDADE ACADÊMICA DO CABO DE SANTO AGOSTINHO - UACSA

@author(s):
    Rogério Soares (rogerio.soaress@ufrpe.br)
    
Created on Sun Apr 19 12:14:33 2020

===============================================================================
ASTM E112 − 12

Abrams Three-Circle Procedure:
    
    The test pattern consists of three concentric and equally spaced circles 
    having a total circumference of 500 mm.
    
    Circles are: Circumference, mm, Diameter, mm
                    250.0           79.58
                    166.7           53.05
                     83.3           26.53
                   -------
            Total   500.0
===============================================================================
"""

def procedure(image_analyzer, cmanager, canvas, ps):
    
    # Each list stores the grains intercepted by one of the three concentrical 
    # circle
    intcpd_contours = [[], [], []]    
    
    # The circles are centered at the middle of image
    width, height = image_analyzer.get_image_dimensions()
    center = ((int(width/2), int(height/2)))   
    radius = image_analyzer.image_prop.Abrams_radius()
    
    # Loop over all grains and find: inetrcepted and inside circle
    for i, r in enumerate(radius):
        for cnt in image_analyzer.grains_contours:
            ret = ps.circunference_contour_test(cnt, center, r)
            if ret==0:            
                intcpd_contours[i].append(cnt)
                
    colors = image_analyzer.colors
    magenta = [colors.magenta_light1, colors.magenta_light2, colors.magenta_light3]
    
    for idx, cnt_list in enumerate(intcpd_contours):
        # print("Number of intercepted grains: ", len(cnt_list))
        image_analyzer.draw_contours(contours=cnt_list, 
                                     contour_color=colors.black, 
                                     area_color = magenta[idx])
    
    cmanager.update(image_analyzer)    
    
    ps.draw_circunference(canvas, [radius[0], center])
    ps.draw_circunference(canvas, [radius[1], center])
    ps.draw_circunference(canvas, [radius[2], center])
    
    return intcpd_contours[0]+intcpd_contours[1]+intcpd_contours[2]

