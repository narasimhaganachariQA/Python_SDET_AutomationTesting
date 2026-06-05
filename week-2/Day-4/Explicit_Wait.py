# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Explicit wait imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome browser
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open website
driver.get("https://demoqa.com/dynamic-properties")

# Maximize browser
driver.maximize_window()

# ---------------- EXPLICIT WAIT ----------------
# Wait until button becomes clickable

wait = WebDriverWait(driver, 10)

enable_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "enableAfter")
    )
)

# ---------------- CLICK BUTTON ----------------

enable_button.click()

# ---------------- VALIDATION ----------------

print(" Button became clickable")
print(" Explicit Wait executed successfully")
visible_after=wait.until(EC.presence_of_element_located((By.ID, "visibleAfter")))
print("text : ", visible_after.text)
# Close browser
driver.quit()