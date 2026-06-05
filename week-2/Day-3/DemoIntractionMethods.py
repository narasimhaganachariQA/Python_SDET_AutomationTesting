from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
try:#try/except used for handle unwanted situation to break the code

    driver= webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://python.org")
    time.sleep(5)
    search_filed=driver.find_element(By.NAME,"q")
    #search_filed=driver.find_element(By.ID,"id-search-field")
    search_filed.clear()
    search_filed.send_keys("documentation") #simulate to send value into webelement
    go_button=driver.find_element(By.ID,"submit")
    go_button.click()#click is standard method, click is perform  left click 
    time.sleep(3)
    print("search executed successfully")


except:
    pass

finally:
    driver.quit()