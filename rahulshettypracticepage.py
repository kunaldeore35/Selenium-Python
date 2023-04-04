from selenium.webdriver.support.select import Select
from chrome_driver import drive
from selenium.webdriver.common.by import By
import time
driver = drive()

class Automation:
    def __init__(self,url):
        self.url = url
        driver.maximize_window()
        driver.get(self.url)
    def dynamicdrop(self,val):
        driver.find_element(By.ID, "autosuggest").send_keys(val)
        time.sleep(2)
        country = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")
        time.sleep(3)
        for i in country:
            # print(i.text)
            if i.text == "India":
                i.click()
                time.sleep(3)
                print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

    def multicheck(self):
        checkboxes = driver.find_elements(By.XPATH,"//div/fieldset/label/input[@type='checkbox']")
        time.sleep(3)
        # print(len(checkboxes))
        for i in checkboxes:
            # print(i.get_attribute('value'))
            i.click()
            time.sleep(1)
            # if i.get_attribute('value') == "option2":
            #     i.click()
            #     time.sleep(2)
    def multiradio(self):
        radiobtn = driver.find_elements(By.XPATH, "//div/div/fieldset/label/input[@class='radioButton']")
        time.sleep(2)
        # print(len(radiobtn))
        for i in radiobtn:
            # print(i.get_attribute('value'))
            if i.get_attribute('value') == "radio2":
                i.click()
                time.sleep(2)
    def alertbox1(self,name):
        driver.find_element(By.ID,"name").send_keys(name)
        driver.find_element(By.ID,"alertbtn").click()
        al = driver.switch_to.alert
        # print(al.text)
        time.sleep(2)
        if name in al.text:
            print("True Value")
            al.accept()
    def alertbox2(self):
        driver.find_element(By.ID,"confirmbtn").click()
        al2 = driver.switch_to.alert
        time.sleep(2)
        al2.accept()

    def dynamicdrops(self, val):
        driver.find_element(By.ID, "autocomplete").send_keys(val)
        time.sleep(2)
        country = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/div")
        time.sleep(3)
        for i in country:
            # print(i.text)
            if i.text == "India":
                i.click()
                time.sleep(3)
                print(driver.find_element(By.ID, "autocomplete").get_attribute("value"))

    def dropd(self):
        sel = driver.find_elements(By.XPATH, "//div/fieldset/select[@id='dropdown-class-example']/option")
        l = len(sel)
        for j in range(1, l):
            # print(j)
            for i in sel:
                # print(i.text)
                # print(j)
                if "Option" in i.text:
                    select = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
                    select.select_by_index(j)
                    time.sleep(1)
                    print(driver.find_element(By.ID,"dropdown-class-example").get_attribute("value"))
                    break






