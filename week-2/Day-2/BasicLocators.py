from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
username_filed=driver.find_element(By.ID,"username")
username_filed.send_keys("student")

password_filed=driver.find_element(By.NAME,"password")
password_filed.send_keys("Password123")
login_button=driver.find_element(By.CLASS_NAME,"btn")

login_button.click()
time.sleep(5)

driver.quit()