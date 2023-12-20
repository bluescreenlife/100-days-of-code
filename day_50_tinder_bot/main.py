'''Automatic Tinder swipe-right bot'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv

# load login credentials
load_dotenv()

FB_EMAIL = os.environ.get("FACEBOOK_EMAIL")
FB_PW = os.environ.get("FACEBOOK_PW")

# webdriver set up
chromedriver_path = ChromeDriverManager().install()
service = Service(chromedriver_path)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

# open Tinder, wait for loading
driver.get("http://www.tinder.com")

# accept cookies
cookies = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button")))
cookies.click()

# find login button, click
login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")))
login_button.click()
time.sleep(2)

# find log in with facebook button, click
login_with_fb = driver.find_element(By.XPATH, "//*[@id='u647161393']/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button")
login_with_fb.click()
time.sleep(2)

# switch to front window (facebook login)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# enter login info, login
email_input_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/form/div/div[1]/div/input")))
email_input_box.send_keys(FB_EMAIL)
time.sleep(2)

pw_input_box = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/form/div/div[2]/div/input")
pw_input_box.send_keys(FB_PW)
pw_input_box.send_keys(Keys.ENTER)

# switch back to main window
driver.switch_to.window(base_window)
time.sleep(5)

# allow location
try:
    allow_location = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]")))
    allow_location.click()
except NoSuchElementException:
    pass

# allow notifications
try:
    disallow_notifications = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='u647161393']/main/div/div/div/div[3]/button[2]")))
    disallow_notifications.click()
except NoSuchElementException:
    pass

# close tinder web exclusive banner
try:
    close_banner = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='u-1919424827']/div/div[1]/div/main/div[1]/div/button")))
    close_banner.click()
except NoSuchElementException:
    pass
time.sleep(15)

# click like on 50 people
like_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")))

for n in range(50):
    time.sleep(1)
    try:
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup_close = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/main/div/div[1]/div/div[4]/button")
            match_popup_close.click()
        except NoSuchElementException:
            try:
                no_add_to_home_screen = driver.find_element(By.XPATH, "//*[@id='o392470796']/main/div/div[2]/button[2]")
                no_add_to_home_screen.click()
            except NoSuchElementException:
                tinder_plus_close = driver.find_element(By.XPATH, "//*[@id='u647161393']/main/div/div[2]/button")
                tinder_plus_close.click()
                print("Out of likes for today, please try again tomorrow.")
                break