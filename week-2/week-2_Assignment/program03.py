from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    
    driver.get("https://the-internet.herokuapp.com/windows")
    original_window = driver.current_window_handle

    
    driver.find_element(By.LINK_TEXT, "Click Here").click()

    
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

   
    driver.execute_script("alert('Hello!');")
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    
    driver.close()
    driver.switch_to.window(original_window)
finally:
    driver.quit()