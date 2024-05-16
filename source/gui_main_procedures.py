# # -*- coding: utf-8 -*-
# """
# Created on Tue Apr 23 19:13:33 2024

# @author: Rogério Soares

# O propósito deste arquivo visa não concentrar muitas linhas de código em 
# gui_main_2_support.py. Isto torna a leitura e manutenção do programa mais
# ágil permitindo identificar erros em menos tempo de trabalho.

# """

# import sys
# sys.path.append('procedures')
# import sys
# sys.path.append('../source')
# import geometry as geo
# import procedures_support as ps


# import Jeffries, Heyns, Hilliard, Abrams

# def apply(MainWindow, root, child_procedure, cmanager, image_analyzer):
#     """Apply ASTM procedure choose by user"""
    
#     print("Apply ASTM procedure choose by user")
    
#     var = int(child_procedure.RB_procedure.get())
#     procedures = ["None", "Jeffries", "Heyns", "Hilliard", "Abrams"]
#     print("Procedure: ", procedures[var])
    
#     canvas = MainWindow.MainCanvas    
#     image_analyzer.image_cv = None
#     image_analyzer.image_cv = image_analyzer.image_original.copy()
    
#     if procedures[var] == "Jeffries":
#        Jeffries.procedure(image_analyzer, cmanager, canvas, geo, ps)
       
#     elif procedures[var] == "Heyns":
#         Heyns.procedure(image_analyzer, child_procedure, cmanager, canvas, geo, ps)
        
#     elif procedures[var] == "Hilliard":
#         Hilliard.procedure(MainWindow, child_procedure, image_analyzer, cmanager, geo, ps)
    
#     elif procedures[var] == "Abrams":
#         Abrams.procedure(image_analyzer, cmanager, canvas, geo, ps)
        