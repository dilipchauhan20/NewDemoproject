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
# driver = webdriver.Chrome(<Executable Path>)
driver.maximize_window()
driver.implicitly_wait(10)

# driver.get("https://www.epam.com")
#
# driver.find_element(By.XPATH, '//a[@href = "/services"]/parent::li').click()



driver.get("https://seleniumpractise.blogspot.com/2021/08/")

columns = driver.find_elements(By.XPATH, '//table[@id="customers"]//tr[2]/td')  # No of columns
total_Columns = len(columns)

rows = driver.find_elements(By.XPATH, '//table[@id="customers"]//tr')   # No of rows
total_Rows = len(rows)


for r in range(2, total_Rows+1):
    for c in range(1, total_Columns):
        value = driver.find_element(By.XPATH, '//table[@id="customers"]//tr[' + str(r) + ']/td[2]').text
        if value == "FlipKart" or value == "Java":
            value1 = driver.find_element(By.XPATH, '//table[@id="customers"]//tr[' + str(r) + ']/td[5]').text
            print(value + ': ' + value1)
            break





driver.close()
driver.quit()

