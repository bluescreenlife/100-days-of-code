'''Checks internet speeds, tweets at ISP provider if speeds are below promised speeds.'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from dotenv import load_dotenv

# get X login credentials
load_dotenv()
X_USERNAME = os.environ.get("X_USERNAME")
X_PW = os.environ.get("X_PW")

# internet speed variables (1GBPS)
PROMISED_DOWN = 1000
PROMISED_UP = 1000
CHROME_DRIVER_PATH = ChromeDriverManager().install()

class InternetSpeedXBot:
    def __init__(self, promised_down=PROMISED_DOWN, promised_up=PROMISED_UP):
        '''Initialize webdriver and promised speeds to check.'''
        self.service = Service(CHROME_DRIVER_PATH)
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        # self.options.add_argument("--headless") # enable/disable headless mode
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.promised_down = promised_down
        self.promised_up = promised_up
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        '''Runs speed test, returns download and upload speeds as ints.'''
        self.driver.get("https://fast.com/")
        sleep(20)
        download_speed = self.driver.find_element(By.XPATH, "//*[@id='speed-value']").text
        self.down = int(download_speed)
        more_info_button = self.driver.find_element(By.XPATH, "//*[@id='show-more-details-link']")
        more_info_button.click()
        sleep(15)
        upload_speed = self.driver.find_element(By.XPATH, "//*[@id='upload-value']").text
        self.up = int(upload_speed)

    def tweet_at_provider(self):
        '''Tweets at USI given a download and upload speed to report.'''
        self.driver.get("https://twitter.com/")

        # sign in steps
        sign_in = WebDriverWait(self.driver, 11.2).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div")))
        sign_in.click()
        
        sleep(5)

        email_input = WebDriverWait(self.driver, 7.6).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")))
        email_input.send_keys(X_USERNAME)
        email_input.send_keys(Keys.ENTER)

        pw_input = WebDriverWait(self.driver, 7.1).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")))
        pw_input.send_keys(X_PW)
        pw_input.send_keys(Keys.ENTER)

        # tweet steps
        tweet_button = WebDriverWait(self.driver, 30.5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")))
        tweet_button.click()

        tweet_box = WebDriverWait(self.driver, 5.1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")))
        tweet_box.send_keys(f"Hey @usifiber, my advertised speed is {PROMISED_DOWN}MBPS down/{PROMISED_UP}MBPS up and I'm receiving {self.down}MBPS down/"
                            f"{self.up}MBPS up. This tweet was automated via a Python script.")

        try:
            post_button = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/span")
            post_button.click()
        except ElementClickInterceptedException:
            try:
                boost_security_dismiss = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div/svg")
                boost_security_dismiss.click()
            except NoSuchElementException:
                unlock_more_dismiss = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div/svg")
                unlock_more_dismiss.click()
                
        self.driver.close()

if __name__ == "__main__":
    bot = InternetSpeedXBot()
    print("Running speed test...")
    bot.get_internet_speed()
    print(f"Download speed: {bot.down} | Upload speed: {bot.up}")
    sleep(5)
    if bot.down < bot.promised_down or bot.up < bot.promised_up:
        print("Speeds lower than promised... tweeting at USI...")
        bot.tweet_at_provider() # X does not like bot logins - forces quit after login
        print("Tweet successful.")
    else:
        print("Speeds are within promised range.")