from appium import webdriver
from appium.options.android import UiAutomator2Options

def create_driver():
    options = UiAutomator2Options()
    options.platform_name= 'Android'
    options.device_name= 'Android Emulator'
    options.app= r"D:\Projects_GIT\Automation\appium-mobile-automation\apps\ApiDemos.apk"
    options.automation_name='UiAutomator2'

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    return driver