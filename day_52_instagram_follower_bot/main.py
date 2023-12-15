'''Logs into an Instagram account, gets follower list of another account, and follows as many as possible.'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
from dotenv import load_dotenv
from random import randint

load_dotenv()

CHROMEDRIVER_PATH = "/Users/andrew/Developer/chromedriver" # set to your local chromedriver path

# fetched from local .env file
IG_USERNAME = os.environ.get("IG_USERNAME")
IG_PW = os.environ.get("IG_PW")
IG_TARGET_ACCT = "https://www.instagram.com/vinylmeplease/" # set to account for which you want to follow their followers

class InstaFollower:
    def __init__(self, driver_path:str, username:str, password:str):
        self.service = Service(executable_path=driver_path)
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options, service=self.service)

        self.username = username
        self.pw = password

        self.accounts_to_follow = []

    def login(self):
        # wait_time_short = randint(1, 5)
        # wait_time_long = randint(10, 20)
        self.driver.get("https://www.instagram.com/")
        sleep(16.1)

        username_input = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        username_input.send_keys(self.username)
        sleep(1.2)
        
        pw_input = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        pw_input.send_keys(self.pw)
        pw_input.send_keys(Keys.ENTER)
        
        # IG seems to detect bot here and close browser if code run too many times
        
        sleep(16.2) # wait while page loads
        
        # dismiss save login info prompt
        save_login_not_now = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Not now')]")
        if save_login_not_now:
            save_login_not_now.click()
        sleep(3.2)

        # dismiss notifications prompt
        notifications_not_now = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not now')]")
        if notifications_not_now:
            notifications_not_now.click()

        print("Login complete. Waiting while page loads...")
        sleep(12.2) # wait while page loads

    def find_followers(self, target_account:str):
        self.driver.get(target_account)
        sleep(10.7) # wait while page loasd

        followers = self.driver.find_element(By.XPATH, "//*[@id='mount_0_0_g1']/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button")
        followers.click()
        sleep(11.2)

        followers_list_element = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]")
        followers_list = followers_list_element.find_elements(By.TAG_NAME, "div")
        self.accounts_to_follow = followers_list
        print(f"Number of followers found: {len(followers_list)}")
       
    def follow(self):
        for follower in self.accounts_to_follow:
            wait_time = randint(1, 3)
            sleep(wait_time)
            follow_button = follower.find_element(By.CLASS_NAME, " _acan _acap _acas _aj1- _ap30")
            if follow_button:
                follow_button.click()
                print("Followed 1 account.")
        print(f"Successfully followed all accounts.")


if __name__ == "__main__":
    instafollower = InstaFollower(CHROMEDRIVER_PATH, IG_USERNAME, IG_PW)
    instafollower.login()
    instafollower.find_followers(IG_TARGET_ACCT)
    instafollower.follow()