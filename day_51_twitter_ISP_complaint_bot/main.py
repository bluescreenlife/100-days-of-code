from distutils.command import upload
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
import os
from dotenv import load_dotenv

# get X login credentials
load_dotenv()
X_USERNAME = os.environ.get("X_USERNAME")
X_PW = os.environ.get("X_PW")

# internet speed variables (1GBPS)
PROMISED_DOWN = 800
PROMISED_UP = 800
CHROME_DRIVER_PATH = "/Users/andrew/Developer/chromedriver"

class InternetSpeedXBot:
    def __init__(self, up=PROMISED_UP, down=PROMISED_DOWN):
        '''Initialize webdriver and promised speeds to check.'''
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.down = up
        self.up = down

    def get_internet_speed(self):
        '''Runs speed test, returns download and upload speeds as ints.'''
        self.driver.get("https://fast.com/")
        sleep(10)
        download_speed = self.driver.find_element(By.XPATH, "//*[@id='speed-value']").text
        more_info_button = self.driver.find_element(By.XPATH, "//*[@id='show-more-details-link']")
        more_info_button.click()
        sleep(10)
        upload_speed = self.driver.find_element(By.XPATH, "//*[@id='upload-value']").text
        self.driver.quit()
        return int(download_speed), int(upload_speed)

    def tweet_at_provider(self, download_speed, upload_speed):
        '''Tweets at USI given a download and upload speed to report.'''
        self.driver.get("https://twitter.com/")
        sleep(5)

        # sign in steps
        sign_in = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div")
        sign_in.click()
        sleep(5)
        email_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_input.send_keys(X_USERNAME)
        sleep(5)
        next_button = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
        next_button.click()
        sleep(10)
        pw_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        pw_input.send_keys(X_PW)
        sleep(5)
        log_in = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span")
        log_in.click()
        sleep(35)

        # tweet steps - non functioning as it seems that X forces browser to quit after a bot login...
        tweet_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
        tweet_button.click()
        sleep(2)
        tweet_box = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet_box.send_keys(f"Hey @usifiber, my advertised speed is 1GBPS down/1GBPS up and I'm receiving {download_speed}MBPS down/"
                            f"{upload_speed}MBPS up. This tweet was automated via a Python script.")
        sleep(2)
        post_button = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/span")
        post_button.click()


if __name__ == "__main__":
    bot = InternetSpeedXBot()
    print("Running speed test...")
    down, up = bot.get_internet_speed()
    print(f"Download speed: {down} | Upload speed: {up}")
    sleep(20) # seems to be an issue with opening another driver instance soon after another
    if down < PROMISED_DOWN or up < PROMISED_UP:
        print("Speeds lower than promised... tweeting at USI...")
        bot.tweet_at_provider(download_speed=down, upload_speed=up) # X does not like bot logins - forces quit after login
        print("Tweet successful.")
    else:
        print("Speeds are within promised range.")