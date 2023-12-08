from selenium import webdriver
from selenium.webdriver.common.by import By
# from dotenv import load_dotenv
# import os

# load_dotenv()
# email = os.environ.get("EMAIL")
# pw = os.environ.get("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3773748741&f_AL=true&f_E=1%2C2&geoId=103039849&keywords=qa%20tester&location=Minneapolis%2C%20Minnesota%2C%20United%20States&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

sign_in_button = driver.find_element(By.XPATH, "/html/body/div[3]/a[1]")
sign_in_button.click()

email_input = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[1]/input")
email_input.send_keys("andrewvanderleest@gmail.com")

pw_input = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[2]/input")
pw_input.send_keys("rjwY9cr&66rT")

signin_button = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
signin_button.click()

job_list = driver.find_element(By.CLASS_NAME, "scaffold-layout__list-container")
jobs = job_list.find_elements(By.TAG_NAME, "li")

job_ids = []

for job in jobs:
    job_id = job.get_attribute("id")
    if job_id != "":
        job_ids.append(job_id)

for job_id in job_ids:
    job_element = driver.find_element(By.ID, job_id)
    job_link = job_element.find_element(By.TAG_NAME, "a")
    job_link.click()

    buttons_element = driver.find_element(By.CLASS_NAME, "job-details-jobs-unified-top-card__content--two-pane")
    buttons = buttons_element.find_elements(By.TAG_NAME, "button")
    for button in buttons:
        span_text = button.find_element(By.CSS_SELECTOR, "span.aria-hidden").text
        if span_text == "Save":
            button.click()
    # apply_button = buttons[2]
    # save_button = buttons[3]
    # save_button.click()