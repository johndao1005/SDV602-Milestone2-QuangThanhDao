from view.upload import StartPage
from view.login import Login
from view.menu import Menu
from view.setup import PageOne
import tkinter as tk
class App(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame()
        container.grid(row=0,column = 0,)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)
        
        self.frames ={}
        for Frame in (Login,Menu):#,PageOne,PageTwo,PageThree):
            frame = Frame(container, self)
            self.frames[Frame] = frame
            frame.grid(row=0,column = 0, sticky = "nsew")
        self.show_frame(Login)
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
        
if __name__ == "__main__":    
    app = App()
    app.geometry("1280x720")
    #ani = animation.FuncAnimation(f,animate, interval = 5000)
    app.mainloop()