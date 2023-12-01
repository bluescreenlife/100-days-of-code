'''Amazon price checker: checks item price from a URL, and emails user if price is below their target price.'''
import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime
import time
from dotenv import load_dotenv
import os

URL = "https://www.amazon.com/FROG-Replacement-SmartChlor-Chlorine-Cartridge/dp/B01AASAM7M?pd_rd_w=hSM2s&content-id=amzn1.sym.d7b2d8b5-a4a1-4936-94ee-0a973f84d4dc&pf_rd_p=d7b2d8b5-a4a1-4936-94ee-0a973f84d4dc&pf_rd_r=KM5HEW58BFHMZNK510PJ&pd_rd_wg=6mZ5E&pd_rd_r=6ef9a206-ec80-464a-b83d-637bb9b068b8&pd_rd_i=B01AASAM7M&psc=1&ref_=pd_bap_d_grid_rp_0_1_ec_pd_gwd_bag_pd_gw_rp_2_t"
TARGET_PRICE = 50.00
ITEM_NAME = "Hot Tub Chrlorine Cartridges"

load_dotenv()

SENDER = os.getenv("SENDER")
RECIPIENT = os.getenv("RECIPIENT")
SENDER_PW = os.getenv("SENDER_PW")
SENDER_SERVER = os.getenv("SENDER_SERVER")
SENDER_PORT = os.getenv("SENDER_PORT")

def get_price(URL):
    '''Fetches the current price of the item.'''
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.7"
    }

    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    data = response.text

    soup = BeautifulSoup(data, "lxml")
    price = float(soup.find("span", class_="a-price-whole").get_text() + soup.find("span", class_="a-price-fraction").get_text())
    return price

def is_deal(price, target=TARGET_PRICE):
    '''Returns true if price is under user's target price.'''
    if price <= target:
        return True

def send_email(message, from_addr=SENDER, to_addr=RECIPIENT):
    '''Sends notification email with price alert.'''
    with smtplib.SMTP(SENDER_SERVER, port=SENDER_PORT) as connection:
        connection.starttls()
        connection.login(user=SENDER, password=SENDER_PW)
        connection.sendmail(
            from_addr=SENDER, 
            to_addrs=RECIPIENT, 
            msg=message
        )

if __name__ == "__main__":
    while True:
        hour = datetime.now().hour
        if hour == 7:
            price = get_price(URL)
            print(f"\n{ITEM_NAME} price check: ${price}\nTarget price: {TARGET_PRICE}\n")
            if is_deal(price):
                print("Price below target. Sending email...\n")
                message_string = f"Price Drop: {ITEM_NAME}\n\nPrice is now ${price}, which is below your target price of ${TARGET_PRICE}.\nLink to item: {URL}"
                send_email(message=message_string)
                print("Email sent.\n")
            else:
                print(f"Price check: {ITEM_NAME}: {price}. Above target price - email not sent.")
        else:
            print("Time check: not 7AM, check not run.")
        time.sleep(3600)