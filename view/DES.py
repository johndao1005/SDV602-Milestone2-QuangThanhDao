from tkinter import *
from tkinter import ttk
import view.setup as setup
from model.chart_create import draw_graph


class DES(Tk):
    def __init__(self, parent, datatype, next, prev,positionX ,positionY): #change to **kwrags
        super().__init__()
        Frame()
        self.parent =parent
        self.datatype = datatype
        self.title(setup.app_name)
        self.iconbitmap(setup.icon)
        label = Label(self, text=f"White shark {datatype} data").grid(column=0,row=0,**setup.pad20,columnspan=3)
        self.geometry(f"940x740+{positionX}+{positionY}")
        parent.DES_check.add(datatype)
        # ANCHOR data display
        draw_graph(self,datatype)
        # Storing new data
        input = StringVar()
        chatLog = StringVar()
        # chat box creating and function
        frame1 = ttk.LabelFrame(self,text="Chat box",borderwidth=0)
        frame1.grid(column=2,row=1,**setup.pad20,sticky = E)
        chatBox = ttk.Label(frame1,
                        background='light gray',
                        textvariable=chatLog,width = 40
                        ).grid(column=1,row=1,**setup.pad20,columnspan=2)
        entry = ttk.Entry(frame1, textvariable=input).grid(column=1,row=2,**setup.pad20,sticky = E)
        button = ttk.Button(frame1,
                        text="Send",
                        command=lambda: chat()
                        ).grid(column=2,row=2,**setup.pad20,sticky = E)
        # ANCHOR Buttons for self
        frame2 = ttk.LabelFrame(self,text="Chat box",borderwidth=0)
        frame2.grid(column=2,row=3,**setup.pad20,sticky=NSEW)
        button = ttk.Button(frame2,
                        text="Next",
                        command=lambda: self.changeWindow(next)
                        ).grid(column=0,row=4,**setup.pad20)
        button = ttk.Button(frame2,
                        text="Previous",
                        command=lambda: self.changeWindow(prev)
                        ).grid(column=1,row=4,**setup.pad20)
        button = ttk.Button(frame2,
                        text="Upload",
                        command=lambda: chat()
                        ).grid(column=1,row=5,**setup.pad20)
        button = ttk.Button(frame2,
                        text="Update",
                        command=lambda: chat()
                        ).grid(column=0,row=5,**setup.pad20)
        Location_self = ttk.Button(frame2,
                              text="upload Data",
                              command=lambda: chat()
                              ).grid(column=1,row=6,**setup.pad20)
        # button = Button(self,
        #                 text="upload Data",
        #                 command=lambda: chat()
        #                 ).grid(column=0,row=0,**setup.pad20)
        button = ttk.Button(self,
                        text="Quit",
                        command=lambda: self.close_DES()
                        ).grid(column=2,row=6,**setup.pad20,sticky=SE)
        self.protocol("WM_DELETE_WINDOW",self.close_DES)
        self.mainloop()
        
    def changeWindow(self,newWindow):
        self.destroy()
        newWindow()
        
    def close_DES(self):
        self.destroy()
        self.parent.DES_check.discard(self.datatype)