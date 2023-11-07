import requests
import smtplib

# weather api
API_KEY = '69f04e4613056b159c2761a9d9e664d2'
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'

# weather location
LOCAL_LAT = 40.712776
LOCAL_LONG = -74.005974

# mail api
SENDER_EMAIL_ADDR ='youremail@gmail.com'
SENDER_PW ='yourkey'
SENDER_SERVER = 'smtp.gmail.com'
SENDER_PORT = 587
SENDER_NAME = "John Doe"

# new york by default, change to any preferred site, to be included in email
LOCAL_WEATHER = 'https://weather.com/weather/today/l/bd5db745591af55a4a30fea48170c2cb8f88b9f253dd3a583cdd862941fd13c2'

will_rain = False

weather_params = {
    'lat': LOCAL_LAT,
    'lon': LOCAL_LONG,
    'exclude': 'current,minutely,daily',
    'appid': API_KEY
}

# get weather forecast
response = requests.get(url=OWM_ENDPOINT, params = weather_params)
response.raise_for_status()
weather_data = response.json()

next_12hr_codes = [hour_dict['weather'][0]['id'] for hour_dict in weather_data['hourly'][:12]]

# set will rain to true if it will rain in next 12 hours
if any(code < 600 for code in next_12hr_codes):
    will_rain = True

def send_email():
    '''Sends an email from user to recipients notifying of weather condition.'''
    with smtplib.SMTP(SENDER_SERVER, port=SENDER_PORT) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL_ADDR, password=SENDER_PW)
        connection.sendmail(
            from_addr=SENDER_EMAIL_ADDR, 
            to_addrs=SENDER_EMAIL_ADDR, 
            msg=f"Subject:Rain Forecasted Today\n\nThere is rain in the forecast today within the next 12 hours. For more
            information, click here: {LOCAL_WEATHER}\n\nThis email was sent automatically using a program written by {SENDER_NAME}.
            \nTo unsubscribe, just reply and let them know!")
    
if will_rain:
    send_email()