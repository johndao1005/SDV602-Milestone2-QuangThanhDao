import tkinter as tk
from tkinter import ttk
from view.DES1 import DES1,DES2,DES3
import view.setup as setup

class DES(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container =tk.Frame()
        container.pack(side = 'top',fill = 'both', expand = True)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)
        self.title(setup.app_name)
        self.iconbitmap(setup.icon)
        self.frames ={}
        for DES in (DES1,DES2,DES3):
            frame = DES(container, self)
            self.frames[DES] = frame
            frame.grid(row=0,column = 0, sticky = "nsew")
        self.show_frame(DES1)
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
        
if __name__ == "__main__":    
    app = DES()
    app.geometry("940x740")
    #ani = animation.FuncAnimation(f,animate, interval = 5000)
    app.mainloop()