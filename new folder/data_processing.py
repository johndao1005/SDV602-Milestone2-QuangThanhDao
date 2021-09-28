import csv
from datetime import datetime
import string
import random
import numpy as np


currentTime = datetime.today().strftime("%d/%m/%Y %H:%M")
currentYear = datetime.today().strftime("%Y")
currentDate = datetime.today().strftime("%d/%m/%Y")


# max -20014910.49 min 20035727.23
x_value = random.randrange(-20014910.49, 20035727.23)
y_value = 0.0  # max -6627823.503 min -1723533.058
longtitude = 0.0  # max -179.797 min 179.984
latitude = 0.0  # max -51.040 min -15.2977

dataList = {
    "year": 19,
    "features": 3,
    "gender": 16,
    "longtitude": 22,
    "latitude": 21
}

id_num = 0


datasource = "./data-sample/test.csv"

def read_data(datatype="longtitude"):
    index = dataList[datatype]
    with open(datasource, "r") as data:
        dataset = data.read().split("\n")
        global id_num
        id_num = len(dataset)
        outputData = []
        for eachLine in dataset[1::]:
            if len(eachLine) > 1:
                dataEntry = eachLine.split(",")
                if dataEntry[index] != "":
                    outputData.append(dataEntry[index])
    return outputData


def append_data(feature=["Immature", "300 cm"], gender="male", newshark=True, orgnisation="NMIT",):
    if newshark == True:
        sharkName = "Shark "+"".join(random.choices(string.ascii_uppercase,
                                                    k=2) + random.choices(string.digits, k=3))
        sharkTag = sharkName + " - " + "".join(random.choices(string.digits,k=2))
    with open(datasource, "a") as data:
        header = ["X", "Y", "FID", "id", "modified", "language", "rights", "rightsHolder", "bibliographicCitation", "institutionCode", "collectionCode", "basisOfRecord", "catalogNumber", "occurrenceRemarks", "individualID", "individualCount", "sex", "occurrenceStatus", "eventDate", "year", "waterBody", "decimalLatitude", "decimalLongitude", "geodeticDatum", "coordinateUncertaintyInMeters", "footprintWKT", "georeferenceRemarks", "scientificNameID", "scientificName", "kingdom", "phylum", "class", "order_", "family", "genus", "subgenus", "specificEpithet", "infraspecificEpithet", "scientificNameAuthorship"]
        writer = csv.DictWriter(data, fieldnames=header)
        item = {"X": -19648669.36,
                "Y": -5483690.139,
                "FID": 3,
                "id": 4,
                "modified": currentTime,
                "language": "en",
                "rights": "Creative Commons Attribution 3.0 New Zealand Licence",
                "rightsHolder": orgnisation,
                "bibliographicCitation": f"Carcharodon carcharias ({sharkTag})",
                "institutionCode": orgnisation,
                "collectionCode": "MBIS White shark tagging",
                "basisOfRecord": "Occurrence",
                "catalogNumber": sharkTag,
                "occurrenceRemarks": f"{feature[0]} {gender} {feature[1]} (TL)",
                "individualID": sharkName,
                "individualCount": 1,
                "sex": gender,
                "occurrenceStatus": "present",
                "eventDate": currentDate,
                "year": currentYear,
                "waterBody": "Pacific Ocean",
                "decimalLatitude": latitude,
                "decimalLongitude": longtitude,
                "geodeticDatum": "WGS84",
                "coordinateUncertaintyInMeters": 10000,
                "footprintWKT": f"POINT ({longtitude} {latitude})",
                "georeferenceRemarks": "Daily positions were estimated from ambient light data stored on WC PAT4 and Mk10 tags using WC-GPE: Global Position Estimator Program Suite software",
                "scientificNameID": "urn:lsid:marinespecies.org:taxname:105838",
                "scientificName": "Carcharodon carcharias",
                "kingdom": "Animalia",
                "phylum": "Chordata",
                "class": "Elasmobranchii",
                "order_": "Lamniformes",
                "family": "Lamnidae",
                "genus": "Carcharodon",
                "specificEpithet": "carcharias",
                "infraspecificEpithet": "",
                "scientificNameAuthorship": "(Linnaeus, 1758)"
                }
        writer.writerow(item)


print(read_data())
print(id_num)
