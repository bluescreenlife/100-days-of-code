import os
import requests
from dotenv import load_dotenv
load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/414d405e70de57c54d4c1178cc937f5a/flightDeals/prices"
        self.SHEETY_FLIGHTS_AUTH = os.environ.get("SHEETY_FLIGHTS_AUTH")

        self.headers = {
            "Authorization" : self.SHEETY_FLIGHTS_AUTH
        }

        