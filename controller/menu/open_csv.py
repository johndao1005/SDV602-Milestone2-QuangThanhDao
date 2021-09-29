
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import *

def selectFile(action,target):
    filetypes = (
            ('csv', '*.csv'),
        )
    filename = fd.askopenfilename(
            title='Select csv datasource',
            initialdir='./data-sample',
            filetypes=filetypes)
    if action =="merge":
        target.insert(END,filename)
    if action =="open":
        target.loadDES(filename)
