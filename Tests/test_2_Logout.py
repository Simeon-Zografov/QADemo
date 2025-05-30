import allure
import pytest
from pytest_check import check
from allure import severity, severity_level
from Pages.LoginPage import Login
from Pages.HomePage import Home
from Common.BaseClass import BaseClass


@pytest.mark.parametrize("driver", BaseClass.browsers, indirect=True)
class TestLogin(BaseClass):

    @severity(severity_level.BLOCKER)
    @allure.feature('Home page')
    @allure.title("User is navigated to the Home page")
    @pytest.mark.dependency(name="test_1")
    def test_1(self, driver):
        login_obj = Login(driver)
        home_obj = Home(driver)
        driver.get(self.url)
        login_obj.complete_loin(BaseClass.username, BaseClass.password)
        with check, allure.step("Check the page title"):
            assert home_obj.get_home_page_title_text() == "Secure Area"

    @severity(severity_level.BLOCKER)
    @allure.feature('Logout')
    @allure.title("User is successfully logged out")
    @pytest.mark.dependency(depends=["test_1"])
    def test_2(self, driver):
        login_obj = Login(driver)
        home_obj = Home(driver)
        home_obj.click_logout_button()
        with check, allure.step("Check the notification"):
            assert login_obj.get_error_message_text() == "You logged out of the secure area!\n×"
        with check, allure.step("Check the page title"):
            assert login_obj.is_login_title_visible()
