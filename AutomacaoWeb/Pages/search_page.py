from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.PRODUCT_NAME_CLASS = "ProductCard_productName__mwx7Y"
        self.PRODUCT_PRICE_CLASS = "ProductCard_productPrice__XFEqu"
        self.LIST_VIEW_XPATH = "/html/body/div[1]/section[2]/div/div[2]/div[1]/div[1]/div[3]/div[2]/button[2]/span"
        self.FIRST_PRODUCT_CLASS = "ProductCard_productImage__60DdZ"
        
    # Getters
    def get_product_name(self):
        prod = self.find_element(By.CLASS_NAME, self.PRODUCT_NAME_CLASS)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", prod)
        return prod.text
    
    def get_product_price(self):
        price = self.get_element_text(By.CLASS_NAME, self.PRODUCT_PRICE_CLASS).replace("R$", "").replace("no Pix", "").replace(" ", "").replace(".", "").replace(",", ".").strip()
        return float(price)
    
    #Buttons & Clicks 
    def switch_to_list_view(self):
        self.click_element(By.XPATH, self.LIST_VIEW_XPATH)
        
    def click_product(self):
        from Pages.product_page import ProductPage
        self.click_element(By.CLASS_NAME, self.FIRST_PRODUCT_CLASS)
        return ProductPage(self.driver)
        
    # Validations
    def validate_product_name_is_shown_and_expected(self, product_name):
        return self.get_product_name() == product_name
    
    def validate_product_price_is_shown_and_expected(self, product_price):
        return self.get_product_price() == product_price