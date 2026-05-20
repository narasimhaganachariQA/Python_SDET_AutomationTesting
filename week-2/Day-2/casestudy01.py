from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
try:

    driver= webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    driver.maximize_window()
    time.sleep(2)
    username_filed=driver.find_element(By.XPATH, "//input[@name='username']")
    username_filed.send_keys("standard_user")
    password_filed=driver.find_element(By.XPATH,"//input[@type='password']")
    password_filed.send_keys("secret_sauce")
    login_button=driver.find_element(By.XPATH,"//*[@type='submit']")
    print("login successfull ")
    assert "OrangeHRM" in driver.title
except:
    print("issue in script")
    driver.quit()