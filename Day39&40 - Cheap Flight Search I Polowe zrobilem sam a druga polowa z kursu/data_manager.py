import requests


class DataManager:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/[TOKEN]/flightDeals/prices"
        self.destination_data = {}

    def get_sheet_prices(self):
        response = requests.get(self.endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def put_iata(self, iata_code, row_id):
        sheet_data = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{self.endpoint}/{row_id}", json=sheet_data)
        return response
