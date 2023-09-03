import h5py
import numpy as np

class IAM:
    
    def __init__(self):
        
        self.ha = 1         # ha: image height (pixels)
        self.hr = 1         # hr: real height (micrometers)
        self.ep = 1         # ep: scale length (pixels)
        self.er = 1         # er: scale taken from picture (in/micrometers)
        self.M = 1          # M: image magnification
        self.width = 1      # width: image width (pixels)
        self.height = 1     # height: image height (pixels)
        self.path = ''      # path: path for image file
        self.image_original = None # original image
        
        self.ratio = 1
    
    def set_ratio(self):
        self.ratio = self.ep/self.er
        
        
    def px_to_um(self, p):
        """Convert pixels to micrometers"""
        return (self.er/self.ep)*p
    
    def um_to_px(self, um):
        """Convert pixels to micrometers"""
        return int((self.ep/self.er)*um)
    
        
    def save(self, project_name, image_original):
        filename = project_name + ".hdf5"
        
        with h5py.File(filename, 'w') as f:
            f.attrs['ha'] = self.ha
            f.attrs['hr'] = self.hr
            f.attrs['M'] = self.M
            f.attrs['width'] = self.width
            f.attrs['height'] = self.height
            f.attrs['ep'] = self.ep
            f.attrs['er'] = self.er
            f.attrs["path"] = filename
            f.create_dataset("image_original", np.shape(image_original), h5py.h5t.STD_U8BE, data=image_original)
        
            
    def clear(self):
        self.ha = 0
        self.hr = 0
        self.ep = 0
        self.er = 0
        self.M = 0
        self.width = 0
        self.height = 0
        self.path = ''
            
    
    def load(self, filename):
        with h5py.File(filename, 'r') as f:        
            self.ha = f.attrs['ha']
            self.hr = f.attrs['hr']
            self.M = f.attrs['M']
            self.width = f.attrs['width']
            self.height = f.attrs['height']
            self.ep = f.attrs['ep']
            self.er = f.attrs['er']
            self.path = f.attrs['path']
            self.image_original = np.array(f["/image_original"]).astype("uint8")
            
        self.print_data()
            
            
    def print_data(self):
        print("Path: ", self.path)
        print("Scale value: ", self.er)
        print("ratio: %f pixels/\u03BCm" % float(self.ep/self.er))
        print("Length in pixels: ", self.ep)
        print("Magnification: %.1f X" % float(self.M))
        print("ALtura da imagem ampliada: %.2f mm" % (self.ha/1000))
