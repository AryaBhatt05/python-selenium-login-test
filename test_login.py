from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    # Enter username
    driver.find_element(By.ID, "username").send_keys("tomsmith")

    # Enter password
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # Click login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)  # wait for page to load

    # Verify login success message
    success_message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_message

    driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    # Enter wrong username
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")

    # Click login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    # Verify error message
    error_message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in error_message

    driver.quit()
