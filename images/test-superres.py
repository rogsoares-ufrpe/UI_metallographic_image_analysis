# -*- coding: utf-8 -*-
"""
Created on ${date}

@author: %(Rogério Soares)s
"""


import cv2
import matplotlib.pyplot as plt


print('Version cv2', cv2.__version__)
# Read image
img = cv2.imread("microstructure-01.jpg")
plt.imshow(img[:,:,::-1])
plt.show()

sr = cv2.dnn_superres.DnnSuperResImpl_create()
 
path = "EDSR_x2.pb"
 
sr.readModel(path)
 
sr.setModel("edsr",4)
 
result = sr.upsample(img)
 
# Resized image
resized = cv2.resize(img,dsize=None,fx=4,fy=4)
 
plt.figure(figsize=(12,8))
plt.subplot(1,2,1)
# Original image
plt.imshow(img[:,:,::-1])
plt.subplot(1,2,2)
# SR upscaled
plt.imshow(result[:,:,::-1])

# plt.subplot(1,3,3)
# # OpenCV upscaled
# plt.imshow(resized[:,:,::-1])

plt.show()