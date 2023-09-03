import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


# read image
# img = cv.imread('images/reference_volume_fraction/Fig2b-aux.jpg')
# img = cv.imread('images/reference_volume_fraction/Fig2c.jpg')

img = np.zeros((100, 100, 3), dtype=np.uint8)
print(img.shape)

img[:,:,2]=255


# converte image to gray scale
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# remove noises from the thresholded image
kernel = np.ones((5,5),np.float32)/25
median = cv.medianBlur(img,7)

# calculate histogram of original gray scaled image before and after noise reduction
hist_img = cv.calcHist([img],[0],None,[256],[0,256])
hist_median = cv.calcHist([median],[0],None,[256],[0,256])


# apply threshold over filtered image
ret, thres_image = cv.threshold(img,115,255,cv.THRESH_BINARY)


# calculates histogram and normalize it
hist_th = cv.calcHist([thres_image],[0],None,[256],[0,256])
hist_thres = 100*hist_th/np.sum(hist_th)

# calculate percentage
fase1 = hist_thres[0]
fase2 = 100-fase1
print(" Fases: %.2f%%, %.2f%% " % (fase1, fase2))


fig1 = plt.figure(dpi=300)

# plot original gray scales before filter
ax1 = fig1.add_subplot(221)
ax1.imshow(img, 'gray')
ax1.axis('off')  # clear x-axis and y-axis
ax1.set_title("Original", fontsize=5)

# plot original image filtered (noise reduction)
ax3 = fig1.add_subplot(222)
ax3.imshow(median, 'gray')
ax3.axis('off')  # clear x-axis and y-axis
ax3.set_title("Original: afetr filter", fontsize=5)
ax3.tick_params(labelsize=4)


# plot histograms
ax4 = fig1.add_subplot(223)
ax4.plot(hist_img, label="original")
ax4.plot(hist_median, label="filtered")
ax4.legend(fontsize=5)
# ax4.set_title("Threshold Img filtered", fontsize=5)
ax4.grid(True)
ax4.tick_params(labelsize=4)

# plot thrseholdes image
ax2 = fig1.add_subplot(224)
ax2.imshow(thres_image, 'gray')
ax2.axis('off')  # clear x-axis and y-axis
ax2.set_title("Thresholded Img", fontsize=5)
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 6,
        }

ax2.text(400, 1500, r'$\alpha:$'+'{:.2f}%'.format(fase1[0]) + r'  $\beta:$'+'{:.2f}%'.format(fase2[0]), fontdict=font)




# SFI
plt.show()