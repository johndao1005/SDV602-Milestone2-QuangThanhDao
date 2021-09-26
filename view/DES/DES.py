from model.chart_create import draw_graph
import tkinter as tk
from tkinter import ttk
import view.setup as setup


class DES(tk.Frame):
    def __init__(self, parent, controller):
        self.frametype = None
        self.nextDES = None
        self.prevDES = None
        tk.Frame.__init__(self, parent)

    def DES_setup(self,window, controller):
        next = self.nextDES
        prev = self.prevDES
        frame = self.frametype
        label = ttk.Label(window, text=f"White shark {frame} data").grid(
            column=0, row=0, **setup.pad20, columnspan=3)
        # graph
        draw_graph(window, frame)
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
                            command=lambda: controller.show_frame(next)
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
                            command=lambda: controller.show_frame(next)
                            ).grid(column=1, row=5, **setup.pad20)
        button = ttk.Button(frame2,
                            text="Update",
                            command=lambda: controller.show_frame(next)
                            ).grid(column=0, row=5, **setup.pad20)
        Location_self = ttk.Button(frame2,
                                text="upload Data",
                                command=lambda: controller.show_frame(next)
                                ).grid(column=1, row=6, **setup.pad20)
        button = ttk.Button(window,
                            text="Quit",
                            command=lambda: controller.destroy()).grid(column=2, row=4, **setup.pad20)

# inherit from DES
class genderDES(DES):
    def __init__(self, parent, controller):
        DES.__init__(self, parent,controller)
        self.nextDES = locationDES
        self.prevDES = featureDES
        self.frametype = "gender"
        self.DES_setup(self, controller)


class locationDES(DES):
    def __init__(self, parent, controller):
        DES.__init__(self, parent,controller)
        self.nextDES = featureDES
        self.prevDES = genderDES
        self.frametype = "location"
        self.DES_setup(self, controller)


class featureDES(DES):
    def __init__(self, parent, controller):
        DES.__init__(self, parent,controller)
        self.nextDES = genderDES
        self.prevDES = locationDES
        self.frametype = "feature"
        self.DES_setup(self, controller)
