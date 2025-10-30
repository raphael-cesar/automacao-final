from Pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.EMAIL_FIELD_XPATH = '//android.widget.EditText[@resource-id="E-mail"]'
        self.PASSWORD_FIELD_XPATH = '//android.widget.EditText[@resource-id="Senha"]'
        self.LOGIN_BUTTON_XPATH = '//android.view.View[@resource-id="Entrar"]'
        self.PASSWORD_ERROR_XPATH = '(//android.view.View[@content-desc="Usuário ou senha inválidos."])[2]'
        
    # Senders    
    def send_email(self, data):
        self.click_element(AppiumBy.XPATH, self.EMAIL_FIELD_XPATH)
        return self.send_keys_to_element(AppiumBy.XPATH, self.EMAIL_FIELD_XPATH, data)
        
    def send_password(self, data):
        self.click_element(AppiumBy.XPATH, self.PASSWORD_FIELD_XPATH)
        self.send_keys_to_element(AppiumBy.XPATH, self.PASSWORD_FIELD_XPATH, data)
        time.sleep(0.5)
     
    # Buttons & Clicks
    def login_button(self):
        from Pages.home_page import HomePage
        self.click_element(AppiumBy.XPATH, self.LOGIN_BUTTON_XPATH)
        return HomePage(self.driver)
    
    # Validation
    def validate_password_error_is_shown(self):
        return self.is_element_displayed(AppiumBy.XPATH, self.PASSWORD_ERROR_XPATH)