from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
try:#try/except used for handle unwanted situation to break the code

    driver= webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://python.org")
    time.sleep(5)
    community_menu =driver.find_element(By.LINK_TEXT,"Community")
    time.sleep(3)
    #Dependency Injection (The Concept)Passing the driver instance into the ActionChains constructor
    #  is called Dependency Injection. 

    mouse_actions=ActionChains(driver) #actionchain gives virtual mouse to the open browser window 
    #and saves into variable mouse-actions

    mouse_actions.move_to_element(community_menu)
    time.sleep(5)
    mouse_actions.perform()
    time.sleep(10)
    #mouse_actions.click()
    #time.sleep(5)
    #print(driver.title())
    print(" Hover action executed successfully")


except:
    pass

finally:
    driver.quit()