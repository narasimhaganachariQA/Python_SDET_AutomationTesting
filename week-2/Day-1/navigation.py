from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#import time

driver=webdriver.Chrome()
driver.get("https://google.com")
WebDriverWait(driver,10)
#time.sleep(10)
driver.get("https://youtube.com")
#time.sleep(10)
WebDriverWait(driver,10)
driver.back()
#driver.forward()
WebDriverWait(driver,10)
#time.sleep(10)
driver.quit()