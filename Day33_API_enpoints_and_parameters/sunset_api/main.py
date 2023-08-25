import requests
import datetime


parameters = {
    "lat": 52.229675,
    "lng": 21.012230,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data= response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunset = sunset.split("T")[1].split("+")[0]

print(sunset)

time_now = datetime.datetime.now()
time_now = time_now.time()
print(time_now)