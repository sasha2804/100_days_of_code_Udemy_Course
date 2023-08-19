#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch


# google sheet Class manupulations
flight_data = DataManager()
flight_data.readData()
readData = flight_data.sheetydata

pprint(readData)
# print(readData['prices'][0]['iataCode'])




# check if there are missing iataCodes in the table and intitiate filling 
# missing info to the google sheet
for i in readData['prices']:
    if i['iataCode'] == '':  
        flight_search = FlightSearch()
        get_destination = flight_search.get_destination_code('New York')
        print(get_destination)
        updateData = flight_data.updateIATACodes()
        break




