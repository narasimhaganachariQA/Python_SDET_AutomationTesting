from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver= webdriver.Chrome()
try:#try/except used for handle unwanted situation to break the code
    driver.maximize_window()
    driver.get("https://automationexercise.com/#google_vignette")
    addcartiteam=driver.find_element(By.XPATH,"//p[text()='Men Tshirt']")
    time.sleep(5)
except:
    pass
finally:
    driver.close()