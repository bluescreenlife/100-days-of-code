import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta

class FlightSearch:
    '''Interacts with Kiwi Tequila flight search API to retrieve flight information.'''
    def __init__(self, home_city: str):
        load_dotenv()
        self.TEQUILA_KEY = os.environ.get("TEQUILA_KEY")

        self.headers = {
            "Content-Type": "application/json",
            "apikey": self.TEQUILA_KEY
        }

        self.home_city = home_city
        today_date = datetime.now()
        six_month_date = today_date + timedelta(days=183)
        self.from_date = datetime.now().strftime("%d/%m/%Y")
        self.to_date = six_month_date.strftime("%d/%m/%Y")

    def search_flights(self, to_city: str, max_price: int):
        '''Searches for flights to a city below a certian price, returns matching flight information.'''
        endpoint =  "https://api.tequila.kiwi.com/v2/search"
        
        flight_criteria = {
            "fly_from" : self.home_city,
            "fly_to" : to_city,
            "date_from" : self.from_date,
            "date_to" : self.to_date,
            "price_to" : max_price,
            "curr" : "USD",
            "max_stopovers" : 0,
            "one_for_city": 1,
            "ret_from_diff_city" : False,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round"
        }

        response = requests.get(url=endpoint, params=flight_criteria, headers=self.headers)
        response.raise_for_status()
        result = response.json()

        matching_flights = []

        for flight in result["data"]:
            # if seats are available, create dict of flight information
            if flight["availability"]["seats"] != "null" and flight["availability"]["seats"] != None:
                departure = flight["local_departure"].split("T")
                departure_date = departure[0]
                departure_time = departure[1][:5]
                arrival = flight["local_arrival"].split("T")
                arrival_date = arrival[0]
                arrival_time = arrival[1][:5]
                price = flight["fare"]["adults"]
                seats_available = flight["availability"]["seats"]
                airline = flight["airlines"][0]
                flight_no = flight["route"][0]["flight_no"]
            
                matching_flights.append(
                    {
                    "price": f"${price}",
                    "departure": f"{departure_date} @ {departure_time}",
                    "arrival": f"{arrival_date} @ {arrival_time}",
                    "seats available": seats_available,
                    "airline": airline,
                    "flight number": flight_no
                    }
                )
        
        # sort list of flights by price, cheapest first
        def custom_key(flight):
            departure_date_string = flight['departure'].split(' @ ')[0]
            departure_date = datetime.strptime(departure_date_string, '%Y-%m-%d')
            price = int(flight['price'].replace('$', ''))
            return (price, departure_date)

        matching_flights = sorted(matching_flights, key=custom_key)

        return matching_flights

    def get_city_code(self, city_name = str):
        '''Retrieves IATA city code given a city name.'''
        endpoint = "https://api.tequila.kiwi.com/locations/query"
        search_criteria = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=endpoint, params=search_criteria, headers=self.headers)
        response.raise_for_status()
        result = response.json()["locations"][0]["code"]
        return result