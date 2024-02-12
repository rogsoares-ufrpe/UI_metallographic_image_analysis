import numpy as np
import cv2
from PIL import Image
from PIL import ImageTk
# from tkinter import messagebox as msgbox
# import h5py
import os

import ImageAnalysisManeger as iam

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




class MEDIA:
    """ MEDIA: MEtallographic digital image analyzer 
    
    The MUST importtant class of the whole project!!!!!!
    
    Lista de funções da classe MDIA
    --------------------------------------------------------------------------
    
    Algoritmos de tratamento de imagem
    --------------------------------------------------------------------------
    def set_parameters(self, param):
    def get_filter_name(self):
    def set_image_filter(self, the_filter):
    def create_binary_image(self, img_gray, thresh=150, maxval=255):
    def get_image_dimensions(self):
    def load_image(self, path_to_image, loaded_from_analysis=False, img=None):
    def resize(self):
    def set_image_for_canvas(self, img):
    def get_orinal_image_grayscale(self):
    def apply_filter_smooth_algorithms(self): 
        
    Algoritmos de segmentação de imagem
    --------------------------------------------------------------------------
    def find_grains(self):
    def draw_contours(self, isFilled):
    def grains_histogram(self):
    
        
    """

    def __init__(self):
        
        # The next image objects are cv2 type objects
        # ---------------------------------------------------------------------
        self.image_cv = None        # segmentation over original image
        self.image_canvas = None    # segmentation over original image to be 
                                    # displayed on canvas window
        self.image_gray = None      # Image to be segmented
        self.image_filtered = None  # Image to be segmented
        self.image_original = None  # Self explained
        self.binary_image = None
        self.original_image_one_quarter = None
        
        # ---------------------------------------------------------------------
        self.path = None            # path for image file

        # image dimensions
        # ---------------------------------------------------------------------
    
        self.height = None          
        self.width = None
        self.no_channels = None

        self.img_loaded = False
        self.segmented_image = False

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
        self.contours = []
        self.area_contours_sorted = []
        self.grains_area_percenage = 0
        self.counter = 0
        self.grains_total_area = 0
        self.image_area_converted = 0
        self.cnt_minmax = [None]*2
        self.tag_min = 0
        self.tag_max = 0
        
        # object for Image dimension properties
        self.image_prop = iam.IAM()          


    def get_image_dimensions(self):
        """Return a tuple: width, height"""
        return (self.width, self.height)

    def is_image_loaded(self):
        return self.img_loaded

    '''
    It only initialize the object <self.image_original> from OpenCV using the
    filename path
    '''
    def load_image(self, path_to_image, loaded_from_analysis=False, img=None):

        # store image path
        self.path = path_to_image

        if loaded_from_analysis:
            self.image_original = img
        else:
            self.image_original = cv2.imread(self.path)

        self.adjust_image_dimensions()

        self.img_loaded = True
        self.segmented_image = False
    
    '''
    Modify, if necessary, image dimensions (height and width) to fit to canvas 
    area and turn it into gray scale for appropriated analysis
    '''
    def adjust_image_dimensions(self):
        
        self.resize()        
        
        # convert resized original image to gray scale
        self.image_gray = cv2.cvtColor(self.image_original, cv2.COLOR_BGR2GRAY)

        # initialize
        self.image_filtered = self.image_original.copy()
 
    '''
    Let's suppose Canvas has 800x600 pixel of resolution'. It fits image to 
    Canvas area using OpenCV algorithms
    '''
    def resize(self):
        
        # Get imagem dimensions from the loaded image
        self.height, self.width, self.no_channels = self.image_original.shape
        
        # Start resizing procedures
        ratio = float(720/self.width)
        if self.height*ratio > 520:
            ratio = float(520/self.height)

        # shrink to width
        if self.width >= 720:
            self.image_original = cv2.resize(self.image_original, 
                                             None, 
                                             fx=ratio, fy=ratio, 
                                             interpolation=cv2.INTER_AREA)
        else:
            self.image_original = cv2.resize(self.image_original, 
                                             None, 
                                             fx=ratio, fy=ratio, 
                                             interpolation=cv2.INTER_CUBIC)

        # Get imagem dimensions from the resized loaded image
        self.height, self.width, self.no_channels = self.image_original.shape
        
    '''
    Defines an image object to be used with canvas. So everytime any modification
    is made to the original greyscale image, <set_image_for_canvas> must be called
    to display it.
    '''
    def set_image_for_canvas(self, img):
        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        # self.image_canvas = None
        self.image_canvas = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)            

        # convert the images to PIL format...
        self.image_canvas = Image.fromarray(self.image_canvas)

        # ...and then to ImageTk format
        self.image_canvas = ImageTk.PhotoImage(self.image_canvas)
        
        return self.image_canvas
        
    def get_image_for_canvas(self):
        return self.image_canvas

    '''
    If a new analysis must be done over the same image, previous modifications
    like edge countors segmentation or areas filling will be present. So, get
    a brand new image.
    '''
    def get_image_grayscale(self):
        return cv2.cvtColor(self.image_original, cv2.COLOR_BGR2GRAY)

    def get_image_original(self):
        return self.image_original
    

    def grains_histogram(self):
        num_bins = 50
        n, bins, patches = plt.hist(self.grains_area, num_bins, facecolor='blue', alpha=0.5)
        plt.show()

    '''
    Applies an image filtering or smoothing algorithm which probably will lead
    to more effective edge detection results.
    '''
    def apply_filter_smooth_algorithms(self):
 
        # print("Filter applied: ", self.filter_name)
        if self.filter_name == "Gaussian blur":
            self.image_filtered = cv2.GaussianBlur(self.image_original, (15,15), 0)
        elif self.filter_name == "2D convolution":
            kernel = np.ones((5, 5), np.float32) / 25
            self.image_filtered = cv2.filter2D(self.image_original, -1, kernel)
        elif self.filter_name == "Median Blurring":
            self.image_filtered = cv2.medianBlur(self.image_original, 7)
        elif self.filter_name == "Bilateral Filter":
            self.image_filtered = cv2.bilateralFilter(self.image_original, 9, 75, 75)
        elif self.filter_name == "Averaging":
            self.image_filtered = cv2.blur(self.image_original, (5, 5))
        elif self.filter_name == "Laplacian":            
            """
            The function can process the image in-place.
            cv.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]	) ->	dst
            
            Parameters:
            * src	          Source 8-bit single-channel image.
            * dst	          Destination image of the same size and the same 
                              type as src.
            * maxValue	      Non-zero value assigned to the pixels for which the
                              condition is satisfied
            * adaptiveMethod  Adaptive thresholding algorithm to use, see 
                              AdaptiveThresholdTypes. The BORDER_REPLICATE | 
                              BORDER_ISOLATED is used to process boundaries.
            * thresholdType	  Thresholding type that must be either THRESH_BINARY
                              or THRESH_BINARY_INV, see ThresholdTypes.
            * blockSize	      Size of a pixel neighborhood that is used to cal-
                              culate a threshold value for the pixel: 3, 5, 7, 
                              and so on.
            """
            gray_img = self.get_image_grayscale()            
            # self.image_filtered = cv2.adaptiveThreshold(gray_img,
            #                                             127,
            #                                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            #                                             cv2.THRESH_BINARY,
            #                                             11,
            #                                             2)                                                        
            
            ret, self.image_filtered = cv2.threshold(gray_img,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
        else:
            self.image_filtered = np.copy(self.image_original)

    def get_filtered_image(self):
        return self.image_filtered
    
    def set_parameters(self, param):
        self.filter = param[0]
        self.l2grad = param[1]
        self.threshold_one = param[2]
        self.threshold_two = param[3]
        # print(param)


    def is_image_segmented(self):
        """Returns true if image grains have already been segmented."""
        return self.segmented_image

    def get_filter_name(self):
        return self.filter_name

    def set_image_filter(self, the_filter):
        self.filter_name = the_filter
        # print("Filter: ", the_filter)

    
    def find_grains(self, gsp):
        """
        Perform Canny algorithm to find edges segmentation.
        gsp: Control grains size area display
        """
        
        msg = []
        contours = []
        
        self.image_gray = self.image_filtered.copy()

        if not self.is_image_segmented():
            # Edge segmentation
            '''
            Finds edges in an image using the Canny algorithm [45] .
            The function finds edges in the input image and marks them in the 
            output map edges using the Canny algorithm. The smallest value 
            between threshold1 and threshold2 is used for edge linking. The 
            largest value is used to find initial segments of strong edges. 
            See http://en.wikipedia.org/wiki/Canny_edge_detector
            '''
            edges = cv2.Canny(self.image_gray,
                              threshold1=self.threshold_one,
                              threshold2=self.threshold_two,
                              L2gradient=False)
            
            # As duas próximas funções são de extrema importância na qualidade da de-
            # finição dos contornos dos grãos removendo aresas desnecessárias.
            
            # removing undersireble edges
            edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, None)
            
            # edges = cv2.ximgproc.thinning(edges, thinningType=THINNING_ZHANGSUEN)
            edges = cv2.ximgproc.thinning(edges, thinningType=THINNING_GUOHALL)
    
            # remove unnecessary edges 
            edges = self.edges_trim(edges)        
    
            # Use edges detected on image connecting each them to form grains contours
            self.contours, h  = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        
        # Some contours are really useless
        self.remove_unnecessary_grains_contours(gsp)
        
        self.segmented_image = True

        # if something went wrong, terminate program
        if not len(self.grains_area):
            msg.append(1)
            msg.append("Grains segmentation procedure has failed! ")            
            return msg
        
        self.image_cv = np.copy(self.image_original)
        
        return msg

    
    def edges_trim(self, _edges):
        """ Performs edges trim for better results"""
        
        edges = np.uint8(_edges > 0)
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
        return edges

    
    def remove_unnecessary_grains_contours(self, gsp):
        """Remove tiny or large contours from list """
        
        # image_area = self.height * self.width
        
        # clean up before performing 
        self.grains_contours.clear()
        self.grains_area.clear()
        
        list_of_centroids = []
        centroid_zero = (0,0)
        list_of_centroids.append(centroid_zero)
    
        # Calcula média e desvio padrão para todas as áreas detectadas
        # pelo algoritmo de segmentação de imagem
        # Passo 1:
        gareas = []
        n = gsp
        # print("Numero de grãos originais: ", len(self.contours))
        for cnt in self.contours:
            gareas.append(cv2.contourArea(cnt))
            
        M_original = np.mean(gareas) # Média
        M = M_original
        SD = np.std(gareas) # Desvio padrão
        # print("M: %.2f,  STD: %.2f" % (M,SD))
        
        
        
        # Passo 2:
        # remova os elementos da lista no sentido maior->menor
        # a cada remoção recalcule M e SD
        # print("remova os elementos da lista no sentido maior->menor")
        while M-n*SD < 0 and len(gareas):
            
            # pop: remove elemento da lista
            gareas.pop(len(gareas)-1)
            
            M = np.mean(gareas)
            SD = np.std(gareas)
            # print("M: %.2f, STD: %.2f, len=%d" % (M,SD,len(gareas)))
            
        # Quando passo 2 falhar 'len(gareas)=1', assuma
        if len(gareas)==1:
            M = M_original
            SD = M
            
        # print("Valor de n:", n)
        # print("Numero de falsos graos removidos: ", len(contours) - len(gareas))
        # print("Fim do processo para encontrar a média e o desvio padrão.")
        
        # Inicia de fato a seleção dos grãos que seão utilizados nas
        # análises metalográficas
        
        
        # self.cnt_minmax.clear()
        min = 1e10
        max = -1
        
        # Cada grão recebe uma numeração sequencial de 1 a len(grains_area)
        # tag_min e tag_max são a numeração dos grãos de menor e maior area, respectivamente
        self.tag_min = 0
        self.tag_max = 0
        for cnt in self.contours:
            area = cv2.contourArea(cnt)           
        
            if  M - n*SD < area < M + n*SD:
                x, y, w, h = cv2.boundingRect(cnt)
                centroid = (int(x+w/2), int(y+h/2))
                # print(centroid)
                
                if not centroid in list_of_centroids:
                    self.grains_contours.append(cnt)
                    self.grains_area.append(area)
                    list_of_centroids.append(centroid)
                    
                    if area > max:
                        max = area
                        self.cnt_minmax[1] = cnt
                        self.tag_max += 1
                    if area < min:
                        min = area
                        self.cnt_minmax[0] = cnt
                        self.tag_min += 1
            # else:
            #     print("Varifique grão: %.2f < %.2f < %.2f. Falhou! n=%d" % (M-n*SD, area, M+n*SD, n))
        
        list_of_centroids.clear()

    

    def draw_contours(self):
        for cnt in self.grains_contours:
            # print("cnt:", cnt)
            cv2.drawContours(self.image_cv, [cnt], -1, self.colors.blue, thickness=1)

            
    def fill_contours(self):
        """Preenche a area dos graos com uma cor"""
        for i in range(len(self.grains_contours)):
            cv2.drawContours(self.image_cv, [self.grains_contours[i]], -1, self.colors.yellow, thickness=cv2.FILLED)
    
    def draw_minmax_grains_area(self):
        
        # Maximo
        # ---------------------------------------------------------------------
        # Desenha o contorno do grão
        cv2.drawContours(self.image_cv, [self.cnt_minmax[1]], -1,self.colors.red, thickness=cv2.FILLED)
        
        # Desenha caixa em torno do grão
        x, y, w, h = cv2.boundingRect(self.cnt_minmax[1])
        cv2.rectangle(self.image_cv,(x,y),(x+w,y+h), self.colors.cian,1)
        
        # Desenha caixa de fundo (Ponto incial da caica: 30 pixels a direita da quina Leste para o mesmo y)
        cv2.rectangle(self.image_cv,      (x+w+15,y-4), (x+w+65, y+18), self.colors.cian, -1)
        
        # Desenha texto sobre caixa
        text = "Max" # (tag:" + str(self.tag_max) + ")"
        cv2.putText(self.image_cv, text, (x+w+15,y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.85, self.colors.black, 1, cv2.LINE_AA)
        
        # Mínimo
        # ---------------------------------------------------------------------
        # Desenha o contorno do grão
        cv2.drawContours(self.image_cv, [self.cnt_minmax[0]], -1,self.colors.blue, thickness=cv2.FILLED)
        
        # Desenha caixa em torno do grão
        x, y, w, h = cv2.boundingRect(self.cnt_minmax[0])
        cv2.rectangle(self.image_cv,(x,y),(x+w,y+h), self.colors.cian,1)
        
        # Desenha caixa de fundo (Ponto incial da caica: 30 pixels a direita da quina Leste para o mesmo y)
        cv2.rectangle(self.image_cv,(x+w+15,y-4), (x+w+60, y+18), self.colors.cian, -1)
        
        # Desenha texto sobre caixa
        text = "Min"  # (tag:" + str(self.tag_min) + ")"
        cv2.putText(self.image_cv, text, (x+w+15,y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.85, self.colors.black, 1, cv2.LINE_AA)
        
            
    def numbering_grains(self):
        """
        Insere um número de identificação no interior de um grão
        """     
        counter = 0
        font = cv2.FONT_HERSHEY_SIMPLEX        
        for cnt in self.grains_contours:
            counter += 1
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.putText(self.image_cv, str(counter), (int(x+w/4), int(y+h/2)), font, 0.25, self.colors.red, 1, cv2.LINE_AA)

    
    def draw_bounding_box(self):
        """
        Constrói uma caixa em torno (boundary box) deste se verdadeira
        """        
        for cnt in self.grains_contours:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(self.image_cv,(x,y),(x+w,y+h), self.colors.cian,1)   
    
    def convert_grains_pixel2micro(self):
        """Convert grains areas in pixels to micrometers"""
    
        self.grains_area = self.image_prop.convert_pixels_to_micrometers(self.grains_area)
        
        # converte image area in pixels to um
        self.image_area_converted = self.height * self.width*self.image_prop.ratio_area
        self.grains_total_area = sum(self.grains_area)
        self.grains_area_percenage = 100*self.grains_total_area/self.image_area_converted
        
    
    def save_analysis_image_files(self, filename):
        """Saves to file the original and the analyzed images. Two .png files"""
        cv2.imwrite(filename+"_analized.png", self.image_cv)
        cv2.imwrite(filename+"_original.png", self.image_original)
        
    
    def get_report_analysis(self):        
        
        title = "Grain alloy microstructure analysis report"
        header = ["Item", "Results"]
        data_rows = [
            ["Sample: ", os.path.basename(self.path)],
            ["Number of grains ", len(self.grains_area)],
            ["Average grain size (um)", "{:.2f}".format( np.mean(self.grains_area)) ],
            ["Min. grain size (um)",    "{:.2f}".format( np.min(self.grains_area ))  ],
            ["Max. grain size (um)",    "{:.2f}".format( np.max(self.grains_area))],
            ["Image size (um):",        "{:.2f}".format( self.image_area_converted) ],
            ["Total grains size (um):", "{:.2f}".format( self.grains_total_area) ],
            ["Total grains (%):",       "{:.2f}".format( np.max(self.grains_area_percenage))],
            ["Filter image:", self.filter_name],
            ["Edge detection:", "Canny"]
            ]
        
        return title, header, data_rows        
        
        
        