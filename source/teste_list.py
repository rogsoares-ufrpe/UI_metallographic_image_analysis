# -*- coding: utf-8 -*-
"""
UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
UNIDADE ACADÊMICA DO CABO DE SANTO AGOSTINHO - UACSA

@author(s):
    Rogério Soares (rogerio.soaress@ufrpe.br)
    
Created on Wed May 13 19:58:20 2020
"""

import numpy as np

contours = []
cnt = np.array([[0,1],[1,0],[20,0],[21,1],[18 ,4],[18,6],[16,8],[16,9],[15,10],[15,11],[14,12],[14,13],[13,14],[13,17],[12,18],[12,26],[10,28],[10,29],[9,30],[1,30],[0,29]])

contours.append(cnt)

print("contours length: ", len(contours))
for c in contours:
    print("cnt length: ", len(c))
    for k in c:
        print(k)
        
        
        
