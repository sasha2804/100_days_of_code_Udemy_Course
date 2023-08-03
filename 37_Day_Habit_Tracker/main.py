
from turtle import st
from urllib import response
from urllib.request import URLopener
import requests
import datetime as dt

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





# today = dt.date.today()
# date_str = today.strftime("%Y%m%d")



# write_params = {
#     "date": date_str,
#     "quantity":"2"     
# }

write_point =  f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

# write_resp = requests.post(url=write_point,json=write_params, headers=headers)
# print(write_resp.text)





# $ curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes", "thanksCode":"ThisIsThanksCode"}'
# {"message":"Success. Let's visit https://pixe.la/@a-know , it is your profile page!","isSuccess":true}

# date = "20230803"

# update_params = {    
#     "quantity":"25"  
#     }


# update_point =  f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

# update_resp = requests.put(url=update_point,json=update_params, headers=headers)
# print(update_resp.text)

date = "20230803"

del_point =  f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

del_resp = requests.delete(url=del_point, headers=headers)
print(del_resp.text)






'''
https://pixe.la/v1/users/oleksandr1987/graphs/graph1
'''


