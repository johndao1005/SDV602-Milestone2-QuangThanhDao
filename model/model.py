"""
This is the Model class the super class of all Models 
"""
from tkinter.constants import S
from model.data.data_processing import *

class Model():
    def __init__(self,data_source=None):
        self.record_set = None

