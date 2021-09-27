"""
This is the Model class the super class of all Models 
"""
from tkinter.constants import S
from model.data.data_processing import *
from model.data.data_scan import DataManager
class Model():
    def __init__(self,dataSource=None):
        self.dataSource =dataSource | "../"
        self.dataManager = DataManager()
        
        if dataSource != None:
            csvFile = self.dataManager.readFile(dataSource)
            
    def merge(self,newFile,currentFile):
        self.dataManager.append(newFile,currentFile)
        
    def getData(self,datatype):
        self.dataManager.readFile(self.dataSource,datatype)
