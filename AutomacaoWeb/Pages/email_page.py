from Pages.base_page import BasePage
from Pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class EmailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.URL_AME = "https://www.americanas.com.br/"
        self.EMAIL_XPATH = "//*[@id='__nuxt']/div[1]/main/div[2]/div/div/div"
        self.REFRESH_XPATH = "//*[@id='__nuxt']/div[1]/main/div[6]/aside/div/div[1]/div/div[1]/button"
        self.CODE_TEXT_XPATH = "/html/body/div[1]/main/div[6]/aside/div/div[2]/div/ul/li/div[2]/span[1]"
        self.CODE_2_TEXT_PATH = "/html/body/div[1]/main/div[6]/aside/div/div[2]/div/ul/li[1]/div[2]/span[1]"
    #Get
    def get_email(self):
        self.click_element(By.XPATH, self.EMAIL_XPATH)
        
    def get_code(self):
        return (self.get_element_text(By.XPATH, self.CODE_TEXT_XPATH)).replace("Seu código de acesso é ", "").strip()
    
    def click_refresh(self):
        return self.click_element(By.XPATH, self.REFRESH_XPATH)
        
    #Actions
    def navigate_ame(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        return LoginPage(self.driver)
    
    def navigate_profile(self):
        from Pages.profile_page import ProfilePage
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        return ProfilePage(self.driver)