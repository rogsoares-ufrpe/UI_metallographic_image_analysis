
# -*- coding: utf-8 -*-
"""
UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
UNIDADE ACADÊMICA DO CABO DE SANTO AGOSTINHO - UACSA

@author(s):
    Rogério Soares (rogerio.soaress@ufrpe.br)
    
Created on Sun Apr 19 12:14:33 2020
"""

import tkinter as tk

class ManagerPosition:
    """Esta classe serve para auxiliar na criação da circunferencia usada como
    ferramenta de interceptação de grãos. Através desta, é possível posicionar
    a circunferência onde se deseja pelo movimento do mouse. Ao clicar, a po-
    sição é fixada e o procedimento de contagem de grão é iniciado automaticamente."""
    
    def __init__(self, window, radius, width, height):     
        
        self.var = tk.BooleanVar()
        self.var.set(False)
        
        self.Canvas = window.MainCanvas
        self.x = 5
        self.y = 5
        self.x_old = self.x
        self.y_old = self.y
        self.radius = radius
        self.hilliard_circle = self.Canvas.create_oval(0, 0, 2*self.radius, 2*self.radius, width=2, outline="red")
        self.stop_move = True
        
        self.width = width
        self.height = height
        
        self.Canvas.bind("<Motion>",          lambda e: self.callback_pointermovement(e))
        self.Canvas.bind("<ButtonRelease-1>", lambda e: self.callback_stopmovement(e))
    
    def movement(self):
        """
        As mouse pointer moves, take the circle along. 
        """
        
        # do not allow any movement after mouse click
        if self.stop_move:
            x = self.x - self.x_old
            y = self.y - self.y_old
            self.Canvas.move(self.hilliard_circle, x, y) 
            # print("%d, %d" % (x,y))
            self.x_old = self.x
            self.y_old = self.y
        
    def callback_pointermovement(self, event):
        """Get pointer position as it move over image"""
        
        self.x = event.x + 5 - self.radius
        self.y = event.y + 5 - self.radius
        # print("x = {:.2f}, y = {:.2f}".format(event.x,event.y))
        self.movement()
        
    def callback_stopmovement(self, event):
        """Stops movement when mouse button was click"""
        
        self.stop_move = False
        self.var.set(True)
        self.x = event.x
        self.y = event.y
        
    def get_center(self):
        self.movement()
        
        self.Canvas.wait_variable(self.var)
        
        print("x = {:.2f}, y = {:.2f}".format(self.x-55, self.y-55))
        return [self.x-55, self.y-55]

       
def procedure(window, child_procedure, image_analyzer, cmanager, ps):
    """When the grain shape is not equiaxed but is distorted
    by deformation or other processes, obtaining an average lineal
    intercept value using straight test lines requires averaging of
    values made at a variety of orientations. If this is not done
    carefully, bias may be introduced. Use of a circle as the test line
    eliminates this problem as the circle will test all orientations
    equally and without bias."""
    

    MainWindow = window
    
    # Permite escolher a posição do centro da circunferência e seu raio movendo
    # o cursor sobre a imagem da amostra a ser analisada.
    global width, height
    width, height = image_analyzer.get_image_dimensions()
    
    # Obetenha o diametro da circunferencia da caixa de entrada
    D = int(child_procedure.HilliardCircunferenceDiameterEntry.get())
    radius = int(D/2)
    
    mp = ManagerPosition(MainWindow, radius, width, height)
    center = mp.get_center()
    
    circunference = [radius, center]
    
    intcpd_contours = []    
    
    # Loop over all grains and find: inetrcepted and inside circle
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    for cnt in image_analyzer.grains_contours:

        # STEP 1: Highlight grains contours intercepted by the cicle
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        ret = ps.circunference_contour_test(cnt, center, radius)
        if ret==0:            
            intcpd_contours.append(cnt)
            

    if  len(intcpd_contours) == 0:
        strg = "No grains intercepted!"
        tk.messagebox.showerror("Error",strg)
        return None
        
    colors = image_analyzer.colors
    image_analyzer.draw_contours(contours=intcpd_contours, contour_color=colors.black, area_color = colors.green_light)
    cmanager.update(image_analyzer)
    ps.draw_circunference(mp.Canvas, circunference)
    
    return intcpd_contours
    
    
    