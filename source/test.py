from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Test Case 1: Valid password
def test_case_1():
    driver.get("http://localhost")  # Replace with the actual file path
    WebDriverWait(driver, 10).until(EC.title_is("Login"))

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("P@ssw0rd12345")
    driver.find_element(By.NAME, "submit").click()

    WebDriverWait(driver, 10).until(EC.title_is("Home"))
    if driver.title == "Home":
        print("Test Case 1: Passed")
    else:
        print("Test Case 1: Failed")

# Test Case 2: Invalid password
def test_case_2():
    driver.get("http://localhost")  # Replace with the actual file path
    WebDriverWait(driver, 10).until(EC.title_is("Login"))

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("12345")
    driver.find_element(By.NAME, "submit").click()

    WebDriverWait(driver, 10).until(EC.title_is("Login"))
    if driver.title == "Login":
        print("Test Case 2: Passed")
    else:
        print("Test Case 2: Failed")

# Execute the test cases
test_case_1()
test_case_2()

# Close the browser
driver.quit()
