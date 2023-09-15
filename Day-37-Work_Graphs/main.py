import requests
from datetime import datetime

USERNAME = "ezer"
USERNAME2 = 'ezertobi'
TOKEN = "hdhd333hfbrfuj4hrjjuejwkskk4jfj"
GRAPHE_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME2,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPHE_ID,
    "name": "Coding time",
    "unit": "min",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# TO CREATE GRAPH
graph_endpoint = f"{pixela_endpoint}/{USERNAME2}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# TO POST IN NEW DATA
post_in_graph_endpoint = f"{pixela_endpoint}/{USERNAME2}/graphs/{GRAPHE_ID}"
today = datetime(year=2023, month=7, day=17)
# print(today.strftime("%Y%m%d"))
# today = datetime.now()
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How man minutes did you use for coding today? "),
}
response = requests.post(url=post_in_graph_endpoint, json=post_config, headers=headers)
print(response.text)

# TO UPDATE/EDIT DATA
update_graph_endpoint = f"{pixela_endpoint}/{USERNAME2}/graphs/{GRAPHE_ID}/{today.strftime('%Y%m%d')}"
update_config = {
    "quantity": "100",
}
# response = requests.put(url=update_graph_endpoint, json=update_config, headers=headers)
# print(response.text)

# FOR DELETING PARTICULAR DATA
delete_graph_endpoint = f"{pixela_endpoint}/{USERNAME2}/graphs/{GRAPHE_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=update_graph_endpoint, headers=headers)
# print(response.text)


