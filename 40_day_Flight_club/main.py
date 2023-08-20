#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch


# google sheet Class manipulations
flight_data = DataManager()
flight_data.readData()
readData = flight_data.sheetydata
pprint(readData)

ORIGIN_CITY_IATA = 'LON'

sheet_data = readData

#flight search Class manipulations
flight_search = FlightSearch()


# check if there are missing iataCodes in the table and intitiate filling 
# missing info to the google sheet
for i in readData['prices']:
    if i['iataCode'] == '':  
        for j in readData['prices']:
            iataCode = flight_search.get_destination_code(j['city'])
            j['iataCode'] = iataCode
        print('sheety data: ',flight_data.sheetydata)
        flight_data.updateIATACodes()
        break

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data['prices']:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )




