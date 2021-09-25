"""Data Explore Application
The program helps presenting as well as reading data regard the tagging of white shark
With the application user can view data in graph with matplotlib while enjoy the GUI navigation of Tkinter

"""

from view.menu import window

if __name__ == '__main__':
    """
    Initiate the app
    """
    dataView = window()
    dataView.mainloop()
    pass
    
