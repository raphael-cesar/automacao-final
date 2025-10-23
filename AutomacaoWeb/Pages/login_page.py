from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip

# from Pages.email_page import EmailPage
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.EMAIL_XPATH = "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/section/div/div[2]/div/div[2]/div/div/form/div[1]/label/div/input"
        self.ENVIAR_BUTTON_XPATH = "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/section/div/div[2]/div/div[2]/div/div/form/div[3]/div/button/div/span"
        self.CODE_INPUT_XPATH = "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/section/div/div[2]/div/div[2]/div/div/form/div[1]/label/div/input"
        self.key = Keys.ENTER
        
    #Get
    def send_email(self):
        text = pyperclip.paste()
        self.send_keys_to_element(By.XPATH, self.EMAIL_XPATH, text)
        self.send_keys_to_element(By.XPATH, self.EMAIL_XPATH, self.key)
        return text
        
    def send_code(self, text):
        from Pages.menu_page import MenuPage
        self.send_keys_to_element(By.XPATH, self.CODE_INPUT_XPATH, text)
        self.send_keys_to_element(By.XPATH, self.CODE_INPUT_XPATH, self.key)
        return MenuPage(self.driver)
        
    def navigate_email(self):
        from Pages.email_page import EmailPage
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        return EmailPage(self.driver)
        