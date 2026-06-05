from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
privacy_Polic_link=driver.find_element(By.LINK_TEXT, "Privacy Policy")
link = privacy_Polic_link.get_attribute("href")
print("Privacy Policy:",link)
#time.sleep(15)
#privacy_Polic_link.click
#time.sleep(5)
#driver.back()
time.sleep(5)
list_of_inputs=driver.find_elements(By.TAG_NAME,"input")
print("number of input tages :", len(list_of_inputs))
time.sleep(10)
#username_filed=driver.find_element(By.ID,"username")
username_filed=driver.find_element(By.XPATH, "//*[@name='username']")


username_filed.send_keys("student")


password_filed=driver.find_element(By.NAME,"password")
password_filed.send_keys("Password123")
login_button=driver.find_element(By.CSS_SELECTOR,"[name='btn']")
print("clicked submit")
#assert "Selenium automates browsers" in main_header.text
login_button.click()
time.sleep(5)

driver.quit()
