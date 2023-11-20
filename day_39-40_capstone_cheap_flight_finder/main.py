'''Program that uses Kiwi Tequila flight search API and Sheety API for Google Sheets, to search for flight
deals given cities and prices in the sheet, and notify users listed in the user tab when a cheap flight is found.'''
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from dotenv import load_dotenv
import os

load_dotenv()

data_manager = DataManager()
flight_finder = FlightSearch("MSP") # pass in home city as parameter
notifier = NotificationManager()
sheet_data = data_manager.get_sheet_data()

flights_to_notify = []
message = "Good news! Some cheap flights were found for your destination(s) today:\n\n"

# check for any missing IATA codes, retrieve if necessary
if data_manager.has_city_codes():
    print("All IATA codes exist.\n")
else:
    print("Fetching missing city codes...\n")
    for index, row in enumerate(sheet_data["prices"]):
        if not row["iataCode"]:
            city_code = flight_finder.get_city_code(row["city"])
            city_index = index + 2
            data_manager.write_city_code(city_index, city_code)

# search for flights by city code, with criteria in flight_search.py
print("Searching for cheap flights...\n")
for row in sheet_data["prices"]:
    cheap_flights = flight_finder.search_flights(row["iataCode"], row["lowestPrice"])
    if cheap_flights:
        print(f"Cheap flights to {row['city']}:")
        for flight in cheap_flights:
            print(flight)
        flight_dict = {"city": row["city"], "flights": cheap_flights}
        flights_to_notify.append(flight_dict)
    else:
        cheap_flights_stopovers = flight_finder.search_flights(row["iataCode"], row["lowestPrice"], stop_overs=2)
        if cheap_flights_stopovers:
            print(f"Cheap flights to {row['city']} with 1 stopover:")
            for flight in cheap_flights_stopovers:
                print(flight)
            flight_dict = {"city": row["city"], "flights": cheap_flights_stopovers}
            flights_to_notify.append(flight_dict)

# if cheap flights found, send notification email to recipient(s) with flight info
if flights_to_notify:
    recipients = data_manager.get_emails()
    print("Sending notification email...")
    for dict in flights_to_notify:
        message += f"{dict['city']}:\n"
        for flight in dict["flights"]:
            for key, value in flight.items():
                message += f"{key}: {value}\n"
        message += "-----------------------------\n"
    notifier.send_message(recipients, message)
    print("Email(s) successfully sent.")
    print(f"Message:\n{message}")
else:
    print("No cheap flights found. No notification sent.")