from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
service = Service("C:/Users/KD00821059/Documents/KD Auto/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
# driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

text = "My name is kunal"
time.sleep(3)
driver.switch_to.frame('mce_0_ifr')
time.sleep(3)
driver.find_element(By.CLASS_NAME,"mce-content-body ").clear()
time.sleep(3)
driver.find_element(By.CLASS_NAME,"mce-content-body ").send_keys(text)
time.sleep(3)

driver.switch_to.default_content()
print(driver.find_element(By.XPATH,"//div/h3").text)


