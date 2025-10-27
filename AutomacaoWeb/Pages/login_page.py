from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# from Pages.email_page import EmailPage
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.EMAIL_INPUT_XPATH = "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/section/div/div[2]/div/div[2]/div/div/form/div[1]/label/div/input"
        self.SEND_EMAIL_BUTTON_CLASS = "t-small"
        self.SEND_CODE_BUTTON_XPATH = "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/section/div/div[2]/div/div[2]/div/div/form/div[2]/div[2]/button"
        self.CODE_INPUT_XPATH = "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/section/div/div[2]/div/div[2]/div/div/form/div[1]/label/div/input"
        self.EMAIL_PASSWORD_LOGIN_XPATH = "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/section/div/div[2]/div/div[1]/div[1]/ul/li[1]/div/button"
        self.PASSWORD_INPUT_XPATH = "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/section/div/div[2]/div/div[2]/div/div/form/div[2]/div/label/div/input"
        self.LOGIN_BUTTON_CSS = ".vtex-login-2-x-formFooter"
        
    #Get
    def send_email(self, text):
        self.send_keys_to_element(By.XPATH, self.EMAIL_INPUT_XPATH, text)
        
    def send_code(self, text):
        self.send_keys_to_element(By.XPATH, self.CODE_INPUT_XPATH, text)
        
    def send_password(self, text):
        self.send_keys_to_element(By.XPATH, self.PASSWORD_INPUT_XPATH, text)
        
    def navigate_email(self):
        from Pages.email_page import EmailPage
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        return EmailPage(self.driver)
        
    def button_login_code(self):
        self.click_command(By.CLASS_NAME, self.SEND_EMAIL_BUTTON_CLASS)
        
    def button_login_password(self):
        from Pages.menu_page import MenuPage
        self.click_element(By.CSS_SELECTOR, self.LOGIN_BUTTON_CSS)
        return MenuPage(self.driver)
        
    def click_send_code(self):
        from Pages.menu_page import MenuPage
        self.click_element(By.XPATH, self.SEND_CODE_BUTTON_XPATH)
        return MenuPage(self.driver)
    
    def click_login_email_password(self):
        self.click_command(By.XPATH, self.EMAIL_PASSWORD_LOGIN_XPATH)
    
    