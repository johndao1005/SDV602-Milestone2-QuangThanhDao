
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt


def draw_graph(windowname, datatype,datasource =""):
    
    # ANCHOR prepare graph
    fig = Figure(figsize=(6, 6), dpi=100)
    a = fig.add_subplot(111)
    # data type plot in graph
    if datatype == "feature":
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]
        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars
        rects1 = a.bar(x - width/2, men_means, width, label='Men')
        rects2 = a.bar(x + width/2, women_means, width, label='Women')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        a.set_xlabel('year')
        a.set_xticks(x)
        a.set_xticklabels(labels)
        a.legend()

        a.bar_label(rects1, padding=3)
        a.bar_label(rects2, padding=3)

        a.plot()
        
    elif datatype == "gender":
        stockListExp = ['AMZN', 'AAPL', 'JETS', 'CCL', 'NCLH']
        stockSplitExp = [15, 25, 40, 10, 10]
        a.pie(stockSplitExp, radius=1, labels=stockListExp,
        autopct='%0.2f%%', shadow=True)
    
    elif datatype == "location":
        data = (20, 35, 30, 35, 27)

        ind = np.arange(5)  # the x locations for the groups
        width = .5
        a.bar(ind, data, width)
    # ANCHOR draw graph
    canvas = FigureCanvasTkAgg(fig, master=windowname)  # A tk.DrawingArea.
    canvas.draw()
    # ANCHOR Options for adding the tool in tool bar

    NavigationToolbar2Tk.toolitems = [t for t in NavigationToolbar2Tk.toolitems if t[0] not in (
        'Subplots', 'Back', 'Forward', 'Save')]
    # pack_toolbar=False will make it easier to use a layout manager later on.
    toolbar = NavigationToolbar2Tk(canvas, windowname, pack_toolbar=False)
    toolbar.update()
    canvas.get_tk_widget().grid(column=0, row=1, rowspan=4)  # create canvas
    toolbar.grid(column=0, row=6)  # create tool bar


if __name__ == "__main__":
    root = Tk()
    draw_graph(root, "location")
    root.mainloop()
