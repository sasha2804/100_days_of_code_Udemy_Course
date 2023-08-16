#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch


flight_data = DataManager()
readData = flight_data.readData()
print(readData)

flight_search = FlightSearch()
get_destination = flight_search.get_destination_code('New York')
print(get_destination)






# print(flight_data.result['prices'][0]['iataCode'])



# for i in flight_data.result['prices']:
#     if flight_data.result['prices'][0]['iataCode'] == "":
#         print('!!!None break check fill!!!')
#         break

