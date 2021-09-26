import tkinter as tk
from upload import StartPage
from setup import PageOne

class App(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        super().__init__()
        
        container.pack(side = 'top',fill = 'both', expand = True)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)
        
        self.frames ={}
        for Frame in (StartPage,PageOne):#,PageOne,PageTwo,PageThree):
            frame = Frame(container, self)
            self.frames[Frame] = frame
            frame.grid(row=0,column = 0, sticky = "nsew")
        self.show_frame(StartPage)
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
        
if __name__ == "__main__":    
    app = App()
    app.geometry("1280x720")
    #ani = animation.FuncAnimation(f,animate, interval = 5000)
    app.mainloop()