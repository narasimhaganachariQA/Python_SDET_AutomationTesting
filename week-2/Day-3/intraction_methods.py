from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver= webdriver.Chrome()
element =driver.find_element(By.XPATH,"")
element.click()
element.send_keys()
element.clear()


#complex Gestures
action=ActionChains(driver)
action.move_to_element(element) #hovers mouse
action.drag_and_drop("","")
action.context_click(element).perform #right-click an item
action.drag_and_drop_by_offset("slider","x","y")

action.move_to_element(element).perform() #hover over a dropdown
action.perform() #execute the chain


#Element level


