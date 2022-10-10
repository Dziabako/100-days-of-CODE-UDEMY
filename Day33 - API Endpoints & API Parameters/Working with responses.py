# modul do uzyskiwania danych z API Endpoint
import requests
import datetime as dt

# # Tworzenie zmiennej, która przechowuje dane z API Endpoint / W ten sposob otrzymamy tylko response code
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# # Zwracanie response
# print(response)
#
# # Status code
# print(response.status_code)
#
# # Raise exceptions from response error / unikamy wtedy bledu / Ten sposob nie jest zbyt uniwersalny
# if response.status_code == 404:
#     raise Exception("This page does not exist")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to enter this page")
#
# # Raise exceptions from built in module
# response.raise_for_status()
#
# # Uzyskiwanie danym z API / uzyskujemy slownik z ktorego mozemy normalnie korzystac
# data = response.json()
# print(data)

# API Parameters / parametry mozna stworzym w formie slownika
# Mozemy parametry podac w linku do API --> https://api.sunrise-sunset.org/json?lat=52.313881&lng=15.082800
parameters = {
    "lat": 52.313881,
    "lng": 15.082800,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# Uzyskanie godziny z nieformatowanego czasu
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)

time_now = dt.datetime.now()

print(time_now.hour)
