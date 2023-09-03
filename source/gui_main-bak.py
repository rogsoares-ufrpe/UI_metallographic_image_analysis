#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.1
#  in conjunction with Tcl version 8.6
#    Apr 29, 2020 12:00:31 AM -03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gui_main_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    gui_main_support.set_Tk_var()
    top = MainWindow (root)
    gui_main_support.init(root, top)
    root.mainloop()

w = None
def create_MainWindow(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_MainWindow(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    gui_main_support.set_Tk_var()
    top = MainWindow (w)
    gui_main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_MainWindow():
    global w
    w.destroy()
    w = None

class MainWindow:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 9"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1200x710+479+110")
        top.minsize(166, 1)
        top.maxsize(1924, 1041)
        top.resizable(0, 0)
        top.title("MDIA - Metallographic Image Analyzer")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="File")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=gui_main_support.load_file,
                font="TkMenuFont",
                foreground="#000000",
                label="Load Image")
        self.sub_menu.add_separator(
                background="#d9d9d9")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=gui_main_support.quit_app,
                font="TkMenuFont",
                foreground="#000000",
                label="Quit")
        self.sub_menu1 = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Segmentation")
        self.sub_menu1.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=gui_main_support.find_grains,
                font="TkMenuFont",
                foreground="#000000",
                label="Grains")
        self.sub_menu1.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Phases")
        self.sub_menu1.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=gui_main_support.grains_histogram,
                font="TkMenuFont",
                foreground="#000000",
                label="Grains histogram")
        self.sub_menu12 = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu12,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Statistics")
        self.sub_menu12.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=gui_main_support.run,
                font="TkMenuFont",
                foreground="#000000",
                label="Run Jeffries Planimetric")
        self.sub_menu12.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=gui_main_support.draw_histogram,
                font="TkMenuFont",
                foreground="#000000",
                label="Gray Image Histogram")
        self.sub_menu12.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=gui_main_support.show_filtered_image,
                font="TkMenuFont",
                foreground="#000000",
                label="Show filtered image")
        self.sub_menu123 = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu123,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Help")
        self.sub_menu123.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=gui_main_support.about,
                font="TkMenuFont",
                foreground="#000000",
                label="About")

        # self.style.configure('TNotebook.Tab', background=_bgcolor)
        # self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        # self.style.map('TNotebook.Tab', background=
        #     [('selected', _compcolor), ('active',_ana2color)])
        # self.TNB_main = ttk.Notebook(top)
        # self.TNB_main.place(relx=0.0, rely=0.0, relheight=1.014, relwidth=1.0)
        # self.TNB_main.configure(takefocus="")
        # self.TNB_main_t0 = tk.Frame(self.TNB_main)
        # self.TNB_main.add(self.TNB_main_t0, padding=3)
        # self.TNB_main.tab(0, text="Image Analysis", compound="left"
        #         ,underline="-1", )
        # self.TNB_main_t0.configure(background="#d9d9d9")
        # self.TNB_main_t0.configure(highlightbackground="#d9d9d9")
        # self.TNB_main_t0.configure(highlightcolor="black")
        # self.TNB_main_Statistics = tk.Frame(self.TNB_main)
        # self.TNB_main.add(self.TNB_main_Statistics, padding=3)
        # self.TNB_main.tab(1, text="Statistics",compound="left",underline="-1",)
        # self.TNB_main_Statistics.configure(background="#d9d9d9")
        # self.TNB_main_Statistics.configure(highlightbackground="#d9d9d9")
        # self.TNB_main_Statistics.configure(highlightcolor="black")

        # self.Frame1 = tk.Frame(self.TNB_main_t0)
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=0.994, relwidth=0.995)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(self.Frame1)
        self.Canvas1.place(relx=0.008, rely=0.014, relheight=0.913
                , relwidth=0.782)
        self.Canvas1.configure(background="#f0ffff")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")

        self.Labelframe2 = tk.LabelFrame(self.Frame1)
        self.Labelframe2.place(relx=0.798, rely=0.377, relheight=0.341
                , relwidth=0.192)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Metallographic procedures''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")

        self.RB_Procedure_Planimetric = tk.Radiobutton(self.Labelframe2)
        self.RB_Procedure_Planimetric.place(relx=0.044, rely=0.085
                , relheight=0.106, relwidth=0.281, bordermode='ignore')
        self.RB_Procedure_Planimetric.configure(activebackground="#ececec")
        self.RB_Procedure_Planimetric.configure(activeforeground="#000000")
        self.RB_Procedure_Planimetric.configure(background="#d9d9d9")
        self.RB_Procedure_Planimetric.configure(disabledforeground="#a3a3a3")
        self.RB_Procedure_Planimetric.configure(foreground="#000000")
        self.RB_Procedure_Planimetric.configure(highlightbackground="#d9d9d9")
        self.RB_Procedure_Planimetric.configure(highlightcolor="black")
        self.RB_Procedure_Planimetric.configure(justify='left')
        self.RB_Procedure_Planimetric.configure(text='''Jeffries''')
        self.RB_Procedure_Planimetric.configure(value="0")
        self.RB_Procedure_Planimetric.configure(variable=gui_main_support.RB_var_MP)
        tooltip_font = "-family {Segoe UI} -size 9"
        ToolTip(self.RB_Procedure_Planimetric, tooltip_font, '''It involves 
an actual count of the number of grains within a known
area. The number of grains per unit area, NA , is used to
determine the ASTM grain size number, G.''', delay=0.5)

        self.Button1 = tk.Button(self.Labelframe2)
        self.Button1.place(relx=0.395, rely=0.809, height=31, width=50
                , bordermode='ignore')
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=gui_main_support.metallographic_procedures)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''OK''')

        self.Radiobutton5 = tk.Radiobutton(self.Labelframe2)
        self.Radiobutton5.place(relx=0.044, rely=0.191, relheight=0.106
                , relwidth=0.246, bordermode='ignore')
        self.Radiobutton5.configure(activebackground="#ececec")
        self.Radiobutton5.configure(activeforeground="#000000")
        self.Radiobutton5.configure(background="#d9d9d9")
        self.Radiobutton5.configure(disabledforeground="#a3a3a3")
        self.Radiobutton5.configure(foreground="#000000")
        self.Radiobutton5.configure(highlightbackground="#d9d9d9")
        self.Radiobutton5.configure(highlightcolor="black")
        self.Radiobutton5.configure(justify='left')
        self.Radiobutton5.configure(text='''Heyn''')
        self.Radiobutton5.configure(value="1")
        self.Radiobutton5.configure(variable=gui_main_support.RB_var_MP)

        self.Radiobutton6 = tk.Radiobutton(self.Labelframe2)
        self.Radiobutton6.place(relx=0.044, rely=0.591, relheight=0.106
                , relwidth=0.596, bordermode='ignore')
        self.Radiobutton6.configure(activebackground="#ececec")
        self.Radiobutton6.configure(activeforeground="#000000")
        self.Radiobutton6.configure(background="#d9d9d9")
        self.Radiobutton6.configure(disabledforeground="#a3a3a3")
        self.Radiobutton6.configure(foreground="#000000")
        self.Radiobutton6.configure(highlightbackground="#d9d9d9")
        self.Radiobutton6.configure(highlightcolor="black")
        self.Radiobutton6.configure(justify='left')
        self.Radiobutton6.configure(text='''Hilliard Single-Circle''')
        self.Radiobutton6.configure(value="2")
        self.Radiobutton6.configure(variable=gui_main_support.RB_var_MP)

        self.Radiobutton2 = tk.Radiobutton(self.Labelframe2)
        self.Radiobutton2.place(relx=0.044, rely=0.685, relheight=0.106
                , relwidth=0.596, bordermode='ignore')
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''Abrams Three-Circle''')
        self.Radiobutton2.configure(value="3")
        self.Radiobutton2.configure(variable=gui_main_support.RB_var_MP)

        self.Spinbox_number_lines = tk.Spinbox(self.Labelframe2, from_=1.0, to=10.0)
        self.Spinbox_number_lines.place(relx=0.614, rely=0.285, relheight=0.081
                , relwidth=0.132, bordermode='ignore')
        self.Spinbox_number_lines.configure(activebackground="#f9f9f9")
        self.Spinbox_number_lines.configure(background="white")
        self.Spinbox_number_lines.configure(buttonbackground="#d9d9d9")
        self.Spinbox_number_lines.configure(disabledforeground="#a3a3a3")
        self.Spinbox_number_lines.configure(font="TkDefaultFont")
        self.Spinbox_number_lines.configure(foreground="black")
        self.Spinbox_number_lines.configure(highlightbackground="black")
        self.Spinbox_number_lines.configure(highlightcolor="black")
        self.Spinbox_number_lines.configure(insertbackground="black")
        self.Spinbox_number_lines.configure(selectbackground="#c4c4c4")
        self.Spinbox_number_lines.configure(selectforeground="black")

        self.Label1 = tk.Label(self.Labelframe2)
        self.Label1.place(relx=0.175, rely=0.285, height=21, width=91
                , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Number of lines''')

        self.Label2 = tk.Label(self.Labelframe2)
        self.Label2.place(relx=0.175, rely=0.383, height=21, width=70
                , bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Lines length''')

        self.Entry_line_length = tk.Entry(self.Labelframe2)
        self.Entry_line_length.place(relx=0.614, rely=0.383, height=20
                , relwidth=0.132, bordermode='ignore')
        self.Entry_line_length.configure(background="white")
        self.Entry_line_length.configure(disabledforeground="#a3a3a3")
        self.Entry_line_length.configure(font="-family {Courier New} -size 10")
        self.Entry_line_length.configure(foreground="#000000")
        self.Entry_line_length.configure(highlightbackground="#d9d9d9")
        self.Entry_line_length.configure(highlightcolor="black")
        self.Entry_line_length.configure(insertbackground="black")
        self.Entry_line_length.configure(selectbackground="#c4c4c4")
        self.Entry_line_length.configure(selectforeground="black")

        self.Label3 = tk.Label(self.Labelframe2)
        self.Label3.place(relx=0.746, rely=0.383, height=21, width=28
                , bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''mm''')

        self.CheckBtn_free_orientation = tk.Checkbutton(self.Labelframe2)
        self.CheckBtn_free_orientation.place(relx=0.175, rely=0.468
                , relheight=0.106, relwidth=0.487, bordermode='ignore')
        self.CheckBtn_free_orientation.configure(activebackground="#ececec")
        self.CheckBtn_free_orientation.configure(activeforeground="#000000")
        self.CheckBtn_free_orientation.configure(background="#d9d9d9")
        self.CheckBtn_free_orientation.configure(disabledforeground="#a3a3a3")
        self.CheckBtn_free_orientation.configure(foreground="#000000")
        self.CheckBtn_free_orientation.configure(highlightbackground="#d9d9d9")
        self.CheckBtn_free_orientation.configure(highlightcolor="black")
        self.CheckBtn_free_orientation.configure(justify='left')
        self.CheckBtn_free_orientation.configure(text='''Free orientation''')
        self.CheckBtn_free_orientation.configure(variable=gui_main_support.chkbtn_free_orientation)
        tooltip_font = "-family {Segoe UI} -size 9"
        ToolTip(self.CheckBtn_free_orientation, tooltip_font, '''Click on image to trace straight lines with random orientation''', delay=0.5)

        self.Labelframe3 = tk.LabelFrame(self.Frame1)
        self.Labelframe3.place(relx=0.798, rely=0.201, relheight=0.152
                , relwidth=0.193)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''Image structure segmetation''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="black")

        self.Button2 = tk.Button(self.Labelframe3)
        self.Button2.place(relx=0.391, rely=0.571, height=31, width=50
                , bordermode='ignore')
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=gui_main_support.image_segmentation_procedure)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''OK''')

        self.RB_Grains = tk.Radiobutton(self.Labelframe3)
        self.RB_Grains.place(relx=0.043, rely=0.19, relheight=0.238
                , relwidth=0.265, bordermode='ignore')
        self.RB_Grains.configure(activebackground="#ececec")
        self.RB_Grains.configure(activeforeground="#000000")
        self.RB_Grains.configure(background="#d9d9d9")
        self.RB_Grains.configure(disabledforeground="#a3a3a3")
        self.RB_Grains.configure(foreground="#000000")
        self.RB_Grains.configure(highlightbackground="#d9d9d9")
        self.RB_Grains.configure(highlightcolor="black")
        self.RB_Grains.configure(justify='left')
        self.RB_Grains.configure(text='''Grains''')
        self.RB_Grains.configure(value="0")
        self.RB_Grains.configure(variable=gui_main_support.RB_var_ISS)

        self.RB_Phases = tk.Radiobutton(self.Labelframe3)
        self.RB_Phases.place(relx=0.043, rely=0.381, relheight=0.238
                , relwidth=0.278, bordermode='ignore')
        self.RB_Phases.configure(activebackground="#ececec")
        self.RB_Phases.configure(activeforeground="#000000")
        self.RB_Phases.configure(background="#d9d9d9")
        self.RB_Phases.configure(disabledforeground="#a3a3a3")
        self.RB_Phases.configure(foreground="#000000")
        self.RB_Phases.configure(highlightbackground="#d9d9d9")
        self.RB_Phases.configure(highlightcolor="black")
        self.RB_Phases.configure(justify='left')
        self.RB_Phases.configure(text='''Phases''')
        self.RB_Phases.configure(value="1")
        self.RB_Phases.configure(variable=gui_main_support.RB_var_ISS)

        self.Checkbutton1 = tk.Checkbutton(self.Labelframe3)
        self.Checkbutton1.place(relx=0.348, rely=0.19, relheight=0.238
                , relwidth=0.439, bordermode='ignore')
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Fill contours''')
        self.Checkbutton1.configure(variable=gui_main_support.fill_contours_chkbox)

        self.Labelframe1 = tk.LabelFrame(self.Frame1)
        self.Labelframe1.place(relx=0.008, rely=0.928, relheight=0.058
                , relwidth=0.782)
        self.Labelframe1.configure(relief='flat')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(relief="flat")
        self.Labelframe1.configure(text='''Image directory:''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Label_FNP = tk.Label(self.Labelframe1)
        self.Label_FNP.place(relx=0.004, rely=0.425, height=25, width=894
                , bordermode='ignore')
        self.Label_FNP.configure(activebackground="#f9f9f9")
        self.Label_FNP.configure(activeforeground="black")
        self.Label_FNP.configure(anchor='w')
        self.Label_FNP.configure(background="#d9d9d9")
        self.Label_FNP.configure(disabledforeground="#a3a3a3")
        self.Label_FNP.configure(foreground="#000000")
        self.Label_FNP.configure(highlightbackground="#d9d9d9")
        self.Label_FNP.configure(highlightcolor="black")
        self.Label_FNP.configure(justify='right')
        self.Label_FNP.configure(text='''File name path''')

        self.Labelframe6 = tk.LabelFrame(self.Frame1)
        self.Labelframe6.place(relx=0.801, rely=0.014, relheight=0.167
                , relwidth=0.185)
        self.Labelframe6.configure(relief='groove')
        self.Labelframe6.configure(foreground="black")
        self.Labelframe6.configure(text='''Image data''')
        self.Labelframe6.configure(background="#d9d9d9")
        self.Labelframe6.configure(highlightbackground="#d9d9d9")
        self.Labelframe6.configure(highlightcolor="black")

        self.Label4 = tk.Label(self.Labelframe6)
        self.Label4.place(relx=0.045, rely=0.174, height=21, width=80
                , bordermode='ignore')
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Magnification''')

        self.Entry_Magnification = tk.Entry(self.Labelframe6)
        self.Entry_Magnification.place(relx=0.455, rely=0.174, height=20
                , relwidth=0.182, bordermode='ignore')
        self.Entry_Magnification.configure(background="white")
        self.Entry_Magnification.configure(disabledforeground="#a3a3a3")
        self.Entry_Magnification.configure(font="-family {Courier New} -size 10")
        self.Entry_Magnification.configure(foreground="#000000")
        self.Entry_Magnification.configure(highlightbackground="#d9d9d9")
        self.Entry_Magnification.configure(highlightcolor="black")
        self.Entry_Magnification.configure(insertbackground="black")
        self.Entry_Magnification.configure(selectbackground="#c4c4c4")
        self.Entry_Magnification.configure(selectforeground="black")

        self.Label5 = tk.Label(self.Labelframe6)
        self.Label5.place(relx=0.045, rely=0.391, height=21, width=89
                , bordermode='ignore')
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Scale: unknown''')
        tooltip_font = "-family {Segoe UI} -size 9"
        ToolTip(self.Label5, tooltip_font, '''Click on two end points scale to inform length (in) or (mm)''', delay=0.5)

        self.Label6 = tk.Label(self.Labelframe6)
        self.Label6.place(relx=0.636, rely=0.174, height=21, width=13
                , bordermode='ignore')
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''X''')

        self.Button3 = tk.Button(self.Labelframe6)
        self.Button3.place(relx=0.045, rely=0.609, height=24, width=112
                , bordermode='ignore')
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(command=gui_main_support.image_data_set)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Get from image''')

        self.RBtn_inches = tk.Radiobutton(self.Labelframe6)
        self.RBtn_inches.place(relx=0.568, rely=0.609, relheight=0.217
                , relwidth=0.173, bordermode='ignore')
        self.RBtn_inches.configure(activebackground="#ececec")
        self.RBtn_inches.configure(activeforeground="#000000")
        self.RBtn_inches.configure(background="#d9d9d9")
        self.RBtn_inches.configure(disabledforeground="#a3a3a3")
        self.RBtn_inches.configure(foreground="#000000")
        self.RBtn_inches.configure(highlightbackground="#d9d9d9")
        self.RBtn_inches.configure(highlightcolor="black")
        self.RBtn_inches.configure(justify='left')
        self.RBtn_inches.configure(text='''(in)''')
        self.RBtn_inches.configure(value="0")
        self.RBtn_inches.configure(variable=gui_main_support.scale_btn)

        self.RBtn_millimeters = tk.Radiobutton(self.Labelframe6)
        self.RBtn_millimeters.place(relx=0.75, rely=0.609, relheight=0.217
                , relwidth=0.218, bordermode='ignore')
        self.RBtn_millimeters.configure(activebackground="#ececec")
        self.RBtn_millimeters.configure(activeforeground="#000000")
        self.RBtn_millimeters.configure(background="#d9d9d9")
        self.RBtn_millimeters.configure(disabledforeground="#a3a3a3")
        self.RBtn_millimeters.configure(foreground="#000000")
        self.RBtn_millimeters.configure(highlightbackground="#d9d9d9")
        self.RBtn_millimeters.configure(highlightcolor="black")
        self.RBtn_millimeters.configure(justify='left')
        self.RBtn_millimeters.configure(text='''(mm)''')
        self.RBtn_millimeters.configure(value="1")
        self.RBtn_millimeters.configure(variable=gui_main_support.scale_btn)

        self.Button_create_stat = tk.Button(self.Frame1)
        self.Button_create_stat.place(relx=0.798, rely=0.739, height=31
                , width=97)
        self.Button_create_stat.configure(activebackground="#ececec")
        self.Button_create_stat.configure(activeforeground="#000000")
        self.Button_create_stat.configure(background="#d9d9d9")
        self.Button_create_stat.configure(disabledforeground="#a3a3a3")
        self.Button_create_stat.configure(foreground="#000000")
        self.Button_create_stat.configure(highlightbackground="#d9d9d9")
        self.Button_create_stat.configure(highlightcolor="black")
        self.Button_create_stat.configure(pady="0")
        self.Button_create_stat.configure(text='''Create Statistics''')

        self.Button_create_stat = tk.Button(self.Frame1)
        self.Button_create_stat.place(relx=0.857, rely=0.754, height=31
                , width=97)
        self.Button_create_stat.configure(activebackground="#ececec")
        self.Button_create_stat.configure(activeforeground="#000000")
        self.Button_create_stat.configure(background="#d9d9d9")
        self.Button_create_stat.configure(disabledforeground="#a3a3a3")
        self.Button_create_stat.configure(foreground="#000000")
        self.Button_create_stat.configure(highlightbackground="#d9d9d9")
        self.Button_create_stat.configure(highlightcolor="black")
        self.Button_create_stat.configure(pady="0")
        self.Button_create_stat.configure(text='''Create Statistics''')
        self.Button_create_stat.configure(command=gui_main_support.statistics)

        # self.Frame_Stat = tk.Frame(self.TNB_main_Statistics)
        # self.Frame_Stat.place(relx=0.004, rely=0.0, relheight=0.937
        #         , relwidth=0.995)
        # self.Frame_Stat.configure(relief='groove')
        # self.Frame_Stat.configure(borderwidth="2")
        # self.Frame_Stat.configure(relief="groove")
        # self.Frame_Stat.configure(background="#d9d9d9")
        # self.Frame_Stat.configure(highlightbackground="#d9d9d9")
        # self.Frame_Stat.configure(highlightcolor="black")

        # self.Canvas_Stat = tk.Canvas(self.Frame_Stat)
        # self.Canvas_Stat.place(relx=0.017, rely=0.031, relheight=0.712
        #         , relwidth=0.566)
        # self.Canvas_Stat.configure(background="#ffffff")
        # self.Canvas_Stat.configure(borderwidth="2")
        # self.Canvas_Stat.configure(insertbackground="black")
        # self.Canvas_Stat.configure(relief="ridge")
        # self.Canvas_Stat.configure(selectbackground="#c4c4c4")
        # self.Canvas_Stat.configure(selectforeground="black")

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




