import tkinter as tk
from tkinter import ttk
import view.setup as setup

class Upload(tk.Tk):
    def __init__(self,controller):
        """Start an instance of login screen which allow user to sign up with top level window or login directly
        When users login, the class would open to menu which is another class which handle the data view, update, delete while
        destroy the current login to prevent multiple login.
        """
        tk.Tk.__init__(self)
        self.title(setup.app_name)
        self.iconbitmap(setup.icon)
        controller.check = True
        self.controller = controller
        self.protocol("WM_DELETE_WINDOW", self.closeToplevel)
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
                          command=lambda: self.closeToplevel(self,controller)
                          ).grid(column=2,row=4,**setup.pad10)
        self.mainloop()
    def closeToplevel(self):
        self.controller.check = False
        self.destroy()