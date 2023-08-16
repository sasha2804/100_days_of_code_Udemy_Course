import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.result = 0

    
    def readData(self):
        sheet_endpoint = "https://api.sheety.co/cc0695d4776ce3d229e48fdb4c878708/flightDeals/prices"
        response = requests.get(sheet_endpoint)
        self.result = response.json()

    def writeData(self):
        pass
 



# test = DataManager()

    