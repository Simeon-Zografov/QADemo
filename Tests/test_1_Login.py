import allure
import pytest
from pytest_check import check
from allure import severity, severity_level
from Pages.LoginPage import Login
from Common.BaseClass import BaseClass


@pytest.mark.parametrize("driver", BaseClass.browsers, indirect=True)
class TestLogin(BaseClass):

    @severity(severity_level.BLOCKER)
    @allure.feature('Login')
    @allure.title("User is navigated to the Login page")
    @pytest.mark.dependency(name="test_1")
    def test_1(self, driver):
        login_obj = Login(driver)
        driver.get(self.url)
        print(BaseClass.cur_env)
        with check, allure.step("Check the page title"):
            assert login_obj.is_login_title_visible()

    @severity(severity_level.NORMAL)
    @allure.feature('Login')
    @allure.title("Unsuccessfully login with username: {username} and password: {password}")
    @pytest.mark.dependency(depends=["test_1"])
    @pytest.mark.parametrize('username,password,error', [
        (BaseClass.username[:-1], BaseClass.password, "Your username is invalid!"),
        (BaseClass.username, BaseClass.password[:-1], "Your password is invalid!"),
        ("", BaseClass.password, "Your username is invalid!"),
        (BaseClass.username, "", "Your password is invalid!")
    ])
    def test_2(self, driver, username, password, error):
        login_obj = Login(driver)
        driver.refresh()
        login_obj.set_username_field(username)
        login_obj.set_password_field(password)
        login_obj.click_login_button()
        with check, allure.step("Check for error message"):
            assert login_obj.is_error_message_visible()
        with check, allure.step("Check error message text"):
            assert login_obj.get_error_message_text() == error + "\n×"

    @severity(severity_level.CRITICAL)
    @allure.feature('Login')
    @allure.title("Successful login")
    @pytest.mark.dependency(depends=["test_1"])
    def test_3(self, driver):
        login_obj = Login(driver)
        driver.refresh()
        login_obj.set_username_field(BaseClass.username)
        login_obj.set_password_field(BaseClass.password)
        login_obj.click_login_button()
        with check, allure.step("The user is logged in"):
            assert login_obj.get_error_message_text() == "You logged into a secure area!\n×"


