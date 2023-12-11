import cv2
import numpy as np

img = 255*np.ones([600,600], np.uint8)

# Green color in BGR 
color = (0, 255, 0) 
  
# Line thickness of 9 px 
thickness = 2

N = 32
delta = int(512/N)
# print('delta: ', delta)

offset=40

for i in range(0, 512, delta):
    # print("i = ", i)
    image = cv2.line(img, (0+offset,i+offset), (512+offset,i+offset), color, thickness)
    image = cv2.line(img, (i+offset,0+offset), (i+offset,512+offset), color, thickness)
image = cv2.line(img, (0+offset,512+offset), (512+offset,512+offset), color, thickness) 
image = cv2.line(img, (512+offset,0+offset), (512+offset,512+offset), color, thickness) 


filename = "../images/calibracao_" + str(N) + "X" + str(N) + ".jpg"
cv2.imwrite(filename, img) 

# Displaying the image  
cv2.imshow("window_name", image) 

cv2.waitKey(0)
cv2.destroyAllWindows()

