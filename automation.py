from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service("C:/Users/KD00821059/Documents/KD Auto/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com")
print(driver.current_url)