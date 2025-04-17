import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://your-bank-login-page.com")
    yield driver
    driver.quit()

def test_valid_login(driver):
    login = LoginPage(driver)
    login.enter_username("validUser")
    login.enter_password("validPass123")
    login.click_login()
    time.sleep(2)
    assert "dashboard" in driver.current_url.lower()

def test_invalid_username(driver):
    login = LoginPage(driver)
    login.enter_username("invalidUser")
    login.enter_password("validPass123")
    login.click_login()
    assert "Invalid username" in login.get_error_message()

def test_account_lock_after_three_failures(driver):
    login = LoginPage(driver)
    for _ in range(3):
        login.enter_username("validUser")
        login.enter_password("wrongPass")
        login.click_login()
        time.sleep(1)
    assert "account locked" in login.get_error_message().lower()
