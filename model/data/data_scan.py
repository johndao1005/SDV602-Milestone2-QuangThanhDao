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
    
    def readFile(self,filePath):
            with open(filePath,'r',newline="") as data:
                dataset =csv.DictReader(data)
                output = []
                for row in dataset:
                    output.append(row)
                return output
    
    def append(self,newFile,currentFile,):
        header = ["ï»¿X", "Y", "FID", "id", "modified", "language", "rights", "rightsHolder", "bibliographicCitation", "institutionCode", "collectionCode", "basisOfRecord", "catalogNumber", "occurrenceRemarks", "individualID", "individualCount", "sex", "occurrenceStatus", "eventDate", "year", "waterBody", "decimalLatitude", "decimalLongitude", "geodeticDatum", "coordinateUncertaintyInMeters", "footprintWKT", "georeferenceRemarks", "scientificNameID", "scientificName", "kingdom", "phylum", "class", "order_", "family", "genus", "subgenus", "specificEpithet", "infraspecificEpithet", "scientificNameAuthorship"]
        with open(currentFile,'a',newline="") as targetData:
            writer = csv.DictWriter(targetData,header)
            for row in self.readFile(newFile):
                writer.writerow(row)
        
