from Pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators