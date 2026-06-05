from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest_check as check
#import time

def soft_assert_test():
    print("soft_assert_test execution stated")
    driver=webdriver.Chrome()
    driver.get("https://www.google.com")
    check.is_true("test" in driver.title,"Title invalid")
    print("first soft assert executed")
    # check.is_true(driver.find_element(By.NAME,"test").is_displayed(), "locator not found")
    # print("second soft assert executed")

    #driver.get("https://www.youtube.com")
    check.is_true("test" in driver.title,"Title invalid")
    print("second soft assert executed")

    driver.quit()

#soft_assert_test()


    

