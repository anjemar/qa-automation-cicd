from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def run_test(username, password, expected_text, check_element=None):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")          # run without GUI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)  # GitHub runner finds chromedriver automatically
    driver.get("https://practicetestautomation.com/practice-test-login/")

    if username:
        driver.find_element(By.ID, "username").send_keys(username)
    if password:
        driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    result = ""
    try:
        if check_element:
            result = driver.find_element(By.ID, check_element).text
        else:
            result = driver.page_source
    except:
        result = driver.page_source

    if expected_text in result:
        print(f"TEST PASSED: {username}/{password}")
    else:
        print(f"TEST FAILED: {username}/{password}")

    driver.quit()

if __name__ == "__main__":
    run_test("student", "Password123", "Logged In Successfully")
    run_test("wronguser", "wrongpass", "Your username is invalid!", check_element="error")
    run_test("", "", "Please enter username and password", check_element="error")
