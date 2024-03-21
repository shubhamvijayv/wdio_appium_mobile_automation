import time
import allure

from base.selenium_driver import BasePage
from PageObjects.locators import *
from Utilities.Readconfigurations import *
from Utilities.return_message import *
from Utilities.constants import *

from appium.webdriver.common.appiumby import AppiumBy


class Swipe(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('swipe method work successfully')
    def swipe_success(self):
        time.sleep(2)
        self.element_click(*SwipeLocators.SWIPE_TEXT)
        time.sleep(2)
        self.scroll(AppiumBy.ANDROID_UIAUTOMATOR, 'down')
        self.scroll(AppiumBy.ANDROID_UIAUTOMATOR, 'up')
        self.switch_app(read_configuration('message_app','message_app_credientials'))
        self.key_code(4)
        self.scroll(AppiumBy.ANDROID_UIAUTOMATOR, 'right')
        self.scroll(AppiumBy.ANDROID_UIAUTOMATOR, 'left')
