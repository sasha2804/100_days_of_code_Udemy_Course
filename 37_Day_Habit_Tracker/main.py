
from urllib import response
from urllib.request import URLopener
import requests

USERNAME = "oleksandr1987"
TOKEN = "123456token!oleks"
GRAPH_ID = "graph1"

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
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)








write_params = {
    "date":"20230725",
    "quantity":"2"     
}

write_point =  f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

write_resp = requests.post(url=write_point,json=write_params, headers=headers)
print(write_resp.text)





# $ curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes", "thanksCode":"ThisIsThanksCode"}'
# {"message":"Success. Let's visit https://pixe.la/@a-know , it is your profile page!","isSuccess":true}



'''
https://pixe.la/v1/users/oleksandr1987/graphs/graph1
'''