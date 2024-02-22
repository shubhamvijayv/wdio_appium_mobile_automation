import pytest
import allure
from PageObjects.LoginPage import Login
from Utilities.Readconfigurations import *
from Utilities.constants import *


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    
    @pytest.fixture(autouse=True)
    def classSetup(self, setup_and_teardown):
        self.login = Login(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression    
    def test_001(self):
        """login functionality with correct username and correct password"""
        self.login.app_login_success(read_configuration("crediential", "login_username"), read_configuration("crediential", "login_password"))
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity    
    def test_002(self):
        """login functionality with correct username and without password"""
        self.login.app_login_failure(read_configuration("crediential", "login_username"), BLANK)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity    
    def test_003(self):
        """login functionality with without username and with correct password"""
        self.login.app_login_failure(BLANK, read_configuration("crediential", "login_password"))

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity    
    def test_004(self):
        """login functionality with without username and without password"""
        self.login.app_login_failure(BLANK, BLANK)
