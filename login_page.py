from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, 'username')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'loginBtn')
        self.error_message = (By.CLASS_NAME, 'error-msg')

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
