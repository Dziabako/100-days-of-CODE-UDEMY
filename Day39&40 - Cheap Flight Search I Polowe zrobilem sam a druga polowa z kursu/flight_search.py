# This class is responsible for talking to the Flight Search API.
# search_flight jest z rozwiazania z kursu
import requests
from flight_data import FlightData

API_ENDPOINT = "https://api.tequila.kiwi.com"
HEADERS = {
    "apikey": "qKZBSZi2U0ko5lJj-YYdmkrPxQo0FU-W"
}


class FlightSearch:
    def __init__(self):
        self.code = ""

    def iata_code(self, city_name):
        location_endpoint = f"{API_ENDPOINT}/locations/query"
        city = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint, headers=HEADERS, params=city)
        data = response.json()
        self.code = data["locations"][0]["code"]
        return self.code

    @staticmethod
    def search_flight(from_city_code, to_city_code, time_from, time_to):
        query = {
            "fly_from": from_city_code,
            "fly_to": to_city_code,
            "date_from": time_from.strftime("%d/%m/%Y"),
            "date_to": time_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
            "max_stopovers": 0,
        }

        search_endpoint = f"{API_ENDPOINT}/v2/search"
        response = requests.get(url=search_endpoint, params=query, headers=HEADERS)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {to_city_code}.")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
