import time
import allure

from PageObjects.locators import *
from base.selenium_driver import BasePage
from Utilities.return_message import *
from Utilities.constants import *


class DragAndDrop(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('successfully drag and drop all elements')
    def drag_success(self):
        self.element_click(*DragAndDropLocators.DRAG_AND_DROP_TEXT)
        time.sleep(3)
        self.swipe(944, 1909, 763, 806)
        self.swipe(784, 1883, 556, 1038)
        self.swipe(638, 1905, 543, 577)
        self.swipe(448, 1917, 758, 590)
        self.swipe(276, 1900, 745, 1034)
        self.swipe(188, 1892, 327, 801)
        self.swipe(375, 2090, 539, 789)
        self.swipe(513, 2081, 310, 616)
        self.swipe(700, 2068, 332, 1051)
        assert self.is_element_displayed(*DragAndDropLocators.IMAGE_DISPLAY)
