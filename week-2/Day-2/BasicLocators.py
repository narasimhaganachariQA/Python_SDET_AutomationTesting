from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
username_filed=driver.find_element(By.ID,"username")
username_filed.send_keys("student")

password_filed=driver.find_element(By.NAME,"password")
password_filed.send_keys("Password")
login_button=driver.find_element(By.CLASS_NAME,"btn")

login_button.click()
time.sleep(5)
actual_text = driver.find_element(By.ID, "error").text
assert "Your password is invalid!" in actual_text, f"Expected 'expected text' but found '{actual_text}'"
print("negative assert is worked ")
time.sleep(5)

driver.quit()