import os
import time
import logging

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
from Utilities.logger import *

class BasePage():
    
    log = LogClass.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, result_message):
        """
        Takes screenshot of the current open web page
        """
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot save to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return AppiumBy.ID
        elif locator_type == "name":
            return AppiumBy.NAME
        elif locator_type == "xpath":
            return AppiumBy.XPATH
        elif locator_type == "css":
            return AppiumBy.CSS_SELECTOR
        elif locator_type == "class":
            return AppiumBy.CLASS_NAME
        elif locator_type == "link":
            return AppiumBy.LINK_TEXT
        elif locator_type == 'accessibility':
            return AppiumBy.ACCESSIBILITY_ID
        else:
            self.log.info("Locator type " + locator_type + " not correct/supported")
            
        return False

    def get_element(self, locator, locator_type="id"):
        """
        Get an element
        """
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " locator_type: " + locator_type)
        except:
            self.log.error("Element not found with locator: " + locator + " locator_type: " + locator_type)
            
        return element

    def get_element_list(self, locator, locator_type="id"):
        """
        Get a list of elements
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator: " + locator + " and locator_type: " + locator_type)
        except:
            self.log.error("Element list not found with locator: " + locator + " and locator_type: " + locator_type)
            
        return element

    def element_click(self, locator="", locator_type="id", element=None):
        """Either provide element or a combination of locator and locator_type"""
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            self.log.error("Cannot click on the element with locator: " + locator + " locator_type: " + locator_type)
            # print_stack()

    def send_key(self, data, locator="", locator_type="id", element=None):
        """
        Send keys to an element - Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            self.log.error("Cannot send data on the element with locator: " + locator + " locator_type: " + locator_type)
            
            # print_stack()

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        """Get 'Text' on an element - Either provide element or a combination of locator and locator_type"""
        try:
            if locator: 
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            # text = None
        return text

    def is_element_present(self, locator="", locator_type="id", element=None):
        """Check if element is present - Either provide element or a combination of locator and locator_type"""
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator: " + locator + " locator_type: " + locator_type)
                return True
            else:
                self.log.error("Element not present with locator: " + locator + " locator_type: " + locator_type)
                
                return False
        except:
            print("Element not found")
            return False

    def is_element_displayed(self, locator="", locator_type="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        is_display = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_display = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator + " locator_type: " + locator_type)
            else:
                self.log.error("Element not displayed with locator: " + locator + " locator_type: " + locator_type)
                
            return is_display
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locator, by_type):
        """
        Check if element is present
        """
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info("Element present with locator: " + locator + " locator_type: " + str(by_type))
                return True
            else:
                self.log.error("Element not present with locator: " + locator + " locator_type: " + str(by_type))
                
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait_for_element(self, locator, locator_type="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element did not appear on the web page")
            
            print_stack()
        return element

    def web_scroll(self, direction="up"):
        """
        Scroll Browser up and down
        """
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")
            
    def clear_element(self, locator="", locator_type="id", element=None):
        """Clear the content of an element - Either provide element or a combination of locator and locatorType"""
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.clear()
            self.log.info("Cleared content of element with locator: " + locator + " locator_type: " + locator_type)
        except:
            self.log.error("Cannot clear content of the element with locator: " + locator + " locator_type: " + locator_type)
               
            print_stack()

    def swipe(self, start_x="", start_y="", end_x="", end_y="", element=None):
        if start_x and start_y and end_x and end_y:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(start_x, start_y).pointer_down().pause(2).move_to_location(end_x, end_y).release()
            actions.perform()
            self.log.info("Swipe performed from ({}, {}) to ({}, {})".format(start_x, start_y, end_x, end_y))
        else:
            self.log.error("Not present coordinates")
        return element

    def switch_app(self, app_credientials):
        self.driver.execute_script('mobile: startActivity', {'intent': app_credientials})
        time.sleep(2)

    def key_code(self, value):
        self.driver.press_keycode(value)

    def scroll(self, by, direction):
        if direction == 'down':
            self.driver.find_element(by, 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')
            self.log.info("scroll down using" + by)

        elif direction == 'up':
            self.driver.find_element(by, 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToBeginning(5)')
            self.log.info("scroll up using" + by)

        elif direction == 'right':
            self.driver.find_element(by, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToEnd(5)')
            self.log.info("scroll right using" + by)

        elif direction == 'left':
            self.driver.find_element(by, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToBeginning(5)') 
            self.log.info("scroll left using " + by)
