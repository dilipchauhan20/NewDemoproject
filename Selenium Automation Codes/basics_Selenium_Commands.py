import time

import webdriver_manager.chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome(<Executable Path>)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH, '//a[@href="http://www.selenium.dev"]').click()
time.sleep(3)

print(driver.title) # To get the title of the page
print(driver.current_url)  # To get the current url

time.sleep(10)

driver.close() # For currently selected tab
time.sleep(10)

driver.quit() # For all the tabs