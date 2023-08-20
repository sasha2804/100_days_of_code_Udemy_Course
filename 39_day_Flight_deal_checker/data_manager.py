import requests
from pprint import pprint

END_POINT_GET = "https://api.sheety.co/cc0695d4776ce3d229e48fdb4c878708/flightDeals/prices"
END_POINT_PUT = "https://api.sheety.co/cc0695d4776ce3d229e48fdb4c878708/flightDeals/prices/"


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheetydata = {}

    # read and preare data structure from google sheet
    def readData(self):
        sheet_endpoint = END_POINT_GET
        response = requests.get(sheet_endpoint)
        self.sheetydata = response.json()      

    def writeData(self):
        pass

    # fill in missing iataCodes      
    def updateIATACodes(self):
        id = 2
        for i in self.sheetydata['prices']:            
            data = {
                "price": {
                   "iataCode": i['iataCode']                    
                }
            }            
            endpoint = f"{END_POINT_PUT}/{id}"
            id += 1
            response = requests.put(url=endpoint, json=data) 
        print("response.status_code =", response.status_code) 
        print("response.text= ", response.text)


    