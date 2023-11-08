import requests
import smtplib
from datetime import datetime
import time

### ADJUST THE FOLLOWING VARIABLES ACCORDINGLY ###

# weather api - retrieved from https://openweathermap.org/api
API_KEY = 'yourkey'
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'

# weather location - retrieved from https://www.latlong.net/ - set to New York by default
LOCAL_LAT = 40.712776
LOCAL_LONG = -74.005974

# mail api
SENDER_EMAIL_ADDR ='youremail@gmail.com'
SENDER_PW ='yourkey'
SENDER_SERVER = 'smtp.gmail.com'
SENDER_PORT = 587
SENDER_NAME = "yourname"

# change to any preferred site, to be included in email - set to new york by default
LOCAL_WEATHER_URL = 'https://weather.com/weather/today/l/bd5db745591af55a4a30fea48170c2cb8f88b9f253dd3a583cdd862941fd13c2'

def get_weather():
    '''Checks local weather conditions for next 24hr, returns a list of any inclement weather that is forecasted.'''
    inclement_weather = []

    weather_params = {
        'lat': LOCAL_LAT,
        'lon': LOCAL_LONG,
        'exclude': 'current,minutely,daily',
        'appid': API_KEY
    }

    response = requests.get(url=OWM_ENDPOINT, params = weather_params)
    weather_data = response.json()
    next_24hr_codes = [hour_dict['weather'][0]['id'] for hour_dict in weather_data['hourly'][:24]]

    # add any inclement weather to list
    if any(200 <= code < 300 for code in next_24hr_codes):
        inclement_weather.append("thunderstorm")

    if any(300 <= code < 400 for code in next_24hr_codes):
        inclement_weather.append("drizzle")

    if any(500 <= code < 600 for code in next_24hr_codes):
        inclement_weather.append("rain")

    if any(600 <= code < 700 for code in next_24hr_codes):
        inclement_weather.append("snow")

    print(f"24hr weather codes: {next_24hr_codes}")
    print(f"Inclement weather to occur today:")
    for condition in inclement_weather:
        print(condition)

    return inclement_weather


def send_email(weather_list):
    '''Sends an email reporting the given weather conditions.'''
    message = "The following weather conditions are to occur within the next 24 hours:"
    for condition in weather_list:
        message = f"{message}\n{condition}"
    message = message + f"\n\nFor more details, here is a link to your local weather report:\n{LOCAL_WEATHER_URL}"
    
    '''Sends an email from user to recipients notifying of weather condition.'''
    with smtplib.SMTP(SENDER_SERVER, port=SENDER_PORT) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL_ADDR, password=SENDER_PW)
        connection.sendmail(
            from_addr=SENDER_EMAIL_ADDR, 
            to_addrs=SENDER_EMAIL_ADDR, 
            msg=f"Subject:Inclement Weather Alert\n\n{message}\n\nThis email was sent automatically using a program written by {SENDER_NAME}."
        )
    
    print("\nEmail(s) successfully sent.")

# check each hour if it's 7am - if true, check weather and send any inclement conditions via email
if __name__ == "__main__":
    while True:
        if datetime.now().hour == 7:
            print("Running 7AM check.")
            if get_weather():
                send_email(get_weather())
        else:
            print(f"Current hour: {datetime.now().hour}\nWeather check not run.\n")
        time.sleep(3600)
