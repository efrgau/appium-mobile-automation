from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

def create_driver():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    APP_PATH = os.path.join(BASE_DIR, 'apps','ApiDemos-debug.apk')
    options = UiAutomator2Options()
    options.platform_name= 'Android'
    options.device_name= 'Android Emulator'
    options.app= APP_PATH
    options.automation_name='UiAutomator2'

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    return driver