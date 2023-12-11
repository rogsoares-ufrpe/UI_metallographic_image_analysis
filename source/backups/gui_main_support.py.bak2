#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#

# TKinter
import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import filedialog



# Python
import numpy as np
import canvas

# Project
import mdia
import mdiastatistics as gstat
import ImageAnalysisManeger as iam
# from image_data_frame import *
import Jeffries as jeffries
import Heyn as heyn
import Hilliard as hilliard
import Abrams as abrams
import ScaleWinDialog as swd

import draw_double_circular_pattern as draw_pattern
import phases_analysis as p_analysis


image_analyzer = mdia.MDIA()    # object for Metallographic Image Analysis class
image_prop = iam.IAM()          # object for Image dimension properties


def set_Tk_var():
    global MA_RB_variable
    MA_RB_variable = tk.IntVar()

    global RB_var_ISS
    RB_var_ISS = tk.IntVar()

    global RB_var_MP
    RB_var_MP = tk.IntVar()

    global fill_contours_chkbox
    fill_contours_chkbox = tk.IntVar()

    global chkbtn_free_orientation
    chkbtn_free_orientation = tk.IntVar()

    global scale_btn
    scale_btn = tk.IntVar()


def about():
    msgbox.showinfo('About MDIA',
                    'Institution:\n'
                    'Universidade Federal Rural de Pernambuco\n'
                    'Unidade Acadêmica do Cabo de Santo Agostinho\n'
                    '\n\n'
                    'MDIA is developed by Prof. Rogério Soares\n'
                    'e-mail: rogerio.soaress@ufrpe.br\n'
                    '2023')

def quit_app():
    dialog = msgbox.askyesno('Confirm exit', 'Are you sure you want to exit MDIA?')
    if dialog:
        destroy_window()

def showmessage(widget):
    msgbox.showinfo("Radio Button event", "You just clicked on Heyn's procedure")


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

    # initialize app entries
    w.Entry_line_length.insert(0,"100")
    w.Entry_Magnification.insert(0,"75")


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def load_file():
    """Load image file for edge segmentation"""
    path_name = filedialog.askopenfilename()
    image_analyzer.load_image(path_name)

    # display image on canvas
    canvas.setup(w, image_analyzer, image_prop)
    

def find_grains():
    """Performe image segmentation finding grains' constours and updating canvas.
       Returns an error if image was not loaded.
    """

    if not image_analyzer.img_loaded:
        msgbox.showerror('Grains segmentation','Image file has not been opened.')
    else:
        image_analyzer.find_grains()
        image_analyzer.draw_contours(fill_contours_chkbox.get())
        image_analyzer.set_image_for_canvas(image_analyzer.image_cv)
        canvas.update(w, image_analyzer)


def image_segmentation_procedure():
    """Command function for Apply button related to which radiobutton was choosed: Grains or Phases"""

    global RB_var_ISS
    procedure = RB_var_ISS.get()

    if procedure==0:
        find_grains()
    elif procedure==1:
        print("You have chose: Phases segmentation")
        # under_construction()

def metallographic_procedures():
    """Command function for Apply button related to which radiobutton was choosed: Planimetric, Heyns, etc"""
    global RB_var_MP, arr
    procedure = RB_var_MP.get()

    width, height = image_analyzer.get_image_dimensions()

    canvas.setup(w, image_analyzer, image_prop)
    canvas.update(w, image_analyzer)
    grain_list = []
    title = ""

    if procedure==0:
        inside_list, intercepted_list = jeffries.procedure(image_analyzer, w, image_prop)
        grain_list = intercepted_list
        title = "Jeffries's planimetric procedure"
    elif procedure==1:
        grain_list = heyn.procedure(width, height, image_analyzer, w)
        title = "Heyn's linear intercept procedure"
    elif procedure==2:
        grain_list = hilliard.procedure(width, height, image_analyzer, w, root)
        title = "Hilliard's Single-Circle Procedure procedure"
    elif procedure==3:
        abrams

    #     under_construction()
    # elif procedure==4:
    #     under_construction()


    # convert area from square pixels to square micrometer
    ratio = float(1/image_prop.ratio)**2 # pixel/um
    the_list = ratio*np.array(grain_list, dtype=float)

    gstat.plot_stat(the_list, root, win_title=title)


def statistics():
    # converts from pixels to mm2
    const = (1/2.83464566929133)**2
    # x = image_analyzer.grains_area
    # gstat.plot_stat(root, x)


def run():
    """Performs a statistical analysis over metallographic image using PLanimetric Jeffries procedure"""
    vec, n = jeffries.run_jeffries_analysis(image_analyzer, w, image_prop)
    gstat.plot_stat(vec, root, n_bins=n)



def image_data_set():
    """Take parameters for correct analysis: Magnification, scale, units"""

    # read data from Scale Window Dialog
    scale_win = swd.SWD(root, w.Canvas1)
    root.bind("<Motion>", lambda e: scale_win.callback_movement(e))
    root.bind("<Button-1>", lambda e: scale_win.callback_click(e))

    image_prop.M = float(w.Entry_Magnification.get())
    image_prop.er, image_prop.ep = scale_win.get()
    image_prop.width, image_prop.height = image_analyzer.get_image_dimensions()

    #  convert from in to micrometers
    if scale_btn.get()==0:
        image_prop.er = 25400.0*image_prop.er
    image_prop.set_ratio()


    # define some parameters
    image_prop.ha = image_prop.height/image_prop.ratio*image_prop.M
    image_prop.hr = image_prop.ha/image_prop.M

    # print on screen
    image_prop.print_data()

    # update canvas with real image properties
    canvas.setup(w, image_analyzer, image_prop)
    canvas.update(w, image_analyzer)

    # update Main Dialog window Label
    txt = "Scale: " + "{:.1f}".format(image_prop.er) + u'''\u03BC'''+'''m'''
    w.Label5.configure(text=txt)


def save_image_analysis():
    print("save image analysis")
    path = filedialog.asksaveasfile()
    image_prop.save(path.name, image_analyzer.image_original)


def load_image_analysis():
    print("save image analysis")
    path = filedialog.askopenfilename()
    image_prop.load(path)

    # path, here, is not necessary. What we need is to tell that the image comes from HDF5 file.
    image_analyzer.load_image(path,loaded_from_analysis=True, img=image_prop.image_original)
    canvas.setup(w, image_analyzer, image_prop)


def image_filter(the_filter):
    image_analyzer.set_image_filter(the_filter)
    image_analyzer.apply_filter_smooth_algorithms()
    image_analyzer.set_image_for_canvas(image_analyzer.image_filtered)
    canvas.update(w, image_analyzer)


def show_filtered_image():
    image_analyzer.set_image_for_canvas(image_analyzer.image_gray)
    # canvas_window.create(image_analyzer.image_canvas, image_analyzer.width, image_analyzer.height)


# def open_algorithm_window():
#     global w, top_level, root
#     # algorithm_window.create_AlgorithmWindow_Toplevel(root, top_level)

# def draw_histogram():
#     gray = image_analyzer.image_gray
#     if not image_analyzer.image_gray_exists:
#         gray = mdia.cv2.cvtColor(image_analyzer.image_original, mdia.cv2.COLOR_BGR2RGB)

#     mdia.plt.hist(gray.ravel(), 256, [0, 256])
#     mdia.plt.title('Histogram of original image in gray e_r.\n Filter: ' + image_analyzer.get_filter_name())
#     mdia.plt.show()


def create_histogram():
    """Creates a histogram for a specific data like grains or other structures sizes"""
    image_analyzer.grains_histogram()    


def metallografic_phases_analysis():
    p_analysis.start(root, w, w.Canvas1, image_analyzer)


def insert_circular_pattern():
    width, height = image_analyzer.get_image_dimensions()
    draw_pattern.circular(root, w.Canvas1, width, height)

if __name__ == '__main__':
    import gui_main
    gui_main.vp_start_gui()




# def callback(event):
#     pos1 = event.x-55
#     pos2 = event.y-55
#     w, h = image_analyzer.get_image_dimensions()

#     if pos1>=0 and pos2>=0:
#         img = image_analyzer.image_gray
#         pixel = img[pos2, pos1]
#         pixels_list.append(pixel)
#         mean = int(np.sum(pixels_list)/len(pixels_list))
#         print("(%d, %d) => pixel: %d, size: %d, mean: %d" % (pos1, pos2, pixel, len(pixels_list), mean))


# def pickup_pixel():
#     root.bind("<Button-1>", callback)

#     global pixels_list
#     pixels_list = []