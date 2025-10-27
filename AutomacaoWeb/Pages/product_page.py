from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.PRODUCT_TITLE_CLASS = "ProductInfoCenter_title__hdTX_"
        self.PRICE_TITLE_CLASS = "ProductPrice_productPrice__vpgdo"
    
    def return_driver(self):
        from Pages.menu_page import MenuPage
        return MenuPage(self.driver)
       
    # Getters
    def get_product_name(self):
        return self.get_element_text(By.CLASS_NAME, self.PRODUCT_TITLE_CLASS)
    
    def get_product_price(self):
        price = self.get_element_text(By.CLASS_NAME, self.PRICE_TITLE_CLASS).replace("R$", "").replace("no Pix", "").replace(" ", "").replace(".", "").replace(",", ".").strip()
        return float(price)
    
    def validate_product_name_is_shown_and_expected(self, product_name):
        return self.get_product_name() == product_name
    
    def validate_product_price_is_shown_and_expected(self, product_price):
        return self.get_product_price() == product_price