from model.chart_create import draw_graph
import tkinter as tk
from tkinter import ttk
import view.setup as setup

class DES1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        DES_setup(self,controller,"gender",DES2,DES3)


class DES2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        DES_setup(self,controller,"location",DES3,DES1)


class DES3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        DES_setup(self,controller,"feature",DES1,DES2)


def DES_setup(window,controller,datatype,next,prev):
    label = ttk.Label(window, text=f"White shark {datatype} data").grid(
        column=0, row=0, **setup.pad20, columnspan=3)
    # graph
    draw_graph(window, datatype)
    input = tk.StringVar()
    chatLog = tk.StringVar()
    # chat box creating and function
    frame1 = ttk.LabelFrame(window, text="Chat box", borderwidth=0)
    frame1.grid(column=2, row=1, **setup.pad20, sticky="E")
    chatBox = ttk.Label(frame1,
                        background='light gray',
                        textvariable=chatLog, width=40
                        ).grid(column=1, row=1, **setup.pad20, columnspan=2)
    entry = ttk.Entry(frame1, textvariable=input).grid(
        column=1, row=2, **setup.pad20, sticky="E")
    button = ttk.Button(frame1,
                        text="Send",
                        command=lambda: chat()
                        ).grid(column=2, row=2, **setup.pad20, sticky="E")
    # ANCHOR Buttons for self
    frame2 = ttk.LabelFrame(window, text="Control box", borderwidth=0)
    frame2.grid(column=2, row=3, **setup.pad20, sticky="NSEW")
    button = ttk.Button(frame2,
                        text="Next",
                        command=lambda: controller.show_frame(next)
                        ).grid(column=0, row=4, **setup.pad20)
    button = ttk.Button(frame2,
                        text="Previous",
                        command=lambda: controller.show_frame(prev)
                        ).grid(column=1, row=4, **setup.pad20)
    button = ttk.Button(frame2,
                        text="Upload",
                        command=lambda: chat()
                        ).grid(column=1, row=5, **setup.pad20)
    button = ttk.Button(frame2,
                        text="Update",
                        command=lambda: chat()
                        ).grid(column=0, row=5, **setup.pad20)
    Location_self = ttk.Button(frame2,
                               text="upload Data",
                               command=lambda: chat()
                               ).grid(column=1, row=6, **setup.pad20)
    button = ttk.Button(window,
                        text="Quit",
                        command=lambda: controller.destroy()).grid(column=2, row=4, **setup.pad20)
