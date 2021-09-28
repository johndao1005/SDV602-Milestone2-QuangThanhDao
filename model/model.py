"""
This is the Model class the super class of all Models
"""
from tkinter.constants import S
from model.data.data_scan import DataManager


class Model():
    def __init__(self, dataSource=None):
        self.dataSource = dataSource
        self.dataManager = DataManager()

        if dataSource != None:
            csvFile = self.dataManager.readFile(dataSource)

    def merge(self, newFile, currentFile):
        self.dataManager.append(newFile, currentFile)

    def genderData(self):
        data = self.dataManager.readFile(self.dataSource)
        male = 0
        female = 0
        for row in data:
            if row['sex'] == "male":
                male += 1
            elif row['sex'] == "female":
                female += 1
        return {"Male": male, "Female": female}

    def locationData(self):
        data = self.dataManager.readFile(self.dataSource)
        yearData = dict()
        for row in data:
            year = row['year']
            if year not in yearData and year != "":
                yearData[year] = [0]*7
            if year != "" and row['occurrenceRemarks'] != "":
                featureData = row['occurrenceRemarks'].split(' ')
                if featureData[0] == "Mature":
                    yearData[year][0] += 1
                elif featureData[0] == "Immature":
                    yearData[year][1] += 1
                if featureData[2] == "300":
                    yearData[year][2] += 1
                elif featureData[2] == "350":
                    yearData[year][3] += 1
                elif featureData[2] == "400":
                    yearData[year][4] += 1
                elif featureData[2] == "420-450":
                    yearData[year][5] += 1
                elif featureData[2] == "440" or featureData[2] == "450":
                    yearData[year][6] += 1
        return yearData

    def featureData(self):
        data = self.dataManager.readFile(self.dataSource)
        latitude = []
        longitude = []
        for row in dataset:
                if row['decimalLatitude'] != "" or row['decimalLongitude'] != "":
                    latitude.append(row["decimalLatitude"])
                    longitude.append(row["decimalLongitude"])
        return {"Latitude": latitude,"Longitude":longitude}
