import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 52.313881
MY_LONG = 15.082800

my_email = "dawidtest315@gmail.com"
password = "ahbzwewvvugqmmig"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

lat_margin = range(42, 63)
long_margin = range(10, 26)

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

time_now = datetime.now().hour

while True:
    time.sleep(60)
    if iss_latitude in lat_margin and iss_longitude in long_margin:
        if time_now >= sunset or time_now <= sunrise:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="dawidtest@yahoo.com",
                    msg="Subject:ISS IS CLOSE\nLOOK UP"
                )
