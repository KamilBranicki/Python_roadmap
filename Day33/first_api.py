import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response) # code = 200 - success
# if response.status_code == 404:
#     raise Exception("That resource does not exits")
# elif response.status_code == 401:
#     raise Exception("Your are not authorised to access")
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)