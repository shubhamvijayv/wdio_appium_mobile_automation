import time
import allure

from PageObjects.locators import *
from base.selenium_driver import BasePage
from Utilities.return_message import *
from Utilities.constants import *

class Login(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('wdio app login functionality')
    def app_login_success(self, username, password):
        self.element_click(*LoginLocators.LOGIN_BUTTON_TEXT)
        time.sleep(2)
        self.element_click(*LoginLocators.USERNAME_AREA)
        self.send_key(username, *LoginLocators.USERNAME_AREA)
        self.send_key(password, *LoginLocators.PASSWORD_AREA)
        self.key_code(66)
        self.key_code(66)
        time.sleep(2)
        assert self.is_element_displayed(*LoginLocators.SUCCESS_MESSAGE)
        
    @allure.step('wdio app login functionality')
    def app_login_failure(self, username, password):
        self.element_click(*LoginLocators.LOGIN_BUTTON_TEXT)
        time.sleep(2)
        if username:
            self.send_key(username, *LoginLocators.USERNAME_AREA)
            self.element_click(*LoginLocators.LOGIN_BUTTON)
            assert self.is_element_displayed(*LoginLocators.PASSWORD_VALIDATION)
        if password:
            self.send_key(password, *LoginLocators.PASSWORD_AREA)
            self.element_click(*LoginLocators.LOGIN_BUTTON)
            assert self.is_element_displayed(*LoginLocators.USERNAME_VALIDATION)
        if username == BLANK and password == BLANK:
            self.element_click(*LoginLocators.LOGIN_BUTTON)
            assert self.is_element_displayed(*LoginLocators.PASSWORD_VALIDATION)
            assert self.is_element_displayed(*LoginLocators.USERNAME_VALIDATION)
