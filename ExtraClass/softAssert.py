from selenium import webdriver

def test_google_page():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    
    # 1. Initialize an empty list to store failure logs
    failures = []

    # 2. Check Title (This will fail)
    if driver.title != "Wrong Title":
        failures.append(f"Title mismatch! Got: '{driver.title}'")
    print("first assert")

    # 3. Check URL (This will pass)
    if driver.current_url != "https://google.com/":
        failures.append(f"URL mismatch! Got: '{driver.current_url}'")
    print("second assert")


    # Close the browser safely
    driver.quit()
    print(failures)

    # 4. Final Hard Assert: If list is not empty, fail the test
    assert len(failures) == 0, f"Test failed with the following errors:\n" + "\n".join(failures)

test_google_page()