# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt
# Modul ktory wyswietla nie uporzadkowane listy w sposob uporzadkowany
# from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()
sms = NotificationManager()

sheet_data = data_manager.get_sheet_prices()

if sheet_data[0]["iataCode"] == "":
    for city in sheet_data:
        iata_code = flight_search.iata_code(city["city"])
        data_manager.put_iata(iata_code, city["id"])

today = dt.datetime.now()
tomorrow = today + dt.timedelta(1)
six_months_from_today = today + dt.timedelta(days=(6 * 30))

DEPARTURE_FROM = "LON"

for city in sheet_data:
    flight = flight_search.search_flight(DEPARTURE_FROM, city["iataCode"], tomorrow, six_months_from_today)
    if flight is None:
        continue
    if flight.price < city["lowestPrice"]:
        message = f"""
        Low Price Alert! Only £{flight.price} 
        to fly from {flight.origin_city}-{flight.origin_airport}
        to {flight.destination_city}-{flight.destination_airport}
        from {flight.out_date} to {flight.return_date}
        """

        email_message = f"""
        Low Price Alert! Only £{flight.price} 
        to fly from {flight.origin_city}-{flight.origin_airport}
        to {flight.destination_city}-{flight.destination_airport}
        from {flight.out_date} to {flight.return_date}\n
        https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.
        {flight.destination_airport}.{flight.out_date}*{flight.origin_airport}.
        {flight.destination_airport}.{flight.return_date}
        """

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            email_message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        sms.send_message(message)
        email_message.encode("utf-8")
        sms.send_emails(email_message)

