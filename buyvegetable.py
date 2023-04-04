from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
service = Service("C:/Users/KD00821059/Documents/KD Auto/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
# driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

def tc001search(vegetable):
    driver.find_element(By.CLASS_NAME,"search-keyword").send_keys(vegetable)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)

def tc002add(qty):
    ele1 = driver.find_elements("xpath","//div[@class='products']/div[@class='product']")
    # print(len(ele1))
    lst = []
    lst = ele1
    for i in range(len(ele1)):
        # print(lst[i])
        # time.sleep(2)
        for j in range(qty):
            lst[i].find_element(By.XPATH,"div[@class='stepper-input']/a[@class='increment']").click()
            j = j + 1
        time.sleep(5)

def tc003addtocart():
    ele1 = driver.find_elements("xpath", "//div[@class='products']/div[@class='product']")
    for i in ele1:
        i.find_element(By.XPATH,"//button[text()='ADD TO CART']").click()
        time.sleep(3)

def tc004opencart():
    driver.find_element("xpath","//img[@alt='Cart']").click()
    time.sleep(3)

def tc005proceed():
    driver.find_element("xpath","//button[text()='PROCEED TO CHECKOUT']").click()
    time.sleep(3)

def tc006promocode(code):
    driver.find_element(By.CLASS_NAME,"promoCode").send_keys(code)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"promoBtn").click()
    time.sleep(10)
    promocheck = driver.find_element(By.CLASS_NAME,"promoInfo").text
    # print(promocheck)
    discamt = driver.find_element(By.CLASS_NAME,"discountAmt").text
    if promocheck!="Code applied ..!" and checkdiscount()!=discamt:
        print("Code is not applied successfully")
    else:
        print("Code is applied successfully")


def checkdiscount():
    total = driver.find_element(By.CLASS_NAME,"totAmt").text
    t = int(total)
    ans = t-(t*0.10)
    # print(ans)

def tc007placeorder():
    driver.find_element("xpath","//button[text()='Place Order']").click()
    time.sleep(3)

def tc008country():
    countryselect = Select(driver.find_element("xpath","//select[@style='width: 200px;']"))
    countryselect.select_by_visible_text('India')
    time.sleep(3)

def tc009agree():
    driver.find_element(By.CLASS_NAME,"chkAgree").click()
    time.sleep(2)

def tc010proceed():
    driver.find_element("xpath","//button[text()='Proceed']").click()
    time.sleep(2)


tc001search("Ca")
tc002add(4)
tc003addtocart()
tc004opencart()
tc005proceed()
tc006promocode("rahulshettyacademy")
tc007placeorder()
tc008country()
tc009agree()
tc010proceed()