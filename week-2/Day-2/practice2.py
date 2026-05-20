from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
#username_filed=driver.find_element(By.ID,"username")
username_filed=driver.find_element(By.ID, "user-name")
username_filed.send_keys("standard_user")
password_filed=driver.find_element(By.NAME,"password")
password_filed.send_keys("secret_sauce")
login_button=driver.find_element(By.ID, "login-button")
time.sleep(3)
login_button.click()
print("clicked submit")
time.sleep(3)

linkedin=driver.find_element(By.LINK_TEXT,"LinkedIn")

print(linkedin.get_attribute("href"))
linkedin1=driver.find_element(By.PARTIAL_LINK_TEXT,"In")

print(linkedin1.text)