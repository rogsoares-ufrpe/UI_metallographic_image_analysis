
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import cv2
import scale_entry_window as sew


class SWD: 
    """ SWD: sacle Window Dialog"""
    def __init__(self, root, canvas): 
        self.root = root 
        self.Window = None
        self.Entry = None
        self.x0 = 0
        self.y0 = 0
        self.first_click = False
        self.second_click = False
        
        self.wait_variable = BooleanVar()
        self.wait_variable.set(False)
    
        self.x1 = 0
        self.y1 = 0
        self.count = 0
        
        self.pixel_length = 0
        self.scale = 0
        
        self.canvas = canvas
        
        self.line = self.canvas.create_line(0, 0, 0, 0, fill='red', width=2)
        self.left_tick = self.canvas.create_line(0, 0, 0, 0, fill='red', width=2)
        self.right_tick = self.canvas.create_line(0, 0, 0, 0, fill='red', width=2)
    
      
    def callback_movement(self, event):
        if self.first_click and not self.second_click:
            self.x1 = event.x
            self.y1 = event.y
            self.canvas.coords(self.right_tick, self.x1, self.y0-12, self.x1, self.y0+12)
            self.canvas.coords(self.line, self.x0, self.y0, self.x1, self.y0)
        
    
    def set_and_close(self):
        s = self.Entry.get()
        self.scale = float(s)
        self.wait_variable.set(True)
        self.Window.destroy()
        self.Window = None
        
        
    def get(self):
        """Hold on program while data is obtained. self.scale and self.pixel_length
        are not availabel when this function is called"""
        self.root.wait_variable(self.wait_variable)
        
        return self.scale, self.pixel_length
    
        
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
            self.open_dialog()
       
        
    def open_dialog(self):
        # win, top = sew.create_EntryWindows(self.root)
        # top.Button.configure(command=lambda: self.get_and_close(top))
        # global win
        
        self.Window = tk.Toplevel(self.root)
        self.Window.title("Set scale")
        self.Window.geometry("234x85+679+310")
        self.Window.minsize(120, 1)
        self.Window.maxsize(1924, 1061)
        self.Window.resizable(1, 1)
        label1 = tk.Label(self.Window, text="Value = ").grid(row=0, padx=10, pady=10)
        self.Entry = tk.Entry(self.Window, width=12)
        self.Entry.grid(row=0, column=1, sticky=W)
        label2 = tk.Label(self.Window, text= u'''\u03BC'''+'''m''').grid(row=0, column=2, padx=10, pady=10, sticky=E)
        btn = tk.Button(self.Window, text="OK", command=self.set_and_close)
        btn.grid(row=2, column=1, padx=0, pady=5)
            
            
    
# if __name__ == "__main__":
    
#     root = Tk() 
#     gfg = GFG(root)
#     root.bind("<Motion>", lambda e: gfg.callback_movement(e))
#     root.bind("<Button-1>", lambda e: gfg.callback_click(e))
#     mainloop()
    