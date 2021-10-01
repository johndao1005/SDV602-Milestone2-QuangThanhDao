"""Data Explore Application
The program helps presenting as well as reading data regard the tagging of white shark
With the application user can view data in graph with matplotlib while enjoy the GUI navigation of Tkinter

"""

from view.login import Login 
app = Login()

def start():
    """Function to jumpstart the application
    """
    app.mainloop()

if __name__ == '__main__':
    """
    Initiate the app
    """
    start()
