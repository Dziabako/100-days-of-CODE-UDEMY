import requests
# Specjalny modul do twilio
from twilio.rest import Client
# Przy uruchamianiu twilio przez serwer zewnetrzny moze pojawic sie blad
# Wtedy nalezy zrobic nastepujace kroki
# from twilio.http.http_client import TwilioHttpClient

# To jest do twilio
account_sid = "twilio account sid"
auth_token = "twilio account token"

parameters = {
    "lat": lat,
    "lon": long,
    "appid": "appid",
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

# Wycinanie 12 pierwszych elementow z listy (z krotki tez moze byc)
twelve_hour_forecast = weather_data["hourly"][:12]

will_rain = False

# Uzyskanie kodow pogody z listy
for hour_data in twelve_hour_forecast:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# W ten sposob komunikat pojawi sie tylko raz jesli w ciagu 12 godzin bedzie padac
if will_rain:
    # Ciag dalszy naprawy bledu polaczenia z powodu darmowego konta
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    # client = Client(account_sid, auth_token, http_client=proxy_client)

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Take an umbrella. It's going to rain",
            from_='number',
            to='number'
        )
