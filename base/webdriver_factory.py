from appium import webdriver
from appium.options.common.base import AppiumOptions
from Utilities.Readconfigurations import *


class WebDriverFactory:
    def __init__(self, device, device_name):
        self.device = device
        self.device_name = device_name

    def get_webdriver_wait(self):
        try:
            options = AppiumOptions()
            if self.device == "android":
                self.set_android_capabilities(options)
            else:
                self.set_ios_capabilities(options)

            url = read_configuration("Url", "base_url")
            driver = webdriver.Remote(url, options=options)
            return driver
        except Exception as e:
            print(f"Error occurred while initializing WebDriver: {str(e)}")
            return None

    def set_android_capabilities(self, options):
        if self.device_name:
            options.load_capabilities({
                "platformName": "Android",
                "appium:platformVersion": "13.0",
                "appium:deviceName": self.device_name,
                "appium:App": "/Android-NativeDemoApp-0.4.0.apk",
                "appium:appPackage": "com.wdiodemoapp",
                "appium:appActivity": "com.wdiodemoapp.MainActivity",
                "appium:automationName": "UIAutomator2",
                "appium:ensureWebviewsHavePages": True,
                "appium:nativeWebScreenshot": True,
                "appium:newCommandTimeout": 3600,
                "appium:connectHardwareKeyboard": True
            })

    def set_ios_capabilities(self, options):
        if self.device_name:
            options.load_capabilities({
                'platformVersion': '12.4',
                'platformName': 'iOS',
                'deviceName': self.device_name,
                'automationName': 'XCUITest',
                'bundleId': 'com.example.apple-samplecode.UICatalog'
            })
