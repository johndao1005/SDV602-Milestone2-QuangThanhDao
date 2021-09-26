
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt

def draw_graph(windowname, datatype):
    # ANCHOR data
    if datatype == "feature":
        fig = Figure(figsize=(6,6), dpi=100)
        a = fig.add_subplot(111)
        t = np.arange(0, 3, .01)
        # create graph
        a.plot(t, 2 * np.sin(4 * np.pi * t))
    elif datatype == "gender":
        fig = Figure(figsize=(6,6), dpi=100)
        a = fig.add_subplot(111)
        a.plot()
    elif datatype == "location":
        fig = Figure(figsize=(6,6), dpi=100)
        a = fig.add_subplot(111)
        a.plot([-100.1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    #ANCHOR draw graph
    canvas = FigureCanvasTkAgg(fig, master=windowname)  # A tk.DrawingArea.
    canvas.draw()
    #ANCHOR Options for adding the tool in tool bar 

    NavigationToolbar2Tk.toolitems = [t for t in NavigationToolbar2Tk.toolitems if t[0] not in ('Subplots','Back', 'Forward','Save')]
    # pack_toolbar=False will make it easier to use a layout manager later on.
    toolbar = NavigationToolbar2Tk(canvas, windowname, pack_toolbar=False)
    toolbar.update()
    canvas.get_tk_widget().grid(column=0, row=1,rowspan=4)  # create canvas
    toolbar.grid(column=0, row=6)  # create tool bar
if __name__ == "__main__":
    root = Tk()
    draw_graph(root,"location")
    root.mainloop()