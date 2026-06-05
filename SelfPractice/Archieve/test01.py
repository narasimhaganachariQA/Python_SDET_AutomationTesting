from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Explicit wait imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()
driver.get("https://www.flipkart.com/")
#time.sleep(5)
driver.maximize_window()
time.sleep(5)
#login_pop_close_btn= driver.find_element(By.XPATH,"//span[@class='b3wTlE' and @role='button']")
#login_pop_close_btn.click
driver.find_element(By.XPATH,"//span[contains(text(),'✕')]").click()
print("element clicked")
time.sleep(10)