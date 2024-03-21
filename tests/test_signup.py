import pytest
import allure
from PageObjects.SignupPage import SignUp
from Utilities.Readconfigurations import *
from Utilities.constants import *


@pytest.mark.usefixtures("setup_and_teardown")
class TestSignUp:
    
    @pytest.fixture(autouse=True)
    def classSetup(self, setup_and_teardown):
        self.sign_up = SignUp(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression    
    def test_001(self):
        """signup functionality with correct username and correct password"""
        self.sign_up.signup_success(read_configuration("crediential", "login_username"), read_configuration("crediential", "login_password"), read_configuration("crediential", "login_password"))
        self.sign_up.signup_success_message()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression 
    def test_002(self):
        """signup functionality with correct username and correct password and without confirm password"""
        self.sign_up.signup_success(read_configuration("crediential", "login_username"), read_configuration("crediential", "login_password"), BLANK)
        self.sign_up.signup_failure_message_not_confirm_password()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression 
    def test_003(self):
        """signup functionality with correct username and without password and correct confirm password"""
        self.sign_up.signup_success(read_configuration("crediential", "login_username"), BLANK, read_configuration("crediential", "login_password"))
        self.sign_up.signup_failure_message_not_confirm_password()
        self.sign_up.signup_failure_message_not_password()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression 
    def test_004(self):
        """signup functionality with correct username and correct password and without confirm password"""
        self.sign_up.signup_success(BLANK, read_configuration("crediential", "login_password"), read_configuration("crediential", "login_password"))
        self.sign_up.signup_failure_message_not_email()
