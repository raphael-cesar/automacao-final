from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from logger import log

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
        self.SEARCH_BAR_ID = "search-input"
        self.MAG_BUTTON_XPATH = "/html/body/div[1]/header/div/section[1]/div/div[1]/div/form/button"
     
    def navigate(self):
        log.info("Open Americanas website")
        return self.driver.get(self.URL_AME)
    
    def navigate_email(self):
        self.driver.execute_script("window.open('https://temp-mail.io/');")
        log.info("Open Temp-Mail website")
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        from Pages.email_page import EmailPage
        return EmailPage(self.driver)
    
    #Getters
    def get_actual_url(self):
        return self.driver.current_url
    
    def get_header_email(self):
        return (self.get_element_text(By.XPATH, self.EMAIL_HEADER_XPATH)).replace("olá, ", "").replace("minha conta", "").strip()
    
    #Senders
    def search_product(self, text):
        log.info(f"Search: {text}")
        self.send_keys_to_element(By.ID, self.SEARCH_BAR_ID, text)
    
    #Buttons & Clicks 
    def check_popup(self):
        log.info("Check Sales banner is displayed")
        return self.is_element_displayed(By.ID, self.MENU_BANNER_ID)
    
    def click_quit_popup(self):
        log.info("Close Sales banner popup")
        self.click_element(By.ID, self.QUIT_BANNER_ID)
    
    def click_login(self):
        log.info("Click login button")
        self.click_element(By.CLASS_NAME, self.LOGIN_BUTTON_CLASS)
    
    def click_header_email(self):
        from Pages.profile_page import ProfilePage
        log.info("Go to profile")
        self.click_element(By.XPATH, self.EMAIL_HEADER_XPATH)
        return ProfilePage(self.driver)
    
    def click_login(self):
        from Pages.login_page import LoginPage
        log.info("Go to login")
        self.click_element(By.XPATH, self.EMAIL_HEADER_XPATH)
        return LoginPage(self.driver)
    
    def search(self):
        from Pages.search_page import SearchPage
        log.info("Open search screen")
        self.click_element(By.XPATH, self.MAG_BUTTON_XPATH)
        return SearchPage(self.driver)
    
    #Validations
    def validate_menu_is_shown(self):
        log.info("Validate Menu Screen")
        return self.get_actual_url() == self.URL_AME
    
    def validate_email_is_shown_and_expected(self, email):
        log.info("Validate email in Menu Screen")
        return self.get_header_email() == email