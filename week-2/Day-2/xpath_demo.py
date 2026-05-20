from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
try:

    driver= webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(5)
    #==========================================================================================
    #contains() -> Partial attribute matching
    #=====================================================================================
    name_filed=driver.find_element(By.XPATH,"//input[contains(@id,'name')]")
    name_filed.send_keys("nikhil")
    print("contains() xpath executed")
    #==============================================================================================
    #2.starts-with() ->match beginning of attribute
    #==============================================================================================
    email_filed=driver.find_element(By.XPATH,"//input[starts-with(@id,'email')]")
    email_filed.send_keys("test@gmail.com")
    print("executed email with starts with menthod")


    #=====================================================================
    #test() ->Exact test match
    #=========================================================================

    wiki_link=driver.find_element(By.XPATH,"//a[text()='GUI Elements']")
    print("Exact text matched:",wiki_link.text)


    #=====================================================
    #normalize-space()
    #removes unnecessary spaces
    #===========================================================
    header=driver.find_element(By.XPATH,"//h1[normalize-space()='Automation Testing Practice']")

    print("normalize-space() : ",header.text)

    #=========================================================================
    #parent axis
    #move one level upward
    #================================================================
    parent_element=driver.find_element(By.XPATH,"//input[@id='name']/parent::div")
    print("parent axis executed")

    #==============================================================
    # ancestor axis
    #ancestor :: searches all levells upward in the HTML tree structur
    #form : limits the search specifically to <form >
    #scope :selects all parent and grandparent nodes.
    #==============================================================
    ancestor_element=driver.find_element(By.XPATH,"//p[contains(text(),'Section 1')]/ancestor::div[@class='widget-content']")
    print("Ancestor executed")


    #=====================================================================
    #child Axis
    #step down exactly one level 
    #=====================================================================
    child_element=driver.find_element(By.XPATH,"//div[@class='widget-content']/child::ul")
    print("child executed")
    #=====================================================================
    #descendant
    #scopr child,grand child(get all lower levels)
    #=====================================================================
    descendent_filed =driver.find_element(By.XPATH,"//div[@class='widget-content']/descendant::ul")
    print("descendant executed")
    #=====================================================================
    #following siblings axis
    #locate next sibling element
    #=====================================================================
    



except:
    pass