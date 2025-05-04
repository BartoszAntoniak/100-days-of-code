import os, requests, pprint
import datetime

class FlightSearch:
    def get_city_code(self,city):
        API_KEY = os.environ.get("AMADEUS_API_KEY", "Key does not exist")
        API_KEY_SECRET = os.environ.get("AMADEUS_API_KEY_SECRET", "Key does not exist")
        AUTH_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

        data = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_KEY_SECRET
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(url=AUTH_ENDPOINT, data=data, headers=headers)

        AMADEUS_TOKEN = response.json()["access_token"]

        headers = {
            "authorization": f"Bearer {AMADEUS_TOKEN}"
        }
        params = {
            "keyword": city,
            "max": "1",
        }

        ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        result = requests.get(url=ENDPOINT, headers=headers,params=params).json()
        return result["data"][0]["iataCode"]

    def get_flights(self, iata_code, max_price):
        API_KEY = os.environ.get("AMADEUS_API_KEY")
        API_KEY_SECRET = os.environ.get("AMADEUS_API_KEY_SECRET")
        AUTH_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

        data = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_KEY_SECRET
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        auth_response = requests.post(url=AUTH_ENDPOINT, data=data, headers=headers)

        if auth_response.status_code != 200:
            print("Failed to retrieve token:")
            pprint.pprint(auth_response.json())
            return

        AMADEUS_TOKEN = auth_response.json().get("access_token")
        if not AMADEUS_TOKEN:
            print("No access token in response:")
            pprint.pprint(auth_response.json())
            return

        headers = {
            "Authorization": f"Bearer {AMADEUS_TOKEN}"
        }

        query = {
            "originLocationCode": "LON",
            "destinationLocationCode": iata_code,
            "departureDate": (datetime.date.today() + datetime.timedelta(days=1)).isoformat(),
            "returnDate": (datetime.date.today() + datetime.timedelta(days=8)).isoformat(),
            "adults": 1,
            "nonStop": "true",
            "maxPrice": max_price,
            "currencyCode": "GBP",
            "max":5
        }

        ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        flight_search_results = requests.get(url=ENDPOINT, headers=headers, params=query)
        return flight_search_results

