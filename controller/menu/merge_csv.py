from model.model import Model
import os
from tkinter.messagebox import showerror,showinfo

def mergeFiles(source,target,window):
    if source =="" or target=="":
        showerror("Error","Please select two files to merge")
    else:
        dataControl = Model()
        dataControl.merge(target,source)
        showinfo("Merge success","The file is merged and will be loaded for viewing")
        window.destroy()