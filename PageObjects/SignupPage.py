import time
import allure

from PageObjects.locators import *
from base.selenium_driver import BasePage
from Utilities.return_message import *
from Utilities.constants import *

class SignUp(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('wdio app signup functionality')
    def signup_success(self, username, password, confirm_password):
        self.element_click(*LoginLocators.LOGIN_BUTTON_TEXT)
        time.sleep(2)
        self.element_click(*SignUpLocators.SIGNUP_BUTTON_TEXT)
        self.send_key(username, *SignUpLocators.USERNAME_AREA)
        self.send_key(password, *SignUpLocators.PASSWORD_AREA)
        self.send_key(confirm_password, *SignUpLocators.CONFIRM_PASSWORD)
        self.element_click(*SignUpLocators.SIGNUP_BUTTON)  
    
    @allure.step('wdio app signup success message')
    def signup_success_message(self):
        time.sleep(2)
        assert self.is_element_displayed(*SignUpLocators.SUCCESS_MESSAGE)

    @allure.step('wdio app signup failure message')
    def signup_failure_message_not_confirm_password(self):
        assert self.is_element_displayed(*SignUpLocators.CONFIRM_PASSWORD_VALIDATION)

    @allure.step('wdio app signup failure message')
    def signup_failure_message_not_password(self):
        assert self.is_element_displayed(*SignUpLocators.PASSWORD_VALIDATION)

    @allure.step('wdio app signup failure message')
    def signup_failure_message_not_email(self):
        assert self.is_element_displayed(*SignUpLocators.USERNAME_VALIDATION)
