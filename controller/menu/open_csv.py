
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import *

def select_file(target):
    filetypes = (
            ('csv', '*.csv'),
            ('All files', '*.*')
        )
    filename = fd.askopenfilename(
            title='Select datasource',
            initialdir='/',
            filetypes=filetypes)
    target.insert(END,filename)
