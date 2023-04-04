from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

service = Service("C:/Users/KD00821059/Documents/KD Auto/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.messenger.com/")
driver.maximize_window()

def id(email):
    driver.find_element(By.ID,"email").send_keys(email)
    time.sleep(5)
def pas(password):
    driver.find_element(By.ID,"pass").send_keys(password)
    time.sleep(5)
def btn():
    driver.find_element(By.ID,"loginbutton").click()
    time.sleep(15)
    # driver.find_element(By.XPATH,"//div[@class='x1ey2m1c xds687c xg01cxk x47corl x10l6tqk x17qophe x13vifvy x1ebt8du x19991ni x1dhq9h x1wpzbip x14yjl9h xudhj91 x18nykt9 xww2gxu']")
    # driver.find_element(By.XPATH,"//div[@class='x1ey2m1c xds687c xg01cxk x47corl x10l6tqk x17qophe x13vifvy x1ebt8du x19991ni x1dhq9h x1wpzbip x14yjl9h xudhj91 x18nykt9 xww2gxu']").click()
    # time.sleep(5)
# def search(name):
#     driver.find_element(By.XPATH,"//input[@type='search']").send_keys(name)
#     time.sleep(5)


id("59846010033596")
pas("lsspl#123")
btn()
# search("li")