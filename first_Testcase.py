import time
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.flightradar24.com/data/airports/pnq/arrivals")

total_rows = len(driver.find_elements(By.XPATH, "//tbody//tr/td[3]")) # total no of rows in table
print(total_rows)

total_columns = len(driver.find_elements(By.XPATH, "//tbody//tr[104]/td")) # total no of columns in table
print(total_columns)


for r in range(104, 178):
    for c in range(1, total_columns+1):
        value = driver.find_element(By.XPATH, "//tbody//tr[" + str(r) + "]/td[3]//span").text
        value1 = driver.find_element(By.XPATH, "//tbody//tr[" + str(r) + "]/td[7]").text
        print(value + ": " + value1)
        break
        # if value == "Delhi" or value == "Bengaluru" or value == "Goa" or value == "Dubai":
        #     print(value + ": " + value1)
        #     break
