from selenium import webdriver

class BrowserUtils:

    @staticmethod  #Decorator
    def get_driver():
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver  # returns control to the tests