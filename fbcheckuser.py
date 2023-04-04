from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:/Users/KD00821059/Documents/KD Auto/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

class Fbusr():
    def __init__(self,url):
        self.url = url
        driver.get(self.url)
        driver.maximize_window()
    def eml(self,email):
        id = driver.find_element(By.XPATH,"//input[@id='email']")
        id.send_keys(email)
        time.sleep(2)
    def pwd(self,password):
        pswd = driver.find_element(By.XPATH,"//input[@id='pass']")
        pswd.send_keys(password)
        time.sleep(2)
    def login(self):
        driver.find_element(By.XPATH,"//div/button[@name='login']").click()
        time.sleep(10)
    def chkusr(self,name):
        usernm = driver.find_element("xpath","//div/div/div/div/div/span/span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6']").text
        if usernm == name:
            return "Successfully logged in...."
        else:
            return "Kuch to gadbad hai JHATUU"    


user = Fbusr("https://www.facebook.com/")
user.eml("59846010033596")
user.pwd("lsspl#123")
user.login()
print(user.chkusr("Shinigami"))
