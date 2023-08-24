import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 52.229675 # Your latitude
MY_LONG = 21.012230 # Your longitude

time_now = datetime.now().__str__().split(" ")[1].split(".")[0].split(":")[0]
time_now = int(time_now)

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)
    if iss_latitude in (MY_LAT - 5, MY_LAT + 5) and iss_longitude in (MY_LONG - 5, MY_LONG + 5):
        return True

def is_night():
    time.sleep(60)
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if time_now > sunset or time_now < sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark

while True:
    if is_iss_overhead() and is_night():
        my_email = "testkamil16@gmail.com"
        password = "bihyhtsbzqosjhfr"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="madafakaa115@gmail.com", msg="Subject:Satellite\n\nLook up")


# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



