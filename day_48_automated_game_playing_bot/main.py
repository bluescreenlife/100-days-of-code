'''bot for cookie-clicker: https://orteil.dashnet.org/experiments/cookie/'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

# times to check upgrades and 
timeout = time.time() + 3 # seconds
thirty_min = time.time() + 60*30  # 30 minutes

def get_balance():
    '''Returns current player balance.'''
    money = driver.find_element(By.ID, "money").text
    if "," in money:
        money = money.replace(",", "")
    return int(money)

def get_most_valuable_upgrade(balance):
    '''Scrapes the shop elements and returns the highest-priced upgrade user can afford.'''
    upgrades = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
    
    upgrade_names = []
    upgrade_prices = []

    # collect names and prices of upgrades
    for upgrade in upgrades[:8]:
        upgrade_details = upgrade.text
        upgrade_names.append(upgrade_details.split("-")[0].strip())
        upgrade_price = upgrade_details.split("-")[1].strip()
        if "," in upgrade_price:
            upgrade_price = upgrade_price.replace(",", "")
        upgrade_price = int(upgrade_price)
        upgrade_prices.append(upgrade_price)

    # select most valuable upgrade below user balance
    affordable_upgrades = [price for price in upgrade_prices if price < balance]
    if affordable_upgrades:
        most_valuable_upgrade = upgrade_names[upgrade_prices.index(max(affordable_upgrades))]
        return most_valuable_upgrade
    else:
        return None

def purchase_upgrade(item):
    # click a given upgrade
    id_str = "buy" + item
    element = driver.find_element(By.ID, id_str)
    element.click()
    print(f"{item} purchased.")

# main loop
print("SMASHIN' COOKIES...")

while True:
    cookie.click()

    # check for and purchase upgrades every 3 seconds
    if time.time() > timeout:
        balance = get_balance()
        best_upgrade = get_most_valuable_upgrade(balance)
        if best_upgrade:
            purchase_upgrade(best_upgrade)
        timeout = time.time() + 3

    # end after 30 minutes
    if time.time() >= thirty_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(f"Script finished. {cookie_per_s}")
        break