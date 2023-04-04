from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:/Users/KD00821059/Documents/KD Auto/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

class Csschk():
    def __init__(self,url):
        self.url = url
        driver.maximize_window()
        driver.get(self.url)

    def checkname(self, names):
        nm = driver.find_element(By.CSS_SELECTOR, "input[name = 'name']")
        nm.send_keys(names)
        # time.sleep(2)
    def checkemail(self,email):
        emails = driver.find_element(By.CSS_SELECTOR,"input[name = 'email']")
        emails.send_keys(email)
        # time.sleep(2)

    def checkpassword(self,password):
        passw = driver.find_element(By.CSS_SELECTOR,"#exampleInputPassword1")
        passw.send_keys(password)
        # time.sleep(2)
    def checkbox(self):
        # driver.find_element(By.ID,"").click()
        driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
        # time.sleep(2)
    def gender(self):
        select = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
        # select.select_by_index(1)
        select.select_by_visible_text('Male')
        # time.sleep(2)
    def radio(self):
        # driver.find_element(By.ID,"inlineRadio2").click()
        driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
        # time.sleep(2)
    def submitbtn(self):
        driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
        time.sleep(2)
    def msg(self):
        mesg = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
        
        # print(mesg)
        assert "Success" in mesg
        return "All test cases are passed"


cs = Csschk("https://rahulshettyacademy.com/angularpractice/")
cs.checkname("KD Bhai")
cs.checkemail("kdbhaikd@kddon.com")
cs.checkpassword("Me hu DON")
cs.checkbox()
cs.gender()
cs.radio()
cs.submitbtn()
print(cs.msg())
