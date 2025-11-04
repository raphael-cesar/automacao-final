from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.AUTH_XPATH = "/html/body/div[2]/div/div[1]/div/div[3]/div/div/div/div/aside/nav/div[1]/div[5]/a"
        self.SET_PASSWORD_CLASS = "vtex-button__label"
        self.CODE_INPUT_CLASS = "vtex-styleguide-9-x-input"
        self.PASSWORD_INPUT_XPATH = "/html/body/div[2]/div/div[1]/div/div[3]/div/div/div/div/div/div[3]/section/main/div/div/section/div/div[4]/label/div/input"
        self.SAVE_PASSWORD_BUTTON_XPATH = "/html/body/div[2]/div/div[1]/div/div[3]/div/div/div/div/div/div[3]/section/main/div/div/section/footer/div/button"
        self.PASSWORD_MASK_CLASS = "vtex-my-authentication-1-x-maskedPassword_content"
        self.PASSWORD_MASK_COMMA_CLASS = ".vtex-my-authentication-1-x-maskedPassword_content"
                
    #Getters
    def get_comma(self):
        return self.get_element_text(By.CSS_SELECTOR, self.PASSWORD_MASK_COMMA_CLASS)
        
    #Actions
    def click_auth(self):
        return self.click_element(By.XPATH, self.AUTH_XPATH)

    def click_set_password(self):
        return self.click_element(By.CLASS_NAME, self.SET_PASSWORD_CLASS)
    
    def navigate_email(self):
        from Pages.email_page import EmailPage
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        return EmailPage(self.driver)
    
    def send_code(self, text):
        return self.send_keys_to_element(By.CLASS_NAME, self.CODE_INPUT_CLASS, text)
    
    def send_password(self, data):
        return self.send_keys_to_element(By.XPATH, self.PASSWORD_INPUT_XPATH, data)
    
    def clear_password_field(self):
        for _ in range(10):
            self.send_keys_to_element(By.XPATH, self.PASSWORD_INPUT_XPATH, Keys.BACKSPACE)
            
    def click_save_password(self):
        return self.click_element(By.XPATH, self.SAVE_PASSWORD_BUTTON_XPATH)
    
    
    #Validations
    def validate_save_password_button(self):
        return self.is_element_enabled(By.XPATH, self.SAVE_PASSWORD_BUTTON_XPATH)
    
    def validate_mask_password_is_shown_and_expected(self):
        return self.is_element_displayed(By.CLASS_NAME, self.PASSWORD_MASK_CLASS)
    
    def validate_comma_is_shown(self):
        return "*" in self.get_comma()