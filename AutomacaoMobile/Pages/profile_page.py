from Pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import time

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.LOGIN_EMAIL_XPATH = '//android.view.View[@resource-id="Entrar com e-mail"]'
        self.LOGIN_EMAIL_PASSWORD_XPATH = '//android.widget.Button[@content-desc="Entrar com e-mail e senha"]'
        
    def click_login_email(self):
        self.click_element(AppiumBy.XPATH, self.LOGIN_EMAIL_XPATH)
        
    def click_login_with_password(self):
        from Pages.login_page import LoginPage
        self.click_element(AppiumBy.XPATH, self.LOGIN_EMAIL_PASSWORD_XPATH)
        return LoginPage(self.driver)