"""
Read csv file in data folder by defaul but also allow reading data from different file source 
"""
import csv
from datetime import datetime
import string
import random
import numpy as np
import sys as sys
from os import path
import argparse
from typing import Dict

class DataManager():
    def __init__(self):
        self.status:Dict = {}
        self.current_files:Dict = {}
        self.current_file = None
    pass

    def openFile(self,filePath):
        try:
            self.current_file = open(filePath)
            return self.current_file
        except FileNotFoundError:
            file_not_found = ("File not found error", filePath)
            self.status['File Error'] = [file_not_found] if not ('File Error' in self.status) else self.status['File Error'] + [file_not_found]
            return None
        except FileExistsError   :
            file_exists_error = ("File exists error", filePath)
            self.status['File Error'] =  [file_exists_error] if not ('File Error' in self.status) else self.status['File Error'] + [file_exists_error]
            return None 
        except:
            print("Unexpected error:", sys.exc_info()[0]) 
            return None
        
    def readFile(self,filePath):
        try:
            with open(filePath,'r') as data:
                dataset =csv.DictReader(data)
                
        except FileNotFoundError:
            error = ("File not found error", filePath)
            self.status['File Error'] = [error] if not ('File Error' in self.status) else self.status['File Error'] + [error]
            return None
        except FileExistsError :
            error = ("File exists error", filePath)
            self.status['File Error'] =  [error] if not ('File Error' in self.status) else self.status['File Error'] + [error]
            return None 
        except:
            print("Unexpected error:", sys.exc_info()[0]) 
            return None
        
        
# def read_data(datatype="longtitude"):
#     index = dataList[datatype]
#     with open(datasource, "r") as data:
#         dataset = data.read().split("\n")
#         global id_num
#         id_num = len(dataset)
#         outputData = []
#         for eachLine in dataset[1::]:
#             if len(eachLine) > 1:
#                 dataEntry = eachLine.split(",")
#                 if dataEntry[index] != "":
#                     outputData.append(dataEntry[index])
#     return outputData
if __name__ == "__main__":
    