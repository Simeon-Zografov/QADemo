from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.login_page_title = (By.XPATH, "//h2")
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.XPATH, "//button")
        self.error_message = (By.ID, "flash")

    def is_login_title_visible(self):
        return self.driver.find_element(*self.login_page_title).is_displayed()

    def set_username_field(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def set_password_field(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def is_error_message_visible(self):
        return self.driver.find_element(*self.error_message).is_displayed()

    def get_error_message_text(self):
        return self.driver.find_element(*self.error_message).text.strip()

    def complete_loin(self, username, password):
        self.set_username_field(username)
        self.set_password_field(password)
        self.click_login_button()
