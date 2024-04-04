import h5py
import numpy as np

class IAM:
    """
    IAM (ImageAnalisysManager) class: defines atributes for proper analisys of 
    metallographic image like scales in pixels and micrometers as well as image
    magnification. All these atributes and more, after image analisys, can be
    written in file (HDF5 file format) for later comparisons.    
    """
    def __init__(self):
        
        self.ha = 1         # ha: image height (pixels)
        """Real image height ..."""
        
        self.hr = 1         # hr: real height (micrometers)
        """Real height in micrometers"""
        
        self.scale_pixels = 1
        """Number of pixels captured from the scale drawing present in the image."""
            
        self.scale_micrometers = 1         # er: scale taken from picture (in/micrometers)
        self.Magnification = 1          # M: image magnification
        self.width = 1      # width: image width (pixels)
        self.height = 1     # height: image height (pixels)
        self.path = ''      # path: path for image file
        self.image_original = None # original image        
        
        self.ratio_area = 1
        
        self.pixels_per_um_ratio = 1
        """ratio says how many pixels represent 1 micrometer"""
    
    def set_ratio(self):    
        self.pixels_per_um_ratio = self.scale_pixels/self.scale_micrometers
    
    
    def convertion_scale_settings(self, scale_micrometers, scale_pixels, M, w, h):
        """Receive image data from scale window widget and set important
        parameters for converting from pixels to micrometers."""
        
        self.width = w
        self.height = h
        
        self.scale_micrometers = scale_micrometers
        self.scale_pixels = scale_pixels        
        self.pixels_per_um_ratio = self.scale_pixels / self.scale_micrometers
        
        # self.ha = (self.height/self.pixels_per_um_ratio)*self.Magnification
        # self.hr = self.ha / self.Magnification
        
        self.ratio_area = self.scale_micrometers**2/self.scale_pixels**2
        print("self.scale_micrometers**2/self.scale_pixels**2 = ", self.ratio_area)
        
    def convert_pixels_to_micrometers(self, theList):
        """ Convert the list of grains areas in pixels to micrometers"""
        print("self.ratio_area:", self.ratio_area)
        theArray = np.array(theList)
        theArray = self.ratio_area*theArray
        return theArray.tolist()
    
    def pixels_to_micrometers(self, val):    
        """
        Convert area in pixels to micrometers"""
        
        # print("self.ratio_area = %f, val = %f" % (self.ratio_area, val))
        return self.ratio_area*val
        
        
    def px_to_um(self, p):
        """Convert pixels to micrometers"""
        return (self.scale_micrometers/self.scale_pixels)*p
    
    
    def um_to_px(self, um):
        """Convert pixels to micrometers"""
        return int((self.scale_pixels/self.scale_micrometers)*um)
    
        
    def save(self, project_name, image_original):
        filename = project_name + ".hdf5"
        
        with h5py.File(filename, 'w') as f:
            f.attrs['ha'] = self.ha
            f.attrs['hr'] = self.hr
            f.attrs['M'] = self.Magnification
            f.attrs['width'] = self.width
            f.attrs['height'] = self.height
            f.attrs['ep'] = self.scale_pixels
            f.attrs['er'] = self.scale_micrometers
            f.attrs["path"] = filename
            f.create_dataset("image_original", np.shape(image_original), h5py.h5t.STD_U8BE, data=image_original)
        
            
    def clear(self):
        self.ha = 0
        self.hr = 0
        self.scale_pixels = 0
        self.scale_micrometers = 0
        self.Magnification = 0
        self.width = 0
        self.height = 0
        self.path = ''
            
    
    def load(self, filename):
        with h5py.File(filename, 'r') as f:        
            self.ha = f.attrs['ha']
            self.hr = f.attrs['hr']
            self.Magnification = f.attrs['M']
            self.width = f.attrs['width']
            self.height = f.attrs['height']
            self.scale_pixels = f.attrs['ep']
            self.scale_micrometers = f.attrs['er']
            self.path = f.attrs['path']
            self.image_original = np.array(f["/image_original"]).astype("uint8")
            
        self.print_data()
            
            
    def print_data(self):
        print("Path:                   ", self.path)
        print("Scale value:            ", self.scale_micrometers)
        print("ratio: %f pixels/\u03BCm" % float(self.scale_pixels/self.scale_micrometers))
        print("Scale in pixels:        ", self.scale_pixels)
        print("Magnification: %.1f X   " % float(self.Magnification))
        # print("ALtura da imagem ampliada: %.2f mm" % (self.ha/1000))
        
    def get_report_analysis(self):
        
        rows = [
            ["Scale value: ",             "{:.2f}".format( self.scale_micrometers) ],
            ["ratio: %f pixels/\u03BCm",  "{:.2f}".format( float(self.scale_pixels/self.scale_micrometers)) ],
            ["Scale in pixels: ",         "{:.2f}".format( self.scale_pixels) ],
            ["Magnification: ",           "{:.2f}".format( float(self.Magnification)) ]
            ]
        
        return rows

    
    def Jeffrie_radius(self):
        """
        Retorna o raio (ampliado) em pixels correspondente a circunferencia de 
        5000mm^2 (área ampliada) adotada pelo procedimento de Jeffries.
        
            r = sqrt(5000/pi) 
              = 39.89422804014327(mm)
        onde r é um valor ampliado
        
        r_real = 39.89422804014327/M, onde M = ampliação
                                             
        valor ampliado (um): val_Magnif_um = 39.89422804014327(mm)
                                           = 0.03989422804014327(um)
        valor real: val_Real_um  = val_Magnif_um / M
        """
        
        M = self.Magnification
        px_per_um__ratio = self.pixels_per_um_ratio
        val_Magnif_um = 3.989422804014327e-2
        
        val_Magnif_px = px_per_um__ratio * M**2 * val_Magnif_um
        return val_Magnif_px