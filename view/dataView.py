import tkinter as tk
from tkinter import ttk
from view.DES.DES import genderDES,locationDES,featureDES
import view.setup as setup
from tkinter.messagebox import showinfo
from controller.openWindow import openTopwindow
from view.DES.upload import Upload

class dataView(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.geometry("940x740+0+0")
        #ANCHOR frame setup
        self.container =tk.Frame()
        self.container.grid(column=0, row=0)
        self.container.grid_rowconfigure(0,weight = 1)
        self.container.grid_columnconfigure(0,weight = 1)
        self.title(setup.app_name)
        self.iconbitmap(setup.icon)
        self.check = False
        #ANCHOR menubar setup
        menubar = tk.Menu(self.container)
        filemenu = tk.Menu(menubar, tearoff = 0)
        # filemenu.add_command(label = "Choose data source",command = lambda: popupmsg("Not support yet"))
        filemenu.add_command(label = "Choose Data Source",command =lambda: openTopwindow(Upload(self),self))
        filemenu.add_command(label = "Edit data source",command =lambda: showinfo("Oops","This function is developing in progress"))
        filemenu.add_command(label = "Sign out",command =lambda: showinfo("Oops","This function is developing in progress"))
        filemenu.add_separator()
        filemenu.add_command(label = "Exit",command = quit)
        DESmenu = tk.Menu(menubar, tearoff = 0)
        DESmenu.add_command(label = "Gender",command = lambda: self.show_frame(genderDES))
        DESmenu.add_separator()
        DESmenu.add_command(label = "Feature",command = lambda: self.show_frame(featureDES))
        DESmenu.add_separator()
        DESmenu.add_command(label = "Location",command = lambda: self.show_frame(locationDES))
        menubar.add_cascade(label = "File",menu=filemenu)
        menubar.add_cascade(label = "Data view",menu=DESmenu)
        
        tk.Tk.config(self,menu=menubar)
        self.frames ={}
        self.loadDES()
    #ANCHOR load all DES
    def loadDES(self):
        for DES in (genderDES,locationDES,featureDES):
            frame = DES(self.container, self)
            self.frames[DES] = frame
            frame.grid(row=0,column = 0, sticky = "nsew")
        self.show_frame(locationDES)
        
    def show_frame(self,newFrame):
        frame = self.frames[newFrame]
        frame.tkraise()
        
if __name__ == "__main__":    
    app = dataView()
    app.geometry("940x740+0+0")
    app.mainloop()