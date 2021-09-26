import tkinter as tk
from tkinter import ttk
from view.DES import DES1,DES2,DES3
import view.setup as setup
from tkinter.messagebox import showinfo

class dataView(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        #ANCHOR frame setup
        container =tk.Frame()
        container.pack(side = 'top',fill = 'both', expand = True)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)
        self.title(setup.app_name)
        self.iconbitmap(setup.icon)
        #ANCHOR menubar setup
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff = 0)
        # filemenu.add_command(label = "Choose data source",command = lambda: popupmsg("Not support yet"))
        filemenu.add_command(label = "Choose Data Source",command =lambda: showinfo("Oops","This function is developing in progress"))
        filemenu.add_command(label = "Edit data source",command =lambda: showinfo("Oops","This function is developing in progress"))
        filemenu.add_command(label = "Sign out",command =lambda: showinfo("Oops","This function is developing in progress"))
        filemenu.add_separator()
        filemenu.add_command(label = "Exit",command = quit)
        DESmenu = tk.Menu(menubar, tearoff = 0)
        DESmenu.add_command(label = "Gender",command = lambda: self.show_frame(DES1))
        DESmenu.add_separator()
        DESmenu.add_command(label = "Feature",command = lambda: self.show_frame(DES3))
        DESmenu.add_separator()
        DESmenu.add_command(label = "Location",command = lambda: self.show_frame(DES2))
        menubar.add_cascade(label = "File",menu=filemenu)
        menubar.add_cascade(label = "Data view",menu=DESmenu)
        
        tk.Tk.config(self,menu=menubar)
        #ANCHOR control DES
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
    app = dataView()
    app.geometry("940x740")
    app.mainloop()