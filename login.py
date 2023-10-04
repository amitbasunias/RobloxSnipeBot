from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
from datetime import datetime

def setup():
  print('--->Setup selenium start : '+str(datetime.now()))
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-gpu')
  chrome_options.add_argument(r'--user-data-dir=C:\Users\amit\AppData\Local\Google\Chrome\User Data')
  chrome_options.add_argument(r'--profile-directory=Profile 1')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
#  chrome_options.add_argument('--force-dark-mode')
#  chrome_options.add_argument("--window-size=2560,1440")
#  capabilities = {
  # "resolution": "2560X1440"
  #  "resolution": "1280X720"
  # "resolution": "768X432"
  #}
  driver = webdriver.Chrome(r'C:\Users\amit\Downloads\chromedriver_win32\chromedriver.exe', options=chrome_options)
  print('Setup selenium complete')
  return driver
def login(input_user,input_pass):
    driver = setup()
    driver.get("https://www.roblox.com/login")
    username = driver.find_element(By.ID,("login-username"))
    password = driver.find_element(By.ID,("login-password"))
    login = driver.find_element(By.ID,"login-button")

    username.send_keys(str(input_user))
    password.send_keys(str(input_pass))
    time.sleep(5)
    login.click()
    time.sleep(10)


