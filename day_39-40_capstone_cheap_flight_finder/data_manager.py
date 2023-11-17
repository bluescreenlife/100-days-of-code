import os
import requests
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

class DataManager:
    '''Manages data in Google Sheet.'''
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/414d405e70de57c54d4c1178cc937f5a/flightDeals/prices"
        self.SHEETY_FLIGHTS_AUTH = os.environ.get("SHEETY_FLIGHTS_AUTH")

        self.HEADERS = {
            "authorization" : self.SHEETY_FLIGHTS_AUTH
        }
        self.SHEET_DATA = self.get_sheet_data()

    def get_sheet_data(self):
        '''Retrieves data from Google Sheet.'''
        response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.HEADERS)
        response.raise_for_status()
        self.SHEET_DATA = response.json()
        return self.SHEET_DATA
    
    def has_city_codes(self):
        '''Checks if the Google Sheet has all IATA city codes.'''
        num_city_codes = 0

        for city in self.SHEET_DATA["prices"]:
            if city["iataCode"]:
                num_city_codes += 1

        if num_city_codes == len(self.SHEET_DATA["prices"]):
            return True
        else:
            return False
        
    def write_city_code(self, index: int, city_code: str):
        '''Writes IATA city code to Google Sheet.'''
        endpoint = f"https://api.sheety.co/414d405e70de57c54d4c1178cc937f5a/flightDeals/prices/{index}"

        data = {
            "price": {
                "iataCode": city_code
            }
        }

        response = requests.put(url=endpoint, json=data, headers=self.HEADERS)
        response.raise_for_status()