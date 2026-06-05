from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Explicit wait imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")
#time.sleep(5)
driver.maximize_window()
time.sleep(5)
wait = WebDriverWait(driver, 10)

rows=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr/following-sibling::tr")
print("rows : ", len(rows))

for row in rows:
    #print(row.text)
    print(driver.find_element(By.XPATH,"//td[text()='Alfreds Futterkiste']/following-sibling::td[2]").text)
    break

