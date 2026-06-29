from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import sys
import time

def run_test():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=opts)
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        page = driver.page_source
        if "Logged In Successfully" in page or "Logged In Successfully" in driver.title:
            print("TEST PASSED")
            return 0
        else:
            print("TEST FAILED")
            return 1
    except (NoSuchElementException, WebDriverException) as e:
        print("TEST ERROR:", e)
        return 2
    finally:
        driver.quit()

if __name__ == "__main__":
    sys.exit(run_test())
