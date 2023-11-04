import requests
from datetime import datetime
import smtplib
import time

# coordinates for sunrise/sunset data and ISS location comparison
MY_LAT = 40.7128
MY_LONG = -74.006

# SMTP data
SENDER_EMAIL_ADDR ='youremail@gmail.com'
SENDER_PW ='yourkey'
SENDER_SERVER = 'smtp.gmail.com'
SENDER_PORT = 587

def is_dark():
    '''Determines whether it is after sunset and before sunrise at user coordinates, returns boolean'''
    time_now = datetime.now()
    response = requests.get(f"https://api.sunrisesunset.io/json?lat={MY_LAT}&lng={MY_LONG}")
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split(":")[0])
    sunset = int(data["results"]["sunset"].split(":")[0])

    print(f"Current hour: {time_now.hour}\nSunrise: {sunrise}\nSunset: {sunset}")
    if sunset < time_now.hour < sunrise:
        print("It is dark.\n")
        return True
    else:
        print("It is not dark.\n")
        return False

def iss_overhead():
    '''Determines whether the ISS is within 5 degress of user coordinates, returns boolean.'''
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"ISS coordinates: {iss_latitude}, {iss_longitude}")
    print(f"My coordinates: {MY_LAT}, {MY_LONG}")
    
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        print("The ISS is overhead.\n")
        return True
    else:
        print("The ISS is not overhead.\n")
        return False

def send_email():
    '''Sends an email from user to self notifying to look up.'''
    with smtplib.SMTP(SENDER_SERVER, port=SENDER_PORT) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL_ADDR, password=SENDER_PW)
        connection.sendmail(
            from_addr=SENDER_EMAIL_ADDR, 
            to_addrs=SENDER_EMAIL_ADDR, 
            msg=f"Subject:ISS Overhead!\n\nLook up!")
    
    print("Email to self successfully sent.\n")

if __name__ == "__main__":
    while True:
        if is_dark() and iss_overhead():
            send_email()
        time.sleep(60)