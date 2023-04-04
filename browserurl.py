from selenium.webdriver.support.select import Select
from chrome_driver import drive
from selenium.webdriver.common.by import By

import time
driver = drive()

class Input():
    def __init__(self,url):
        # self.title = title
        self.url = url
        driver.maximize_window()
        driver.get(self.url)
    # def checktitle(self):
    #     if driver.title == self.title:
    #         return f"Correct Title"
    #     else:
    #         return f"Wrong Title"
    def checkname(self,name):
        nm = driver.find_element(By.NAME,"name")
        nm.send_keys(name)
        time.sleep(2)
    def checkemail(self,email):
        emails = driver.find_element(By.NAME,"email")
        emails.send_keys(email)
        time.sleep(2)

    def checkpassword(self,password):
        passw = driver.find_element(By.ID,"exampleInputPassword1")
        passw.send_keys(password)
        time.sleep(2)
    def checkbox(self):
        # driver.find_element(By.ID,"").click()
        driver.find_element("xpath", "//input[@id = 'exampleCheck1']").click()
        time.sleep(2)
    def gender(self):
        select = Select(driver.find_element("xpath", "//select[@id = 'exampleFormControlSelect1']"))
        # select.select_by_index(1)
        select.select_by_visible_text('Male')
        time.sleep(2)
    def radio(self):
        # driver.find_element(By.ID,"inlineRadio2").click()
        driver.find_element("xpath","//input[@id='inlineRadio2']").click()
        time.sleep(2)
    def submitbtn(self):
        driver.find_element("xpath", "//input[@value='Submit']").click()
        time.sleep(2)
    def msg(self):
        mesg = driver.find_element("xpath", "//div[@class='alert alert-success alert-dismissible']").text
        # print(mesg)
        assert "Success" in mesg
        return "All test cases are passed"













