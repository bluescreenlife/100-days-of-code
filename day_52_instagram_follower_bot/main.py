'''Logs into an Instagram account, gets follower list of another account, and follows as many as possible.
Current viewable follower list for any account is 50 accounts, therefore this is the max this program can follow.

Instagram currently seems to have an invisible overlay element over the followers element 
to prevent bot clicks = this program is not currently operational for this reason.'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from dotenv import load_dotenv

CHROMEDRIVER_PATH = ChromeDriverManager().install()

# load login credentials
load_dotenv()
IG_USERNAME = os.environ.get("IG_USERNAME")
IG_PW = os.environ.get("IG_PW")
IG_TARGET_ACCT = "https://www.instagram.com/vinylmeplease/followers" # set to account for which you want to follow their followers

class InstaFollower:
    '''Logs into Instagram and follows all accounts of a specified account.'''
    def __init__(self, driver_path:str, username:str, password:str):
        self.service = Service(executable_path=driver_path)
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options, service=self.service)

        self.username = username
        self.pw = password

        self.accounts_to_follow = []

    def login(self):
        '''Logs in to Instagram, clears prompts.'''
        self.driver.get("https://www.instagram.com/")
        sleep(3)

        # log in
        username_input = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        username_input.send_keys(self.username)
        sleep(1)
        
        pw_input = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        pw_input.send_keys(self.pw)
        pw_input.send_keys(Keys.ENTER)
        sleep(3)
        
        # dismiss save login info prompt
        save_login_not_now = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Not now')]")
        if save_login_not_now:
            save_login_not_now.click()
        sleep(3)

        # dismiss notifications prompt
        try:
            notifications_not_now = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not now')]")
            notifications_not_now.click()
        except NoSuchElementException:
            try:
                notifications_not_now = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
                notifications_not_now.click()
            except NoSuchElementException:
                pass
        sleep(3)

    def find_followers(self, target_account:str):
        '''Retrieves list of follower elements.'''
        sleep(5)
        self.driver.get(target_account)
        
        self.accounts_to_follow = self.driver.find_elements(By.CLASS_NAME, "x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3")
        if self.accounts_to_follow:
            print(f"Located {len(self.accounts_to_follow)} followable accounts.")

        # remove any already-followed accounts
        for account in self.accounts_to_follow:
            if account.find_element(By.CLASS_NAME, "_ap3a _aaco _aacw _aad6 _aade").text == "Requested" or "Following":
                self.accounts_to_follow.remove(account)
        
    def follow(self):
        '''Clicks follow button on each follower element'''
        for account in self.accounts_to_follow:
            follow_button = account.find_element(By.CLASS_NAME, "_ap3a _aaco _aacw _aad6 _aade")
            follow_button.click()
            print("Follow confirmed.")
        print(f"Successfully followed all accounts. Quitting browser in 5s...")
        self.driver.close()


if __name__ == "__main__":
    instafollower = InstaFollower(CHROMEDRIVER_PATH, IG_USERNAME, IG_PW)
    instafollower.login()
    instafollower.find_followers(IG_TARGET_ACCT)
    instafollower.follow()