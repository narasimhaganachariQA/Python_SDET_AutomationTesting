from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver= webdriver.Chrome()
try:#try/except used for handle unwanted situation to break the code
    driver.maximize_window()
    # driver.get("https://python.org")
    # time.sleep(5)
    # mouse_actions=ActionChains(driver)

    # #mouse hover action
    # #Action 1: Mouse Hover
    # community_menu =driver.find_element(By.LINK_TEXT,"Community")
    # time.sleep(3)
    mouse_actions=ActionChains(driver) #actionchain gives virtual mouse to the open browser window 
    # #and saves into variable mouse-actions

    # mouse_actions.move_to_element(community_menu)
    # time.sleep(5)
    # mouse_actions.perform()
    # time.sleep(10)

    #Action 2:Double click

    # driver.get("https://www.demo.guru99.com/test/simple_context_menu")
    # time.sleep(2)
    # double_click_button=driver.find_element(By.XPATH,"//button[contains(text(),'Double-Click Me')]")
    # print("get click button")
    # mouse_actions.double_click(double_click_button).perform()
    # print("Double click action successful")
    # time.sleep(2)
    # driver.switch_to.alert.accept()
    # print("alert accepted")
    # time.sleep(2)

    # #Action 03: Drag and Drophttps:
    driver.get("https://www.demo.guru99.com/test/drag_drop.html")
    time.sleep(2)
    source_money_block=driver.find_element(By.XPATH,"//*[@id='fourth']/a")
    target_amount_placeholder=driver.find_element(By.XPATH,"//*[@id='amt7']/li")
    mouse_actions=ActionChains(driver)
    mouse_actions.drag_and_drop(source_money_block,target_amount_placeholder).perform()
    time.sleep(5)
    print("Drag and drop performed")

    

except:
    pass
finally:
    driver.quit()