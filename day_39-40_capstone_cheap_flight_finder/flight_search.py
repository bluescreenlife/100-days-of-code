import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta
import json

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, home_city: str):
        load_dotenv()
        self.TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
        self.TEQUILA_KEY = os.environ.get("TEQUILA_KEY")
        self.headers = {
            "Content-Type" : "application/json",
            "apikey" : self.TEQUILA_KEY
        }
        self.HOME_CITY = home_city
        self.CURRENCY = "USD"

        today_date = datetime.now()
        one_year_date = today_date + timedelta(days=183)
        one_month_date = today_date + timedelta(days=30)

        self.FROM_DATE = datetime.now().strftime("%d/%m/%Y")
        self.TO_DATE = one_year_date.strftime("%d/%m/%Y")
        self.RETURN_TO_DATE = one_month_date.strftime("%d/%m/%Y")

    def search_flights(self, to_city: str, max_price: int):
        '''Searches for flight criteria, returns matching flights'''
        # NOTE: date must be in dd/mm/yyyy format
        flight_criteria = {
            "fly_from" : self.HOME_CITY,
            "fly_to" : to_city,
            "date_from" : self.FROM_DATE,
            "date_to" : self.TO_DATE,
            "return_to": self.RETURN_TO_DATE,
            "price_to" : max_price,
            "curr" : self.CURRENCY,
            "max_stopovers" : 0,
            "ret_from_diff_city" : False
        }

        response = requests.get(url=self.TEQUILA_ENDPOINT, params=flight_criteria, headers=self.headers)
        response.raise_for_status()
        result = response.json()

        airlines_dict = {
            'AA': 'American Airlines',
            'DL': 'Delta Air Lines',
            'UA': 'United Airlines',
            'LH': 'Lufthansa',
            'EK': 'Emirates',
            'BA': 'British Airways',
            'AF': 'Air France',
            'QR': 'Qatar Airways',
            'SQ': 'Singapore Airlines',
            'CX': 'Cathay Pacific',
            'KL': 'KLM Royal Dutch Airlines',
            'WN': 'Southwest Airlines',
            'NH': 'ANA All Nippon Airways',
            'TK': 'Turkish Airlines',
            'QF': 'Qantas',
            'EY': 'Etihad Airways',
            'AC': 'Air Canada',
            'LA': 'LATAM Airlines',
            'AS': 'Alaska Airlines',
            'VS': 'Virgin Atlantic',
            'JL': 'Japan Airlines',
            'LX': 'Swiss International Air Lines',
            'AY': 'Finnair',
            'SU': 'Aeroflot',
            'CZ': 'China Southern Airlines',
            'AI': 'Air India',
            'KE': 'Korean Air',
            'SK': 'SAS Scandinavian Airlines',
            'TG': 'Thai Airways',
            'NZ': 'Air New Zealand',
            'BR': 'EVA Air',
            'GA': 'Garuda Indonesia',
            'MS': 'EgyptAir',
            'IB': 'Iberia',
            'SV': 'Saudia',
            'AM': 'Aeromexico',
            'KA': 'Cathay Dragon',
            'HU': 'Hainan Airlines',
            'OS': 'Austrian Airlines',
            'DY': 'Norwegian Air Shuttle',
            'AK': 'AirAsia',
            'B6': 'JetBlue Airways',
            'NK': 'Spirit Airlines',
            'F9': 'Frontier Airlines',
            'VY': 'Vueling Airlines',
            'W6': 'Wizz Air',
            'FR': 'Ryanair',
            'U2': 'EasyJet',
            'AZ': 'Alitalia',
            'AV': 'Avianca',
            'TP': 'TAP Air Portugal',
            'CM': 'Copa Airlines',
            'WS': 'WestJet',
            'HA': 'Hawaiian Airlines',
            'D7': 'AirAsia X',
            'TR': 'Scoot',
            'G9': 'Air Arabia',
            'AD': 'Azul Brazilian Airlines',
            'D8': 'Norwegian Air International',
            'HO': 'Juneyao Airlines',
            '6E': 'IndiGo',
            'UK': 'Vistara',
            'HM': 'Air Seychelles',
            'BI': 'Royal Brunei Airlines',
            'RJ': 'Royal Jordanian',
            'KQ': 'Kenya Airways',
            'ET': 'Ethiopian Airlines',
            'SA': 'South African Airways',
            'PR': 'Philippine Airlines',
            'PK': 'Pakistan International Airlines',
            'PG': 'Bangkok Airways',
            'VN': 'Vietnam Airlines',
            'OZ': 'Asiana Airlines',
            'KC': 'Air Astana',
            'SY': 'Sun Country',
            'N0': 'Norwegian Airlines',
            'Z0': 'Zoom Air',
            'W4': 'Wizz Air Malta',
            'FI': 'Icelandair',
            'OG': 'PLAY Airlines',
            'TO': 'Transavia France',
            'RK': 'Ryanair UK'
        }

        matching_flights = []

        for flight in result["data"]:
            if flight["availability"]["seats"] != "null" and flight["availability"]["seats"] != None:
                departure = flight["local_departure"].split("T")
                departure_date = departure[0]
                departure_time = departure[1][:5]
                arrival = flight["local_arrival"].split("T")
                arrival_date = arrival[0]
                arrival_time = arrival[1][:5]
                price = flight["fare"]["adults"]
                seats_available = flight["availability"]["seats"]
                airline = airlines_dict[flight["airlines"][0]]
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
        
        def custom_key(flight):
            departure_date_string = flight['departure'].split(' @ ')[0]  # Extracting the date part
            departure_date = datetime.strptime(departure_date_string, '%Y-%m-%d')
            price = int(flight['price'].replace('$', ''))  # Extracting the price as an integer
            return (price, departure_date)

        # Sort the list of flights using the custom key function
        matching_flights = sorted(matching_flights, key=custom_key)

        # Print the sorted list of flights
        for flight in matching_flights:
            print(flight)

        return matching_flights

flight_finder = FlightSearch("MSP")
flight_finder.search_flights("LAS", 400)