"""
Read csv file in data folder by defaul but also allow reading data from different file source 
"""
import csv
from datetime import datetime
import string
import random
import sys as sys
from os import path
import argparse
from typing import Dict

class DataManager():
    def __init__(self):
        self.status:Dict = {}
        self.file:Dict = {}
        self.file = None
    
    def readFile(self,filePath,datatype="all"):
            with open(filePath,'r',newline="") as data:
                dataset =csv.DictReader(data)
                output = []
                for row in dataset:
                    featureData = row['occurrenceRemarks'].split(' ')
                    sex = featureData[0]
                    #gender = featureData[1]
                    #size = featureData[2]
                    output.append(row)
                    #print(sex,gender,size,row["decimalLatitude"],row["decimalLongitude"])#decimalLongitude,decimalLatitude)
                return output
    
    def append(self,newFile,currentFile,):
        header = ["ï»¿X", "Y", "FID", "id", "modified", "language", "rights", "rightsHolder", "bibliographicCitation", "institutionCode", "collectionCode", "basisOfRecord", "catalogNumber", "occurrenceRemarks", "individualID", "individualCount", "sex", "occurrenceStatus", "eventDate", "year", "waterBody", "decimalLatitude", "decimalLongitude", "geodeticDatum", "coordinateUncertaintyInMeters", "footprintWKT", "georeferenceRemarks", "scientificNameID", "scientificName", "kingdom", "phylum", "class", "order_", "family", "genus", "subgenus", "specificEpithet", "infraspecificEpithet", "scientificNameAuthorship"]
        with open(currentFile,'a',newline="") as targetData:
            writer = csv.DictWriter(targetData,header)
            for row in self.readFile(newFile):
                writer.writerow(row)
        
if __name__ == "__main__":
    data = DataManager()
    print("start reading")
    data.readFile("./test2.csv")
    data.append('./test.csv','./test2.csv')