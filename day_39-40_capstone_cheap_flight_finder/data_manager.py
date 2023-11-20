import os
import requests
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

class DataManager:
    '''Manages data in Google Sheet.'''
    def __init__(self):
        self.SHEETY_FLIGHTS_AUTH = os.environ.get("SHEETY_FLIGHTS_AUTH")

        self.HEADERS = {
            "authorization" : self.SHEETY_FLIGHTS_AUTH
        }
        self.SHEET_DATA = None

    def get_sheet_data(self):
        '''Retrieves data from Google Sheet.'''
        prices_post_endpoint = "https://api.sheety.co/414d405e70de57c54d4c1178cc937f5a/flightDeals/prices"

        response = requests.get(url=prices_post_endpoint, headers=self.HEADERS)
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

    def new_user_signup(self):
        '''Adds a new user (recipient of flight deal alerts) to the Google Sheet.'''
        users_endpoint = "https://api.sheety.co/414d405e70de57c54d4c1178cc937f5a/flightDeals/users"

        first_name = input("Welcome to Flight Club. We find the best flight deals and email you.\nWhat is your first name? ").title()
        last_name = input("What is your last name? ").title()
        email = input("What is your email address? ").lower()
        confirm_email = input("Confirm your email address: ").lower()

        if email == confirm_email:
            print("Congrats, you're in the club!")

        data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }

        response = requests.post(url=users_endpoint, json=data, headers=self.HEADERS)
        response.raise_for_status()

    def get_emails(self):
        '''Retrieves a list of email address from the users tab of the Google Sheet.'''
        users_endpoint = "https://api.sheety.co/414d405e70de57c54d4c1178cc937f5a/flightDeals/users"

        response = requests.get(url=users_endpoint, headers=self.HEADERS)
        response.raise_for_status()
        data = response.json()

        emails = [user["email"] for user in data["users"]]
        return emails