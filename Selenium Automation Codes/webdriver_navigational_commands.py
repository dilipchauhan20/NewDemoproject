import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.google.com")
print(driver.title)

time.sleep(5)

driver.get("https://www.facebook.com")
print(driver.title)

time.sleep(5)

driver.back()
print(driver.title)

time.sleep(5)

driver.forward()
print(driver.title)

time.sleep(5)

driver.close()
driver.quit()