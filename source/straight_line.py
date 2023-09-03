
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import cv2
import scale_entry_window as sew

class GFG: 
    def __init__(self, master = None): 
        self.master = master 
        self.x0 = 0
        self.y0 = 0
        self.first_click = False
        self.second_click = False
    
        self.x1 = 0
        self.y1 = 0
        self.count = 0
        
        self.pixel_length = 0
        self.scale = 0
        self.SI_pixel_ratio = 0
        
        self.canvas = Canvas(master, width=1600, height=1600) 
        self.image_original = cv2.imread("images/large.jpg")    
        self.image_canvas = cv2.cvtColor(self.image_original, cv2.COLOR_BGR2RGB)
        self.image_canvas = Image.fromarray(self.image_canvas)
        self.image_canvas = ImageTk.PhotoImage(self.image_canvas)
        self.canvas.create_image(0,0, image=self.image_canvas, anchor=NW)
        
        self.line = self.canvas.create_line(0, 0, 0, 0, fill='red', width=2)
        self.left_tick = self.canvas.create_line(0, 0, 0, 0, fill='red', width=2)
        self.right_tick = self.canvas.create_line(0, 0, 0, 0, fill='red', width=2)
        
        self.canvas.pack()
    
      
    def callback_movement(self, event):
        if self.first_click and not self.second_click:
            self.x1 = event.x
            self.y1 = event.y
            self.canvas.coords(self.right_tick, self.x1, self.y0-12, self.x1, self.y0+12)
            self.canvas.coords(self.line, self.x0, self.y0, self.x1, self.y0)
        
    
    def get_and_close(self, win, entry):
        s = entry.get()
        self.scale = 1000.0*float(s)
        self.SI_pixel_ratio = float(self.pixel_length/self.scale)
        print("Scale value: ", self.scale)
        print("ratio: %f pixels/mm" % self.SI_pixel_ratio)
        win.destroy()
        win = None
        
    def callback_click(self, event):
        self.count += 1 
        if self.count==1:
            self.x0 = event.x
            self.y0 = event.y
            self.first_click = True
            
            # draw tick
            self.canvas.coords(self.left_tick, self.x0, self.y0-12, self.x0, self.y0+12)
            self.canvas.coords(self.right_tick, self.x0, self.y0-12, self.x0, self.y0+12)
            
            
        elif self.count==2:
            self.second_click = True
            self.pixel_length = self.x1 - self.x0
            print("Length in pixels: ", self.pixel_length)
            
            # win, top = sew.create_EntryWindows(self.master)
            # top.Button.configure(command=lambda: self.get_and_close(top))
            win = Toplevel(self.master)
            win.title("Set scale")
            win.geometry("234x85")
            win.minsize(120, 1)
            win.maxsize(1924, 1061)
            win.resizable(1, 1)
            label1 = Label(win, text="Value = ").grid(row=0, padx=10, pady=10)
            entry = Entry(win, width=12)
            entry.grid(row=0, column=1, sticky=W)
            label2 = Label(win, text="mm").grid(row=0, column=2, padx=10, pady=10, sticky=E)
            btn = Button(win, text="OK", command=lambda: self.get_and_close(win, entry))
            btn.grid(row=2, column=1, padx=0, pady=5)
            
            
    
if __name__ == "__main__":
    
    master = Tk() 
    gfg = GFG(master)
    master.bind("<Motion>", lambda e: gfg.callback_movement(e))
    master.bind("<Button-1>", lambda e: gfg.callback_click(e))
    mainloop()
    