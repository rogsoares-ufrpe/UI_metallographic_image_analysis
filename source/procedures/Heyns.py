
# -*- coding: utf-8 -*-
"""
UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
UNIDADE ACADÊMICA DO CABO DE SANTO AGOSTINHO - UACSA

@author(s):
    Rogério Soares (rogerio.soaress@ufrpe.br)
    
Created on Fri Apr 17 21:50:27 2020
"""
import cv2

def procedure(image_analyzer, child_procedure, cmanager, canvas, ps):
    """
    Estimate the average grain size by counting (on the ground-glass screen, on
    a photomicrograph of a representative field of the specimen, a monitor or on
    the specimen itself) the number of grains intercepted by one or more straight
    lines sufficiently long to yield at least 50 intercepts.
    """
    
    # check entry box for length. It is initialized with 0um
    # micrometer -> milimeter
    line_length = float(child_procedure.LineLength.get())
    num_lines = int(child_procedure.NumLinesHeyns.get())
    
    linelength_px = image_analyzer.image_prop.um_to_px(line_length)
    
    # Draw horizontal lines over image
    width, height = image_analyzer.get_image_dimensions()
    
    delta_h = int(height/(num_lines+1))
    x_left = int(0.5*(width - linelength_px))
    x_right = int(0.5*(width + linelength_px))  
    
    h = 0
    full_intercpt = []
    half_intercpt = []
   
    # k=0
    # stop = False
    for i in range(num_lines):
        h = h + delta_h
        
        for cnt in image_analyzer.grains_contours:
            x_box, y_box, w_box, h_box = cv2.boundingRect(cnt)
            x, y, w, hl = cv2.boundingRect(cnt)
            
            # k += 1
            # if k==369 and not stop:
            #     bbox.append( (x,y,w,hl) )
            #     stop=True
            
            # Grão na linha de ação da interceptação
            if y_box < h < y_box+h_box:
                
                # Verifique se o grao foi completamente interceptado
                if x_box >= x_left and x_box+w_box <= x_right:
                    full_intercpt.append(cnt)
                    
                # Verifique se o grão foi parcialmente interceptado
                # Não permita que mais de um grão seja considerado 1/2
                # interceptado pela ponta da mesma reta tanto a esquerda quando
                # a direita
                
                #                        -1: fora
                # cv2.pointPolygonTest =  0: em cima
                #                         1: dentro
                
                if x_box < x_left < x_box+w_box:
                    if cv2.pointPolygonTest(cnt, (x_left,h), False) >= 0:
                        half_intercpt.append(cnt)
                    
                if x_box < x_right < x_box+w_box:
                    if cv2.pointPolygonTest(cnt, (x_right,h), False) >= 0:
                        half_intercpt.append(cnt)
   
    colors = image_analyzer.colors
    image_analyzer.draw_contours(contours=full_intercpt, contour_color=colors.black, area_color = colors.magenta_light)
    image_analyzer.draw_contours(contours=half_intercpt, contour_color=colors.black, area_color = colors.green_light)
    
    # update canvas
    cmanager.update(image_analyzer)

    ps.draw_lines(canvas, width, height, linelength_px, nlines=num_lines)

    # calculate grain size number
    num_intcp = .5*len(half_intercpt) + len(full_intercpt)
    G = ps.get_G_number("Heyns", num_intcp, length=0.001*line_length*num_lines)
    print("Grain size number: %f  (Heyns procedure)" % G)
    
    return full_intercpt+half_intercpt

