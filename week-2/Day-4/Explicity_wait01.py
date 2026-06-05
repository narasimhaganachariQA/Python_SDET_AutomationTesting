# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Explicit wait imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome browser
driver = webdriver.Chrome()

# ---------------- IMPLICIT WAIT ----------------
# Selenium will wait up to 10 seconds
# before throwing an exception

#driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")

# Maximize browser
driver.maximize_window()

# ---------------- LOGIN ----------------

username=wait.until(
    EC.presence_of_element_located(
        (By.ID, "user-name")
    )
)

username.send_keys("standard_user")
time.sleep(5)

#username=wait.until(EC.visibility_of((driver.find_element(By.ID, "user-name")))#.send_keys("standard_user")

pw=wait.until(
    EC.presence_of_element_located(
        (By.ID, "password")
    )
)
pw.send_keys("secret_sauce")
#driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(5)

login_btn=wait.until(EC.presence_of_element_located((By.ID,"login-button"))) #  driver.find_element(By.ID, "login-button").click()
login_btn.click()


add_to_cart01=wait.until(EC.presence_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
add_to_cart01.click()

add_to_cart02=wait.until(EC.presence_of_element_located((By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")))
add_to_cart02.click()


# cart_icon=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"shopping-cart-badge")))
# time.sleep(2)
cart_btn=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"shopping_cart_link")))
cart_btn.click()
time.sleep(5)
check_out_btn=wait.until(EC.presence_of_element_located((By.ID,"checkout")))

wait.until(EC.presence_of_element_located((By.ID,"first-name"))).send_keys("test")
#firstName.send_keys("test")
wait.until(EC.presence_of_element_located((By.ID,"last-name"))).send_keys("QA")
wait.until(EC.presence_of_element_located((By.ID,"postal-code"))).send_keys("12345")
time.sleep(5)
wait.until(EC.presence_of_element_located((By.ID,"postal-code"))).send_keys("continue")


# if int(cart_icon.text)>=1:
#     time.sleep(5)
#     #cart_btn=driver.find_element((By.CLASS_NAME,"shopping_cart_link"))
#     cart_btn=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"shopping_cart_link")))
#     time.sleep(2)
#     cart_btn.click()
#     print("card clicked")

#     time.sleep(5)
# else:
#     print("items not added")
#     driver.quit()






# ---------------- VALIDATION ----------------

# Get page title after login
# title = driver.title


# print("Page Title is:", title)

# # Check login success
# if "Swag Labs" in title:
#     print(" Login Successful")
# else:
#     print(" Login Failed")

# # Wait to see result
# time.sleep(8)

# # Close browser
# driver.quit()