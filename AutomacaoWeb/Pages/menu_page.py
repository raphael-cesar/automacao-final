from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from Pages.email_page import EmailPage

class MenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.URL_AME = "https://www.americanas.com.br/"
        #self.URL_EMAIL = 
        self.QUIT_BANNER_ID = "close-button-1454703513200"
        self.MENU_BANNER_ID = "close-button-1454703513200"
        self.LOGIN_BUTTON_CLASS = "ButtonLogin_Container__sgzuk"
        self.EMAIL_HEADER_XPATH = "/html/body/div[1]/header/div/section[1]/div/a[2]/div[2]"

        
    def navigate(self):
        return self.driver.get(self.URL_AME)
    
    def navigate_email(self):
        self.driver.execute_script("window.open('https://temp-mail.io/');")
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        return EmailPage(self.driver)
    
    #Getters
    def get_actual_url(self):
        return self.driver.current_url
    
    def get_header_email(self):
        return (self.get_element_text(By.XPATH, self.EMAIL_HEADER_XPATH)).replace("olá, ", "").replace("minha conta", "").strip()
    
    #Actions
    def check_popup(self):
        return self.is_element_displayed(By.ID, self.MENU_BANNER_ID)
    
    def click_quit_popup(self):
        return self.click_element(By.ID, self.QUIT_BANNER_ID)
    
    def click_login(self):
        return self.click_element(By.CLASS_NAME, self.LOGIN_BUTTON_CLASS)
    
    def click_header_email(self):
        from Pages.profile_page import ProfilePage
        self.click_element(By.XPATH, self.EMAIL_HEADER_XPATH)
        return ProfilePage(self.driver)
    
    
    
    #Validations
    def validate_menu_is_shown(self):
        return self.get_actual_url() == self.URL_AME
    
    def validate_email_is_shown_and_expected(self, email):
        return self.get_header_email() == email