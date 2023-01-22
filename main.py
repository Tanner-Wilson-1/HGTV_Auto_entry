from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

hgtv_url = 'https://www.hgtv.com/sweepstakes/hgtv-dream-home/sweepstakes'
foodnetwork_url = 'https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-dream-home-sweepstakes'
HGTV_ngxFrame = 'ngxFrame230599'
foodnetwork_ngxFrame = 'ngxFrame230603'
all_email = ['tannerw2013@gmail.com', 'KevinBiedrzycki@gmail.com', 'meghannlkirby@gmail.com']
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for emails in all_email:
    browser.get(hgtv_url)
    browser.maximize_window()

    time.sleep(2)
    browser.switch_to.frame(browser.find_element(By.ID, HGTV_ngxFrame))

    time.sleep(2)
    email_input = browser.find_element(By.ID, "xReturningUserEmail")
    email_input.send_keys(emails)

    time.sleep(2)
    sign_up = browser.find_element(By.ID, "xCheckUser")
    sign_up.click()

    browser.switch_to.default_content()
    time.sleep(2)
    browser.switch_to.frame(browser.find_element(By.ID, HGTV_ngxFrame))
    action = ActionChains(browser)
    action.send_keys(Keys.TAB)
    action.send_keys(Keys.ENTER)
    action.perform()

    time.sleep(10)

    browser.get(foodnetwork_url)
    browser.maximize_window()

    time.sleep(2)
    browser.switch_to.frame(browser.find_element(By.XPATH, foodnetwork_ngxFrame))

    time.sleep(2)
    email_input = browser.find_element(By.ID, "xReturningUserEmail")
    email_input.send_keys(emails)

    time.sleep(2)
    sign_up = browser.find_element(By.ID, "xCheckUser")
    sign_up.click()

    browser.switch_to.default_content()
    time.sleep(2)
    browser.switch_to.frame(browser.find_element(By.XPATH, foodnetwork_ngxFrame))
    action = ActionChains(browser)
    action.send_keys(Keys.TAB)
    action.send_keys(Keys.ENTER)
    action.perform()

    time.sleep(5)

browser.quit()
