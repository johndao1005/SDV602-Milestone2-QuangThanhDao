import tkinter as tk
from tkinter import ttk
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text="STart Page")
        label.pack(pady=10,padx=10)
        # button1 = ttk.Button(self, text ="Visit Page 1",
        #                     command=lambda:controller.show_frame(PageOne))
        # button1.pack()
        # button2 = ttk.Button(self, text ="Visit Page 2",
        #                     command=lambda:controller.show_frame(PageTwo))
        # button2.pack()
        # button3 = ttk.Button(self, text ="Visit Page 3",
        #                     command=lambda:controller.show_frame(PageThree))
        # button3.pack()
        # button4 = ttk.Button(self, text ="Visit Page 4",
        #                     command=lambda:controller.show_frame(PageOne))
        # button4.pack()