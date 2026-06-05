from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    wait =WebDriverWait(driver,10)
    print("---Started form validation test")

    #Create a reliable wait engine(waits up to 10 seconds)
    #--------------------------------------------------------------------
    #Test 1: Validate the "Validate the "Disabled Input " filed
    #--------------------------------------------------------------------
    #locate the disabled text field using its name attribute
    disabled_field=wait.until(EC.presence_of_element_located((By.NAME,"my-disabled")))
    assert disabled_field.is_displayed()==True,"Error: Disable"

    #--------------------------------------------------------------------
    #Test 
    #--------------------------------------------------------------------
    assert disabled_field.is_enabled()==True
    assert disabled_field.get_attribute("disabled")=='true'
    #--------------------------------------------------------------------
    #Test 
    #--------------------------------------------------------------------
    #--------------------------------------------------------------------
    #Test 
    #--------------------------------------------------------------------
    #--------------------------------------------------------------------
    #Test 
    #--------------------------------------------------------------------
    #--------------------------------------------------------------------
    #Test 
    #--------------------------------------------------------------------
    #--------------------------------------------------------------------
    #Test 
    #--------------------------------------------------------------------
    #--------------------------------------------------------------------
    #Test 
    #--------------------------------------------------------------------
    #--------------------------------------------------------------------
    #Test 
    #--------------------------------------------------------------------



except:
    pass
finally:
    pass