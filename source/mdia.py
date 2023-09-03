import numpy as np
import cv2
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox as msgbox
import h5py


from cv2.ximgproc import THINNING_ZHANGSUEN
from cv2.ximgproc import THINNING_GUOHALL

import matplotlib.pyplot as plt


class Colors:
    def __init__(self):
        self.red = (0, 0, 255)
        self.yellow = (0, 255, 255)
        self.white = (255, 255, 255)
        self.cian =  (255, 255, 0)
        self.blue = (255, 0, 0)
        self.magenta = (255, 0, 255)
        self.green = (0, 255, 0)
        self.black = (0, 0, 0)


class MDIA:
    """ MDIA: digital metallographic image analyzer """

    def __init__(self):
        self.image_cv = None        # segmentation over original image
        self.image_canvas = None    # segmentation over original image to be displayed on canvas window
        self.image_gray = None      # Image to be segmented
        self.image_filtered = None      # Image to be segmented
        self.image_original = None
        self.binary_image = None
        self.original_image_one_quarter = None
        self.path = None            # path for image file

        # image dimensions
        self.height = None
        self.width = None
        self.no_channels = None

        self.img_loaded = False
        self.grains_already_segmented = False

        # filter/smoothing algorithm
        # self.filter = 0
        self.filter_name = "None"
        self.last_filer_applyed = "None"
        self.image_gray_exists = False

        # Canny parameters
        self.threshold_one = 125
        self.threshold_two = 150
        self.l2grad = False

        self.colors = Colors()

        # grains
        self.grains_area = []
        self.grains_contours = []


    def get_image_dimensions(self):
        """Return a tuple: width, height"""
        return (self.width, self.height)


    def load_image(self, path_to_image, loaded_from_analysis=False, img=None):

        # store image path
        self.path = path_to_image

        if not loaded_from_analysis:
            self.image_original = cv2.imread(self.path)
        else:
            self.image_original = img

        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, self.no_channels = self.image_original.shape
        self.resize()
        self.height, self.width, self.no_channels = self.image_original.shape
        
        # convert resized original image to gray scale
        self.image_gray = cv2.cvtColor(self.image_original, cv2.COLOR_BGR2GRAY)

        # set to canvas only gray image
        self.set_image_for_canvas(self.image_gray)

        # initialize
        self.image_filtered = self.image_original.copy()


        self.img_loaded = True
        self.grains_already_segmented = False
 
    
    def resize(self):
        ratio = float(810/self.width)
        if self.height*ratio > 550:
            ratio = float(550/self.height)

        # shrink to width
        if self.width >= 810:
            self.image_original = cv2.resize(self.image_original, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_AREA)
        else:
            self.image_original = cv2.resize(self.image_original, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_CUBIC)



    def set_image_for_canvas(self, img):
        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        self.image_canvas = None
        self.image_canvas = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # convert the images to PIL format...
        self.image_canvas = Image.fromarray(self.image_canvas)

        # ...and then to ImageTk format
        self.image_canvas = ImageTk.PhotoImage(self.image_canvas)


    def get_orinal_image_grayscale(self):
        return cv2.cvtColor(self.image_original, cv2.COLOR_BGR2GRAY)


    def find_grains(self):
        """Perform Canny algorithm to find edges segmentation.
        Gray image scale is created during loading image process """

        if not self.img_loaded:
            msgbox.showerror("Error","Image file not openned.")
            return -1

        if not self.is_segmented() or self.last_filer_applyed != self.filter_name:

            self.last_filer_applyed = self.filter_name

            # Remove noise
            # self.apply_filter_smooth_algorithms()
            
            
            print(self.image_filtered.shape)
            self.image_gray = self.image_filtered.copy()

            self.image_gray[:, 0] = 255
            self.image_gray[0, :] = 255
            self.image_gray[:, -1] = 255
            self.image_gray[-1, :] = 255
            
            # Edge segmentation
            edges = cv2.Canny(self.image_gray,
                              threshold1=self.threshold_one,
                              threshold2=self.threshold_two,
                              L2gradient=self.l2grad)

            # removing undersireble edges
            edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, None)
            # edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, None)
            edges = cv2.ximgproc.thinning(edges, thinningType=THINNING_ZHANGSUEN)
            # edges = cv2.ximgproc.thinning(edges, thinningType=THINNING_GUOHALL)

            # realiza a poda dos contornos
            edges = np.uint8(edges > 0)
            count = 0
            while count != np.sum(edges):
                # non-zero pixel count
                count = np.sum(edges)
                # examine 3x3 neighborhood of each pixel
                filt = cv2.boxFilter(edges, -1, (3, 3), normalize=False)
                # if the center pixel of 3x3 neighborhood is zero, we are not interested in it
                edges = edges * filt
                # now we have pixels where the center pixel of 3x3 neighborhood is non-zero
                # if a pixels' 8-connectivity is less than 2 we can remove it
                # threshold is 3 here because the boxfilter also counted the center pixel
                edges[edges < 3] = 0
                # set max pixel value to 1
                edges[edges > 0] = 1

            num_rows = len(edges)
            num_cols = len(edges[0])

            for i in range(num_rows):
                for j in range(num_cols):
                    if edges[i][j] == 1:
                        edges[i][j] = 255

            # print('find contours')
            contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            length = len(contours)
            minarea = 5

            self.grains_contours.clear()
            self.grains_area.clear()

            max_area = -1
            pos = -1
            counter = 0
            for k in range(length):
                area = cv2.contourArea(contours[k])
                if area > minarea:
                    self.grains_contours.append(contours[k])
                    self.grains_area.append(area)
                    counter += 1

                    if area > max_area:
                        max_area = area
                        pos = counter

            self.grains_area.pop(pos)
            self.grains_contours.pop(pos)
            self.grains_already_segmented = True


        "Guarrantees correct image update everytime some modification is required."
        self.image_cv = np.copy(self.image_original)


    def is_segmented(self):
        """Returns true if image grains have already been segmented."""
        return self.grains_already_segmented


    def draw_contours(self, isFilled):
        # color list
        color_list = [self.colors.blue, self.colors.red, self.colors.yellow, \
                      self.colors.magenta, self.colors.cian, self.colors.green]

        # fill or not contours
        filled = 1
        if isFilled==1:
            filled = cv2.FILLED

        k = 0
        counter = 1
        font = cv2.FONT_HERSHEY_SIMPLEX
        mask = np.zeros(self.image_gray.shape, np.uint8)
        for area, cnt in zip(self.grains_area, self.grains_contours):

            # if area>400:
            #     print(area)
            #     x, y, w, h = cv2.boundingRect(cnt)
            #     pos = (int(x+w/2), int(y+h/2))
            #     cv2.putText(self.image_cv,str(counter),pos, font, 0.5, (0,255,255), 1, cv2.LINE_AA)
                
            cv2.drawContours(self.image_cv, [cnt], 0, color_list[k], thickness=filled)

            # extract pixels from countour's interior
            # mask[::] = 0
            # cv2.drawContours(mask,[cnt], 0, 255, -1)
            # pixelpoints = np.transpose(np.nonzero(mask))

            # if len(pixelpoints) != 0:
            #     # calculate average mean pixel
            #     px_values_sum = 0
            #     for px in pixelpoints:
            #         px_values_sum += int(self.image_gray[px[0], px[1]])
            #     px_mean = px_values_sum/len(pixelpoints)
            #     # print("mean[%d]: %f" % (counter, px_mean) )

            #     for px in pixelpoints:
            #         self.image_cv[px[0], px[1]] = int(px_mean)

            counter += 1
            k += 1
            if k==6:
                k = 0

        # Highlight grains contours
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        cv2.drawContours(self.image_cv, self.grains_contours, -1, self.colors.red, thickness=1)

        # cv2.imwrite("Fig2b-cut-filtered.jpg", self.image_cv)
        # plt.imshow(self.image_cv)
        # plt.show()

    def grains_histogram(self):
        num_bins = 50
        n, bins, patches = plt.hist(self.grains_area, num_bins, facecolor='blue', alpha=0.5)
        plt.show()


    def apply_filter_smooth_algorithms(self):
        
       
        print("Filter applied: ", self.filter_name)
        if self.filter_name == "Gaussian blur":
            self.image_filtered = cv2.GaussianBlur(self.image_filtered, (15,15), 0)
        elif self.filter_name == "2D convolution":
            kernel = np.ones((5, 5), np.float32) / 25
            self.image_filtered = cv2.filter2D(self.image_filtered, -1, kernel)
        elif self.filter_name == "Median Blurring":
            self.image_filtered = cv2.medianBlur(self.image_filtered, 7)
        elif self.filter_name == "Bilateral Filter":
            self.image_filtered = cv2.bilateralFilter(self.image_filtered, 9, 75, 75)
        elif self.filter_name == "Averaging":
            self.image_filtered = cv2.blur(self.image_filtered, (5, 5))
        elif self.filter_name == "HistogramEqualization":
            self.image_gray = cv2.cvtColor(self.image_filtered, cv2.COLOR_BGR2GRAY)
            self.image_filtered = cv2.equalizeHist(self.image_gray);
        else:
            self.image_filtered = np.copy(self.image_original)


    def set_parameters(self, param):
        self.filter = param[0]
        self.l2grad = param[1]
        self.threshold_one = param[2]
        self.threshold_two = param[3]
        # print(param)


    def get_filter_name(self):
        return self.filter_name

    def set_image_filter(self, the_filter):
        self.filter_name = the_filter
        print("Filter: ", the_filter)


    def create_binary_image(self, img_gray, thresh=150, maxval=255):

        if self.last_filer_applyed != self.filter_name:
            self.last_filer_applyed = self.filter_name
            self.apply_filter_smooth_algorithms()

        # # calculate histogram of original gray scaled image before and after noise reduction
        # hist_img = cv.calcHist([img],[0],None,[256],[0,256])
        # hist_median = cv.calcHist([median],[0],None,[256],[0,256])

        # apply threshold over filtered image
        # ret, self.binary_image = cv2.threshold(img_gray, thresh, maxval, cv2.THRESH_BINARY)
        self.binary_image =  cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

