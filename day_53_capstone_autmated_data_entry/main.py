'''Automated data entry project: Scrapes apartment listings from Zillow
and fills out a Google Sheet with addresses, rent prices, and links.

Undiagnosed issue with webdriver, runs fine in headless mode, but
quits after 10-15 sheet entries in normal mode, disconnects from devtools.'''

from cgitb import text
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

# beautiful soup setup for scraping property listings
zillow_url = "https://appbrewery.github.io/Zillow-Clone/"

addresses = []
prices = []
links = []

response = requests.get(zillow_url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

# get list of all properties at zillow url
properties = soup.find_all("li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

# get address, rent price, and link for each property, append to lists above
for property in properties:
    address = property.find("address", {'data-test':'property-card-addr'}).text.strip()

    if "|" in address:
        address = address.split("|")[1].strip()
    else:
        address = address.split(",")
        address = (address[1] + address[2]).strip()
    addresses.append(address)

    price = property.find("span", {'data-test':'property-card-price'}).text.split("+")[0]
    price = price.split("/")[0]
    prices.append(price)

    link = property.find("a", {'data-test':'property-card-link'}).get("href")
    links.append(link)

# webdriver setup for input to Google Sheet
google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeep00r5NguE17zhAvKleAcY0teBUuAszFWghMly216GMeiwQ/viewform?usp=sf_link"

chromedriver_path = "/Users/andrew/Developer/chromedriver"

service = Service(executable_path=chromedriver_path)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options, service=service)

# input each property's data into Google Sheet
driver.get(google_form_url)

properties_added = 0

for address in addresses:
    sleep(1)
    property_index = addresses.index(address)

    address_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address_input.send_keys(address)
    rent_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    rent_input.send_keys(prices[property_index])
    link_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input.send_keys(links[property_index])

    submit_button = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    submit_button.click()
    sleep(1)
    submit_another = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    submit_another.click()

    properties_added += 1
    print(f"Added property:\n{address}\n{prices[property_index]}\n{links[property_index]}\nTotal added: {properties_added}")

driver.close()