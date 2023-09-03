# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:32:31 2020

@author: roger
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


filename = "Fig2b.jpg"
img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = img.shape
# print(img.shape)

row = int(1.05*h/2)
start = (0, row)
end = (w, row)
thickness = 1
line_type = 8
cv2.line(img, start, end, (0, 175, 175), thickness, line_type)


pixels = img[row+1, :]
px = np.zeros(len(pixels))
for i in range(len(pixels)):
    px[i] = int(pixels[i])

length = len(px)
diff_values = np.zeros(length-1)
for i in range(length-1):
    diff_values[i] = px[i+1] - px[i]
    # print("pixels[%d] = %d, pixels[%d] = %d" % (i+1, px[i+1], i, px[i]))

# print(px[:length])
# print(diff_values)

plt.plot(diff_values, 'kd',  markersize=2)
plt.xscale("log")
plt.show()

cv2.imshow("Thresholded image",img)
cv2.waitKey(0)