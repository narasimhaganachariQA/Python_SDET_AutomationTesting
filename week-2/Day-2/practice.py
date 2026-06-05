from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Explicit wait imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
#time.sleep(5)
driver.maximize_window()
time.sleep(5)
wait = WebDriverWait(driver, 10)
#username_filed=driver.find_element(By.ID,"username")
username=wait.until(
    EC.presence_of_element_located(
        (By.ID, "username")
    )
)

username.send_keys("student")
time.sleep(5)

password_filed= wait.until(
    EC.presence_of_element_located(
        (By.ID, "password")
    )
)#driver.find_element(By.ID,"password")
password_filed.send_keys("Password123")

login_butn=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"btn")))

print("login button avaliable ")

login_butn.click()
print("login button clicked ")
expectedValue=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"post-title")))
assert "Logged In Successfully" in expectedValue.text
time.sleep(5)
driver.get("https://practicetestautomation.com/practice-test-login/")
username=wait.until(
    EC.presence_of_element_located(
        (By.ID, "username")
    )
)

username.send_keys("student")
time.sleep(5)

password_filed= wait.until(
    EC.presence_of_element_located(
        (By.ID, "password")
    )
)#driver.find_element(By.ID,"password")
password_filed.send_keys("Password")

login_butn=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"btn")))

print("login button avaliable ")
login_butn.click()
invalid_login=wait.until(EC.presence_of_element_located((By.ID,"error")))
print(invalid_login.text)
assert "Your password is invalid!" in invalid_login.text

driver.quit()
