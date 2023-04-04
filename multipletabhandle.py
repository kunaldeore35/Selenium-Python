from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
service = Service("C:/Users/KD00821059/Documents/KD Auto/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
# driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

# driver.find_element(By.XPATH,"//a[text()='Click Here']").click()
# time.sleep(1)
# parent = driver.window_handles[0]
# childs = driver.window_handles[1]
# driver.switch_to.window(childs)
# time.sleep(3)
# t = driver.find_element(By.XPATH,"//h3[text()='New Window']").text
# print(t)
# driver.close()
# driver.switch_to.window(parent)
# time.sleep(5)
# print(driver.title)

#Not working *************************************************************
# links = driver.find_elements(By.XPATH,"//a")
# # print(len(links))
# for i in range(len(links)):
#     driver.find_element(By.XPATH,"//a").click()
#     time.sleep(2)
#**************************************************************

# parent = driver.window_handles[0]
# windows = driver.window_handles
# totalwins = len(windows)
#
# for j in range(totalwins):
#     if j!=parent:
#         driver.switch_to.window(j)
#         time.sleep(2)

# driver.close()


