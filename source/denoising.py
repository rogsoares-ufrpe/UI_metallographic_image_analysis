# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:03:32 2020

@author: roger
"""


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('images/nano2.jpg')
dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()