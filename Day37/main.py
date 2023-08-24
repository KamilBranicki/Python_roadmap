import requests

USERNAME = "branicki"
TOKEN = "effgas43t43452sdf423t"

pixela_endpoit_user = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoit_user, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoit_user}/{USERNAME}/graphs'

graph_params = {
    "id": "graph1",
    "name": "Programing Graph",
    "unit": "h",
    "type": "float",
    "color": "shibafu"

}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)