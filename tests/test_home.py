from utils.wait_utils import wait_for_element
from appium.webdriver.common.appiumby import AppiumBy

# Este primer test solo definimos que se abra la APP
def test_open_app(driver):
    element = wait_for_element(driver,(AppiumBy.ACCESSIBILITY_ID,"App"))
    assert element is not None

def test_navigate_to_app(driver):
    # Click en App
    app_options = wait_for_element(driver,(AppiumBy.ACCESSIBILITY_ID,"App"))
    app_options.click()

    #Validar que cargó la siguiente pantalla
    activity= wait_for_element(driver ,(AppiumBy.ACCESSIBILITY_ID,"Activity"))
    assert activity is not None