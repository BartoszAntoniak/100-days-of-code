from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
import time

data_manager = DataManager()
sheet_data = data_manager.get_docs_data()
data_manager.update_data()

flight_search = FlightSearch()

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_city_code(row["city"])
        time.sleep(2)

data_manager.data = sheet_data
data_manager.update_data()

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.get_flights(iata_code=destination["iataCode"],max_price=destination["lowestPrice"])

    cheapest_flight = FlightData.find_cheapest_flight(flights.json())
    print(f"{destination['city']}: £{cheapest_flight.price}")
    time.sleep(2)