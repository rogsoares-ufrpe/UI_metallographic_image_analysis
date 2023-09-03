# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:32:31 2020

@author: roger
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


filename = "Fig2b-cut.jpg"
img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mask = np.zeros(img.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
#pixelpoints = cv.findNonZero(mask)


# h, w = img.shape
# row_mean = 0
# for row in range(h):
#     pixels = np.array(img[row, :], dtype='int64')
#     row_mean += np.mean(pixels)

# print("Mean pixels: ", float(row_mean/h))

# segment = np.array(img[h-240, 500:700], dtype='int64')
# plt.plot(segment)
# plt.show()
# print(segment)
# print("Mean segment: ", np.mean(segment))
