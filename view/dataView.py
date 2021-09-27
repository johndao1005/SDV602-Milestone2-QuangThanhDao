import tkinter as tk
from tkinter import ttk
from view.DES.DES import genderDES,locationDES,featureDES
import view.setup as setup
from tkinter.messagebox import showinfo

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
        filemenu.add_command(label = "Choose Data Source",command =lambda: self.openUpload())
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
        

    def uploadWindow(self):
        """
        """
        self.check = True
        self.upload = tk.Toplevel()
        self.upload.title(setup.app_name)
        self.upload.iconbitmap(setup.icon)
        options = {'padx': 10, 'pady': 5}
        label = ttk.Label(self.signup, text="Sign up").grid(
            column=0, row=0, **options, columnspan=2)
        self.upload.geometry("310x360+100+100")
        self.upload.protocol("WM_DELETE_WINDOW", self.closeUpload)
        options = setup.pad5
        self.resizable(0, 0)
        label = ttk.Label(self, text="Upload").grid(column=0,row=0,sticky="N",**options,columnspan=3)
        self.geometry("420x220+200+300")
        lf = ttk.LabelFrame(self,text="Merge Data").grid(column=0, row=1, padx=10, pady=0)
        target = tk.StringVar()
        source = tk.StringVar()
        label = ttk.Label(lf, text="Target File").grid(column=0,row=2,**options)
        username_entry = ttk.Entry(lf, textvariable=target).grid(column=1,row=2,**options,columnspan=3)
        label = ttk.Label(lf, text="Source File").grid(column=0,row=3,**options)
        password_entry = ttk.Entry(lf, textvariable=source).grid(column=1,row=3,**options,columnspan=3)
        browse_file = ttk.Button(lf,
                            text="Select",
                            command=lambda: self.destroy()
                            ).grid(column=4,row=2,**setup.pad10)
        browse_file = ttk.Button(lf,
                          text="Select",
                          command=lambda: self.destroy()
                          ).grid(column=4,row=3,**setup.pad10)
        merge_btn = ttk.Button(lf,
                            text="Merge",
                            command=lambda: self.destroy()
                            ).grid(column=1,row=4,**setup.pad10)
        quit_btn = ttk.Button(lf,
                          text="Quit",
                          command=lambda: self.closeUpload()
                          ).grid(column=2,row=4,**setup.pad10)
        self.upload.mainloop()
        
    def openUpload(self):
        if self.check == False:
            self.uploadWindow()
            
    def closeUpload(self):
        self.check = False
        self.upload.destroy()
        
if __name__ == "__main__":    
    app = dataView()
    app.geometry("940x740+0+0")
    app.mainloop()