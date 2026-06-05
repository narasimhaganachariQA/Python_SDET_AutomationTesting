from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()

try:
    driver.get("https://selenium.dev")
    time.sleep(4)
    main_header =driver.find_element(By.TAG_NAME,"h1")

    assert "Selenium automates browsers" in main_header.text
    print("Text validation passed")

    assert main_header.is_displayed()==True
    print("Test validation headline found,header is vissible on screen ")

    # assert main_header.get_attribute("class")=="h1"
    # print("attribute validated pass")
    # time.sleep(10)

    button_search=driver.find_element(By.XPATH,"//button[@aria-label='Search']")
    assert button_search.is_enabled()==True
    print("search button is avaliable")

except AssertionError:
    print("one of the validation failed")

except Exception as e :
    print(f"An error occured(e.g.., Element not found :{e} )" )

finally:
    driver.quit()