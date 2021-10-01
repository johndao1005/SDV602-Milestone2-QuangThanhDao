"""
Read csv file in data-sample folder by defaul but also allow reading data from different file source provided with open-csv function or merge function
"""
import csv
from os import path
import pandas as pd
from typing import Dict


class DataManager():
    """Data manager class which handle the raw data at the lowest level which directly interact with csv
    """
    def readFile(self, filePath):
        """Read csv file in dictionary format with dict reader

        Args:
            filePath (string): the path to the file

        Returns:
            array: list of the row data which readed with dictionary reader
        """
        with open(filePath, 'r', newline="") as data:
            dataset = csv.DictReader(data)
            output = []
            for row in dataset:
                output.append(row)
            return output

    def append(self, newFile, currentFile,):
        """added the new File data into the current file at the button with dictionary writer

        Args:
            newFile (string): the directory of the target file
            currentFile (string): the directory of the current file
        """
        header = ["ï»¿X", "Y", "FID", "id", "modified", "language", "rights", "rightsHolder", "bibliographicCitation", "institutionCode", "collectionCode", "basisOfRecord", "catalogNumber", "occurrenceRemarks", "individualID", "individualCount", "sex", "occurrenceStatus", "eventDate", "year", "waterBody",
                "decimalLatitude", "decimalLongitude", "geodeticDatum", "coordinateUncertaintyInMeters", "footprintWKT", "georeferenceRemarks", "scientificNameID", "scientificName", "kingdom", "phylum", "class", "order_", "family", "genus", "subgenus", "specificEpithet", "infraspecificEpithet", "scientificNameAuthorship"]
        with open(currentFile, 'a', newline="") as targetData:
            writer = csv.DictWriter(targetData, header,extrasaction='ignore')
            for row in self.readFile(newFile):
                writer.writerow(row)

    def readLocation(self, filePath):
        """Reading the current csv file in pandas to allow plotting the data with geopandas with the map

        Args:
            filePath (string): the path to the csv file 

        Returns:
            pandas: pandas format longtitude and latitude
        """
        locationData = pd.read_csv(filePath,
                                usecols=["decimalLatitude",
                                            "decimalLongitude"],
                                )
        return locationData
