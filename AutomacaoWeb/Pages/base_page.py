from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))
        
    def click_element(self, by, locator):
        self.find_element(by, locator).click()

    def send_keys_to_element(self, by, locator, text):
        self.find_element(by, locator).send_keys(text)

    def get_element_text(self, by, locator):
        return self.find_element(by, locator).text
    
    def is_element_displayed(self, by, locator):
        try:
            return self.find_element(by, locator).is_displayed()
        except:
            return False
        
    def is_element_enabled(self, by, locator):
        try:
            return self.find_element(by, locator).is_enabled()
        except:
            return False
        
    def scroll(self, direction):
        self.driver.execute_script("mobile: scrollGesture", {
        "left": 0,
        "top": self.screen_height * 0.3,
        "width": self.screen_width,
        "height": self.screen_height * 0.5,
        "direction": f"{direction}",
        "percent": 1.0
    })