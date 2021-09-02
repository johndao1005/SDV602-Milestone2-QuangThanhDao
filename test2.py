
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from tkinter import ttk
import numpy as np
from tkinter import *
def draw_graph(windowname,datatype):
    # ANCHOR data
    fig = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    
    # ANCHOR create graph
    fig.add_subplot().plot(t, 2 * np.sin(2 * np.pi * t))
    #draw graph
    canvas = FigureCanvasTkAgg(fig,master = windowname)  # A tk.DrawingArea.
    canvas.draw()
    #
    # pack_toolbar=False will make it easier to use a layout manager later on.
    toolbar = NavigationToolbar2Tk(canvas, windowname, pack_toolbar=False)
    toolbar.update()
    canvas.get_tk_widget().pack() # create canvas
    toolbar.pack(side=BOTTOM, fill=X)#create tool bar
    
# canvas.mpl_connect(
#     "key_press_event", lambda event: print(f"you pressed {event.key}"))
# canvas.mpl_connect("key_press_event", key_press_handler)
