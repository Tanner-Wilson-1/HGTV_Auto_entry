from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config
import CatFacts

#set some variables
hgtv_url = 'https://www.hgtv.com/sweepstakes/hgtv-smart-home/sweepstakes'
foodnetwork_url = 'https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-smart-home-sweepstakes'
HGTV_ngxFrame = 'ngxFrame243797'
foodnetwork_ngxFrame = 'ngxFrame243801'
all_email = config.entry_emails
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
send_success_emails = config.success_emails
my_email = config.my_email

# Use Selenium to enter both sweeps for each email in 'all_email'
# to-do add try catch blocks to account for failures instead of assuming it works
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

    print(emails + " has been entered into HGTV.")
    time.sleep(10)

    browser.get(foodnetwork_url)
    browser.maximize_window()

    time.sleep(5)
    browser.switch_to.frame(browser.find_element(By.ID, foodnetwork_ngxFrame))

    time.sleep(2)
    email_input = browser.find_element(By.ID, "xReturningUserEmail")
    email_input.send_keys(emails)

    time.sleep(2)
    sign_up = browser.find_element(By.ID, "xCheckUser")
    sign_up.click()

    browser.switch_to.default_content()
    time.sleep(2)
    browser.switch_to.frame(browser.find_element(By.ID, foodnetwork_ngxFrame))
    action = ActionChains(browser)
    action.send_keys(Keys.TAB)
    action.send_keys(Keys.ENTER)
    action.perform()

    time.sleep(5)
    print(emails + " has been entered into Food Network.")
browser.quit()

# setup for sending confirmation emails
password = config.password
# To-do: Make it so it doesn't share a fact that's already been sent
content = "Enjoy today's Cat Fact! \n" + CatFacts.get_cat_facts()

# to-do: Move email into the original for loop and only send if successfully entered
for email in send_success_emails:
    message = MIMEMultipart()
    message['From'] = my_email
    message['To'] = email
    message['Subject'] = 'Automagically sent from Tanner!'
    message.attach(MIMEText(content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(my_email, password) #login with mail_id and password
    text = message.as_string()
    session.sendmail(my_email, email, text)
    session.quit()
    print('Mail Sent to: ' + email)
# Running this via Windows task scheduler, so need to exit the script to avoid next day failures
exit()
