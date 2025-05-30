from selenium.webdriver.common.by import By


class Home:

    def __init__(self, driver):
        self.driver = driver
        self.home_page_title = (By.XPATH, "//h2")
        self.logout_button = (By.XPATH, "//a[@class='button secondary radius']")

    def is_home_page_title_visible(self):
        return self.driver.find_element(*self.home_page_title).is_displayed()

    def get_home_page_title_text(self):
        return self.driver.find_element(*self.home_page_title).text

    def click_logout_button(self):
        self.driver.find_element(*self.logout_button).click()

