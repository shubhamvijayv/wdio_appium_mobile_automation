import time
import pytest
import allure

from appium.webdriver.appium_service import AppiumService
from allure_commons.types import AttachmentType
from base.webdriver_factory import WebDriverFactory

from Utilities.logger import LogClass
from Utilities.Readconfigurations import *   


def pytest_addoption(parser):
    parser.addoption("--device", action="store", default="default device")
    parser.addoption("--device_name", action="store", default="default device_name")


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    appium_service = AppiumService()
    appium_service.start()
    
    device = request.config.getoption("--device")
    device_name = request.config.getoption("--device_name")
    webdriver_data = WebDriverFactory(device, device_name)
    driver = webdriver_data.get_webdriver_wait()
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.log = LogClass(driver)
    yield driver
    driver.quit()
    appium_service.stop()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()
    if result.failed:
        allure.attach(item.cls.driver.get_screenshot_as_png(), name='screenshot' + time.strftime('_%Y_%m_%d_%H_%M_%S'), attachment_type=AttachmentType.PNG)
