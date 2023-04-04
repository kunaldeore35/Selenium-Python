from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

service = Service("C:/Users/KD00821059/Documents/KD Auto/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

sel = driver.find_elements(By.XPATH,"//div/fieldset/select[@id='dropdown-class-example']/option")
l = len(sel)
for j in range(1,l):
    # print(j)
    for i in sel:
        # print(i.text)
        # print(j)
        if "Option" in i.text:
            select = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
            select.select_by_index(j)
            time.sleep(2)
            print(driver.find_element(By.ID, "dropdown-class-example").get_attribute("value"))
            break
# //select[@id='dropdown-class-example']/
# select = Select(driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))

# Auto suggest Dynamic Dropdown
# driver.find_element(By.ID,"autosuggest").send_keys("Ind")
# time.sleep(2)
# country = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")
# time.sleep(3)
# for i in country:
#     # print(i.text)
#     if i.text == "India":
#         i.click()
#         time.sleep(3)
#         print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

# Multiple Check boxes #
# checkboxes = driver.find_elements(By.XPATH,"//div/fieldset/label/input[@type='checkbox']")
# time.sleep(3)
# print(len(checkboxes))
# for i in checkboxes:
#     print(i.get_attribute('value'))
#     if i.get_attribute('value') == "option2":
#         i.click()
#         time.sleep(2)

# Radio Button #
# radiobtn = driver.find_elements(By.XPATH,"//div/div/fieldset/label/input[@class='radioButton']")
# time.sleep(2)
# print(len(radiobtn))
# for i in radiobtn:
#     # print(i.get_attribute('value'))
#     if i.get_attribute('value') == "radio2":
#         i.click()
#         time.sleep(2)

# Alert Box #
# driver.find_element(By.ID,"name").send_keys("Kunal")
# alert = driver.find_element(By.ID,"alertbtn").click()
# al = driver.switch_to.alert
# print(al.text)
# time.sleep(2)
# if "Kunal" in al.text:
#     print("True Value")
# alert2 = driver.find_element(By.ID,"confirmbtn").click()
# al = driver.switch_to.alert
# time.sleep(2)
# al.accept()
# time.sleep(2)
# al.dismiss()
# time.sleep(2)
# driver.switch_to.alert

