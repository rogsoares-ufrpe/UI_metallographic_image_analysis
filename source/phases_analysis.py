# -*- coding: utf-8 -*-
"""
Created on Tue May 26 23:57:25 2020

@author: roger
"""

import numpy as np
import cv2 as cv

import draw_double_circular_pattern as pattern
import canvas as cnvs
import threshold_gui as thresh_gui
import threshold_gui_support as thresh_support


class CIM:
    """confidence_interval_multiplier"""
    # TABLE 1 95 % Confidence Interval Multipliers

    def __init__(self):

        # From 5 to 39 fields
        self.table = np.array([0,0,0,0,0,2.776,2.571,2.447,
                            2.365, 2.306,2.262,
                            2.228, 2.201, 2.179,
                            2.160, 2.145, 2.131,
                            2.120, 2.110, 2.101,
                            2.093, 2.086, 2.080,
                            2.074, 2.069, 2.064,
                            2.060, 2.056, 2.052,
                            2.048, 2.045])

    def get(self, n_fields):
        if n_fields < 29:
            return self.table[n_fields]
        else:
            if 30 < n_fileds <= 40:
                return 2.020
            if 40 < n_fields <=60:
                return 2.000
            else:
                return 1.960


def start(root, window, canvas, image_analyzer):

    track = pattern.SinglePixel(root, image_analyzer.image_gray)    

    # image_analyzer.set_image_for_canvas(image_analyzer.image_gray)
    # cnvs.update(window, image_analyzer)

    # open window to create a binary window adjusting threshold values
    # thresh_gui.create_Toplevel1(root)

    # thresh_support.create_histogram_plot(image_analyzer.image_gray)
    # thresh_support.load_threshold_histogram()
    
    # image_cv = np.zeros(image_analyzer.image_gray.shape, np.uint8)
    # counter = 1
    # for k in [2, 4, 8, 16, 32, 64]:
    #     delta_w = int(image_analyzer.width/k)
    #     delta_h = int(image_analyzer.height/k)
    #     img = np.zeros((delta_h, delta_w), np.uint8)
        
    #     for i in range(k):
    #         from_h = i*delta_h
    #         to_h = from_h + delta_h
    #         for j in range(k):
    #             from_w = j*delta_w
    #             to_w = from_w + delta_w
    #             img = image_analyzer.image_gray[from_h:to_h, from_w:to_w]

    #             # perform an histogram equalization for better contrast
    #             img = cv.equalizeHist(img)
                
    #             # apply the threshold Otsu: thresh is set to 0 but it´s doesn´t matter
    #             # Otsu’s algorithm tries to find a threshold value (t) which minimizes 
    #             # the weighted within-class variance
    #             # Otsu's thresholding after Gaussian filtering
    #             img = cv.GaussianBlur(img, (5,5), 0)
    #             ret, img = cv.threshold(img, 0, 255, cv.THRESH_OTSU)
    
    #             # transpose block image to main frame
    #             image_cv[from_h:to_h, from_w:to_w] = img

    #     cv.imwrite("output-" + str(counter) + ".jpg", image_cv)
    #     counter += 1
    
    # # create a CLAHE object (Arguments are optional).
    # clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    # blur = cv.GaussianBlur(image_analyzer.image_gray, (5,5), 0)
    # cl1 = clahe.apply(blur)
    # cv.imwrite('clahe_image_gray.jpg',cl1)
    # print("Done!")
        
    # image_analyzer.set_image_for_canvas(image_cv)
    # cnvs.update(window, image_analyzer)

    
# # update binary image as user is setting parameters for threshold
    # while thresh_support.is_opened():

    #     # this function also sets a waiting point. one 'while' loop is only
    #     # completed when a different value for threshold is chosed. Otherwise,
    #     # any image update is performed
    #     thresh, maxval = thresh_support.get_parameters()
    #     print("thresh: %d, maxval: %d" % (thresh, maxval))

    #     numblocks = 2**thresh + 1
    #     print("Num blocks: ", numblocks)
        
    #     delta_w = int(image_analyzer.width/numblocks)
    #     delta_h = int(image_analyzer.height/numblocks)
    #     last_delta_w = image_analyzer.width -  (numblocks-1)*delta_w
    #     last_delta_h = image_analyzer.height -  (numblocks-1)*delta_h
        
    #     for i in range(numblocks):
    #         for j in range    
    #         # take a block from gray image
    #         from_w = i*delta_w
    #         to_w = from_w + delta_w
    #         from_h = i*delta_h
    #         to_h = from_h + delta_h
    #         img = image_analyzer.image_gray[from_w:to_w, from_h:to_h]
            
            
        
    #     # # apply image filters to obtain a binary image (black-white)
    #     # # image_analyzer.create_binary_image(image_analyzer.image_gray, thresh, maxval)

    #     # image_analyzer.binary_image = image_analyzer.image_cv.copy()
    #     # image_analyzer.binary_image[ image_analyzer.binary_image >= maxval] = 255
    #     # image_analyzer.binary_image[ image_analyzer.binary_image <= thresh] = 0

    #     # # # Get a tuple of unique values & their frequency in numpy array
    #     # uniqueValues, occurCount = np.unique(image_analyzer.binary_image, return_counts=True)

    #     # if len(uniqueValues)==2:
    #     #     print("Unique Values : " , uniqueValues)
    #     #     print("Occurrence Count : ", occurCount)
    #     #     white_perc = 100*occurCount[1]/(occurCount[0]+occurCount[1])
    #     #     black_perc = 100*occurCount[0]/(occurCount[0]+occurCount[1])
    #     #     print("Black: %.2f%%, White: %.2f%%" % (black_perc, white_perc))


    #     # # perform transparency between threshold image and the original one in gray scale
    #     # # img = image_analyzer.binary_image.copy()
    #     # # output = image_analyzer.image_gray.copy()
    #     # # output = cv.addWeighted(img, alpha, output, 1-alpha, 0, output)

    # after thrsehold values has been choose, close window
    # thresh_support.destroy_window()


    # print("Threshold: ", thresh)
    # width, height = image_analyzer.get_image_dimensions()


    # # apply geometric pattern over binary-image to extract the respective pixels values
    # # returns only the number of pixels of one phase. We are supposing a two-phase micrographic image.

    # # ASTM Designation: E-562 "
    # # This test method may be used to determine the volume fraction of constituents in an opaque
    # # specimen using a polished, planar cross section by the manual point count procedure"

    #   # each phase of a two-phase micrographic image is represented by one color (black/white)

    # # n = number of fields counted.
    # n = 15
    # print("Number of field: ",n)

    # # Pp(i) = Pi/Pt x 100 = percentage of grid points, in the constituent observed on the i th field.
    # Pp = np.zeros( shape=(n+1), dtype=float)

    # # Pt = total number of points in the test grid. Here, we are using two concentric circunferences
    # Pt = 24
    # grid_size = Pt
    # print("Number of grid points: ", Pt)

    # for i in range(1, n+1):

    #     # coordinates of binary image where the circular pattern is located
    #     coords = pattern.get_coordinates(root, canvas, width, height, grid_size)

    #     rows = coords[:,1]
    #     cols = coords[:,0]
    #     pixels = image_analyzer.binary_image[rows, cols]
    #     # print(pixels)

    #     # Get a tuple of unique values & their frequency in numpy array
    #     uniqueValues, occurCount = np.unique(pixels, return_counts=True)
    #     # print("Unique Values : " , uniqueValues)
    #     # print("Occurrence Count : ", occurCount)

    #     # Pi = point count on the ith field.
    #     Pi = occurCount[1]

    #     Pp[i] = Pi/Pt * 100
    #     # print("Percentage: ", Pp[i])


    #     # the average, Pp_avg
    #     Pp_avg = np.mean(Pp)
    #     print("avg: ", Pp_avg)

    #     # The standard deviation is the square root of the average of the squared
    #     # deviations from the mean, i.e., std = sqrt(mean(abs(x - x.mean())**2)).
    #     # The average squared deviation is normally calculated as x.sum() / N, where
    #     # N = len(x). If, however, ddof is specified, the divisor N - ddof is used
    #     # instead. In standard statistical practice, ddof=1 provides an unbiased
    #     # estimator of the variance of the infinite population. ddof=0 provides a
    #     # maximum likelihood estimate of the variance for normally distributed
    #     # variables.
    #     # ddof: Means Delta Degrees of Freedom. The divisor used in calculations
    #     # is N - ddof, where N represents the number of elements. By default ddof
    #     # is zero.
    #     s = np.std(Pp, ddof=1)
    #     print("STD: ",s)


    #     # t - multiplier
    #     multiplier = CIM()
    #     t = multiplier.get(n)
    #     print("t = ",t)

    #     # the 95 % confidence interval: CI
    #     CI = t * s/np.sqrt(n)
    #     print("95 % confidence interval (CI): ", CI)

    #     # The volume percentage estimate is given as:
    #     V_v = (Pp_avg-CI, Pp_avg + CI)
    #     print("Phase A: %.2f%% +/- %.2f" % (Pp_avg, CI))
    #     print("Phase B: %.2f%% +/- %.2f" % (100-Pp_avg, CI))

    #     # An estimate of the % relative accuracy associated with the estimate
    #     RA = CI / Pp_avg * 100
    #     print("Percentual relative accuracy: %.2f%% " % RA)
    #     print("---------------------------------------------------------------")


