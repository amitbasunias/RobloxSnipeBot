from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,csv
from datetime import datetime


driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://www.roblox.com/CATALOG?Category=2&Subcategory=2&CurrencyType=3&pxMin=1000&SortType=3")

time.sleep(20)

driver.execute_script("window.scrollTo(0, 200)")

links = driver.find_elements(By.TAG_NAME, 'a')

def getLinks():
    temp_urls = []
    for link in links:
        url = link.get_attribute('href')
        temp_urls.append(url)

    final_urls = []

    for urls in temp_urls:
        urls = str(urls)
        if(urls.startswith('https://www.roblox.com/catalog/')):
            final_urls.append(urls)

    return final_urls

def saveToCSV(row):
    with open('purchased.csv', 'a') as f:
  
        writer = csv.writer(f)

        writer.writerow([row])

def traverseURL(final_urls):
    for link in final_urls:
        driver.get(link)
        time.sleep(1)
        try:
            best_price = driver.find_element(By.XPATH,('//*[@id="item-details"]/div[1]/div[1]/div[2]/div/span[2]')).get_attribute('innerHTML')
            best_price = best_price.strip('')
            best_price = best_price.replace(',', '')
        except:
            continue
        try:
            avg_price = driver.find_element(By.XPATH,('//*[@id="item-average-price"]')).get_attribute('innerHTML')
            avg_price = avg_price.strip('')
            avg_price = avg_price.replace(',', '')
        except:
            continue

        if(float(best_price)<=float(avg_price)*0.7):
            time.sleep(3)
            buy = driver.find_element(By.CLASS_NAME,'action-button')
            buy.click()

            now = datetime.now()
            dt = now.strftime("%H:%M:%S %d/%m/%Y")
            saveToCSV(str(best_price) + ',' + str(link)+ ',' + dt)

def scrollPage(i):
    while(i>0):
        time.sleep(3)

        height = int(driver.execute_script("return document.documentElement.scrollHeight"))
        driver.execute_script("window.scrollTo(0, {})".format(height))
        i-=1
links = driver.find_elements(By.TAG_NAME, 'a')
current_links = getLinks()
traverseURL(current_links)

while(True):

    scrollCounter = 1

    prev_links = current_links

    driver.get("https://www.roblox.com/CATALOG?Category=2&Subcategory=2&CurrencyType=3&pxMin=1000&SortType=3")

    scrollPage(scrollCounter)
    time.sleep(20)
    links = driver.find_elements(By.TAG_NAME, 'a')

    current_links = getLinks()

    current_links = list(set(current_links).symmetric_difference(set(prev_links)))

    traverseURL(current_links)

    scrollCounter+=1
