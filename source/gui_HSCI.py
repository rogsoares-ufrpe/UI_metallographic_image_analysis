import tkinter as tk
from tkinter import messagebox as msgbox
import numpy as np

class Hilliard:
    def __init__(self, width, height):
        self.radius = 0.0
        self.width = width
        self.height = height
        self.r_pixels = 0
        
        
    def set_radius(self, top):
        value = float(top.Entry1.get())
        self.radius = value
        self.r_pixels =  int(2.83464566929133*self.radius)
        # print("radius: ", self.radius)
    
        min_value = np.minimum(self.width, self.height)
        lim = int(min_value/2)
        if self.r_pixels > lim:
            msgbox.showerror("Radius error value","It must be less than " + str('{:.2f}'.format(lim/2.83464566929133)) + "mm")
        else:
            top.w.destroy()
            top.w = None
        
    def get_radius(self):
        """"Return circunference radius in mm"""
        return self.r_pixels
    

def create_Toplevel_HSCP(root, hilliard, *args, **kwargs):
    top = Toplevel_HSCP(hilliard)
    return top


def destroy_Toplevel_HSCP():
    global w
    w.destroy()
    w = None


class Toplevel_HSCP:
    def __init__(self, ext, top=None):
        self.w = tk.Toplevel()
        top = self.w
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("340x105+731+396")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("Hilliard Single Circle Interecept")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.029, rely=0.19, height=21, width=143)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Enter circunference radius''')

        self.Button_radius = tk.Button(top)
        self.Button_radius.place(relx=0.353, rely=0.571, height=24, width=50)
        self.Button_radius.configure(activebackground="#ececec")
        self.Button_radius.configure(activeforeground="#000000")
        self.Button_radius.configure(background="#d9d9d9")
        self.Button_radius.configure(disabledforeground="#a3a3a3")
        self.Button_radius.configure(foreground="#000000")
        self.Button_radius.configure(highlightbackground="#d9d9d9")
        self.Button_radius.configure(highlightcolor="black")
        self.Button_radius.configure(pady="0")
        self.Button_radius.configure(text='''OK''')
        self.Button_radius.configure(command=lambda: ext.set_radius(self))

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.471, rely=0.19,height=20, relwidth=0.129)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 10")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        tooltip_font = "-family {Segoe UI} -size 9"
        ToolTip(self.Entry1, tooltip_font, '''Keep the same unit measurement applied for the image (in) or (mm)''', delay=0.5)

        self.Button_help = tk.Button(top)
        self.Button_help.place(relx=0.588, rely=0.571, height=24, width=50)
        self.Button_help.configure(activebackground="#ececec")
        self.Button_help.configure(activeforeground="#000000")
        self.Button_help.configure(background="#d9d9d9")
        self.Button_help.configure(disabledforeground="#a3a3a3")
        self.Button_help.configure(foreground="#000000")
        self.Button_help.configure(highlightbackground="#d9d9d9")
        self.Button_help.configure(highlightcolor="black")
        self.Button_help.configure(pady="0")
        self.Button_help.configure(text='''Help''')

# ======================================================
# Modified by Rozen to remove Tkinter import statements and to receive
# the font as an argument.
# ======================================================
# Found the original code at:
# http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
# ======================================================

from time import time, localtime, strftime

class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=1, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          tooltip_font: Font to be used
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in miliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()

# ===========================================================
#                   End of Class ToolTip
# ===========================================================

if __name__ == '__main__':
    vp_start_gui()





