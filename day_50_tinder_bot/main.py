'''Automatic Tinder swipe-right bot'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv
from random import randint

load_dotenv()

FB_EMAIL = os.environ.get("FACEBOOK_EMAIL")
FB_PW = os.environ.get("FACEBOOK_PW")

# webdriver set up
# chromedriver_path = "/Users/andrew/Developer/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

# open Tinder, wait for loading
driver.get("http://www.tinder.com")
# driver.get("")

# accept cookies
cookies = WebDriverWait(driver, randint(10,12)).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button")))
cookies.click()

# find login button, click
login_button = WebDriverWait(driver, randint(3,7)).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")))
login_button.click()

time.sleep(randint(9,11))

# find log in with facebook button, click
login_with_fb = driver.find_element(By.XPATH, "//*[@id='u647161393']/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button")
login_with_fb.click()

time.sleep(randint(10,13))

# switch to front window (facebook login)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# enter login info, login
email_input_box = WebDriverWait(driver, 5.1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/form/div/div[1]/div/input")))
email_input_box.send_keys(FB_EMAIL)

driver.implicitly_wait(1.3)

pw_input_box = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/form/div/div[2]/div/input")
pw_input_box.send_keys(FB_PW)
pw_input_box.send_keys(Keys.ENTER)

# switch back to main window
driver.switch_to.window(base_window)

time.sleep(randint(9,11))

# seems to be a fail point here where Tinder recognizes bot and quits the browser

try:
    allow_location = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]")))
    allow_location.click()
except NoSuchElementException:
    pass

time.sleep(randint(10,13))

# allow notifications
try:
    allow_notifications = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]")))
    time.sleep(10)
    allow_notifications.click()
except NoSuchElementException:
    pass

# close tinder web exclusive banner
try:
    close_banner = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='u-1919424827']/div/div[1]/div/main/div[1]/div/button")))
    close_banner.click()
except NoSuchElementException:
    pass

driver.implicitly_wait(11.1)

# locate like button
try:
    like = WebDriverWait(driver, 10.4).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")))
except NoSuchElementException:
    time.sleep(5.2)
    like = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")

for n in range(10):
    driver.implicitly_wait(1)
    try:
        like.click()
    except ElementClickInterceptedException:
        try:
            match_popup_close = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/main/div/div[1]/div/div[4]/button")
            match_popup_close.click()
        except NoSuchElementException:
            try:
                no_add_to_home_screen = driver.find_element(By.XPATH, "//*[@id='o392470796']/main/div/div[2]/button[2]")
                no_add_to_home_screen.click()
            except NoSuchElementException:
                driver.implicitly_wait(2)