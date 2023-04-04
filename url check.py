from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:/Users/KD00821059/Documents/KD Auto/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# print(driver.current_url)
# print(driver.title)
class Check_url():
    def __init__(self,title,url):
        self.title = title
        self.url = url
        # self.element = element
        driver.get(self.url)
    def checktitle(self):
        print(driver.title)
        # print(self.title)
        if self.title == driver.title:
            return f"Correct Title"
        else:
            return f"Wrong Title"
    def checkurl(self):
        # print(self.url)
        # print(driver.current_url)
        if self.url == driver.current_url:
            return f"Correct URL"
        else:
            return f"Wrong URL"
    def checkelement(self):
        element = driver.find_element(By.ID,self.element)
        element.send_keys("kudeore@fb.com")
        time.sleep(5)
    def btn(self):
        driver.find_element("xpath","//input[@value='Submit']").click()
        time.sleep(3)
    def msg(self):
        mesg = driver.find_element("xpath","//div[@class='alert alert-success alert-dismissible']").text
        # print(mesg)
        assert "Success" in mesg
        return "All test case passed"
url = Check_url("ProtoCommerce","https://rahulshettyacademy.com/angularpractice/")
print(url.checktitle())
print(url.checkurl())
# url.checkelement()
url.btn()
url.msg()
print(url.msg())

