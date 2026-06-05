from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_hard_assert():
    print("test hard assert method started")
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")
    time.sleep(10)


    assert "OrangeHRM" in driver.title, "Title does not contain 'OrangeHRM'"
    print("title assert executed")
    username= driver.find_element(By.ID, "txtUsername")

    assert username.is_displayed(), "Username field is not displayed"
    print("username assert executed")
    
    dashboard = driver.find_element(By.XPATH, "//div[@id='dashboard']")

    assert dashboard.text == "Dashboard", "Dashboard text does not match expected value"
    print("dashboard assert executed")

test_hard_assert()