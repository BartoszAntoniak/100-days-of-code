import requests
import os
from requests.auth import HTTPBasicAuth
from flight_search import FlightSearch

USERNAME = os.environ.get("USERNAME", "Key does not exist")
PASSWORD = os.environ.get("PASSWORD", "Key does not exist")
TOKEN = os.environ.get("TOKEN", "Key does not exist")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT", "Key does not exist")

fs = FlightSearch()

class DataManager:
    def __init__(self):
        self.data = {}

    def get_docs_data(self):
        auth = HTTPBasicAuth(username=USERNAME, password=PASSWORD)
        get_docs_data_request = requests.get(SHEET_ENDPOINT,auth=auth)
        self.data = get_docs_data_request.json()["prices"]
        return self.data

    def update_data(self):
        for city in self.data:
            new_data = {
                "price":{
                    "iataCode":fs.get_city_code(city["city"])
                }
            }

            update_endpoint = f"{SHEET_ENDPOINT}/{city['id']}"
            json = new_data
            auth = HTTPBasicAuth(username=USERNAME, password=PASSWORD)
            update_request = requests.put(update_endpoint,auth=auth,json=json)

            if update_request.status_code != 200:
                print(f"Failed to update {city['city']}: {update_request.status_code}, {update_request.text}")

        return True

