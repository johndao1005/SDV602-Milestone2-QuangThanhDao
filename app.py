"""Data Explore Application
The program helps presenting as well as reading data regard the tagging of white shark
With the application user can view data in graph with matplotlib while enjoy the GUI navigation of Tkinter

"""

from view.dataView import dataView#.login import Login

if __name__ == '__main__':
    """
    Initiate the app
    """
    dataView = dataView()
    dataView.mainloop()
    pass
    
