from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
service = Service("C:/Users/KD00821059/Documents/KD Auto/chromedriver_win32/chromedriver.exe")
# It will run chrome tab into background
hidetab = webdriver.ChromeOptions()
hidetab.add_argument('--headless')
driver = webdriver.Chrome(service=service,options=hidetab)

# driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,1000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

print("Program run successfully")