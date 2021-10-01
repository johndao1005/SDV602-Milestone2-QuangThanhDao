"""
Model class which contain method to get the raw data from csv DataManager, merge files or read the location data with pandas.
After that filter the data in different catogeries with different methods such as featureData, locationData and genderData
"""
from tkinter.constants import S
from model.data.data_scan import DataManager

class Model():
    """Handle the data filter read and merge datasource
    """
    def __init__(self, dataSource=None):
        """Start the model class which take the data source provided as argurement as well as get the DataManager class to use the method attached to the Data

        Args:
            dataSource (string, optional): Get the data source to be analyzed. Defaults to None.
        """
        self.dataSource = dataSource
        self.dataManager = DataManager()

    def merge(self, newFile, currentFile):
        """Excute the append method of data manager class taking the 2 file paths

        Args:
            newFile (string): path to the target file
            currentFile (string): path to the source file
        """
        self.dataManager.append(newFile, currentFile)

    def genderData(self):
        """return the gender data from the data source provided in the model parameter

        Returns:
            dictionary: contain the gender as the key and the corespond integer value
        """
        data = self.dataManager.readFile(self.dataSource)
        male = 0
        female = 0
        for row in data:
            if row['sex'] == "male":
                male += 1
            elif row['sex'] == "female":
                female += 1
        return {"Male": male, "Female": female}

    def featureData(self):
        """return the feature data from the data source provided in the model parameter

        Returns:
            dictionary: contain the year as the key and the value as array for each category belong to their index
        """
        data = self.dataManager.readFile(self.dataSource)
        yearData = dict()
        for row in data:
            year = row['year']
            if year not in yearData and year != "":
                yearData[year] = [0]*7
            if year !="" and row['occurrenceRemarks'] != "":
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
                else:
                    yearData[year][6] += 1
        return yearData

    def locationData(self):
        """read the location data from the data source provided in the model parameter

        Returns:
            pd format data : latitude and longtitude pair value
        """
        locationData = self.dataManager.readLocation(self.dataSource)
        return locationData

