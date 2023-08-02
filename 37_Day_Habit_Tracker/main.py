
from urllib import response
import requests

USERNAME = "oleksandr1987"
TOKEN = "123456token!oleks"

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# CREATE USER
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)



# CREATE GRAPH
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Reading graph",
#     "unit": "Minutes",
#     "type": "int",
#     "color": "ajisai"
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


