# -*- coding: utf-8 -*-
"""
UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
UNIDADE ACADÊMICA DO CABO DE SANTO AGOSTINHO - UACSA

@author(s):
    Rogério Soares (rogerio.soaress@ufrpe.br)
    
Created on Wed Apr 29 00:03:47 2020
"""


import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
import scipy.stats as scs
from matplotlib.figure import Figure
import numpy as np


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)
    
# global canvas    
# canvas.mpl_connect("key_press_event", on_key_press)
    
    
def _quit():
    stat_window.destroy()   # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate

def plot_stat(x, window, n_bins = 12, win_title="Statistics"):
    
    vec = np.array(x)

    global stat_window
    stat_window = tkinter.Toplevel(window)
    stat_window.wm_title(win_title)
    
    fig = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    ax = fig.add_subplot(111)
    
    
    n, bins, patches  = ax.hist(x, bins=n_bins, density=1, facecolor='blue', alpha=0.5)
    
    # add a 'best fit' line
    mu = np.mean(x)
    sigma = np.std(x)
    
    
    ax.set_xlabel(r'Grain area distribution $\left[\mu m^2\right]$')
    ax.plot(bins,scs.norm.pdf(bins, mu, sigma), '--', color='r', lw=1.4,label='$\mathcal{N}[0,1]$')
    ax.set_ylabel('Frequency (%)')
    fig.tight_layout()

    
    global canvas
    canvas = FigureCanvasTkAgg(fig, master=stat_window)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    
    global toolbar
    toolbar = NavigationToolbar2Tk(canvas, stat_window)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    button = tkinter.Button(master=stat_window, text="Quit", command=_quit)
    button.pack(side=tkinter.BOTTOM)
    
    