import tkinter as tk
from tkinter import ttk
import view.setup as setup

class DES1(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Graph Page")
        label.pack(pady=10,padx=10)
        
        # graph
        
        canvas = FigureCanvasTkAgg(f, self,)
        canvas.draw()
        
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack()
        canvas.get_tk_widget().pack(expand=True)
        
        # buttons
        button1 = ttk.Button(self, text ="Back To Home",
                            command=lambda:controller.show_frame(StartPage))
        button1.pack()