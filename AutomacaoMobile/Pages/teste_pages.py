from appium.webdriver.common.appiumby import AppiumBy
from Pages.base_page import BasePage

class TestePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Locators
        
    def product_name(self, product):
        return f"//android.view.View[contains(@content-desc, '{product}')]"
     
    def product_price(self, price):
        return f"//android.view.View[contains(@content-desc, '{price}')]"
     
    def get_product_name(self, product):
        xpath = self.product_name(product)
        prod = self.get_element_attribute(AppiumBy.XPATH, xpath)
        if "%" in prod:
            prod = prod.split('\n')[1]
            return prod
        else:
            prod = prod.split('\n')[0]
            return prod    
        
    def get_product_price(self, product):
        xpath = self.product_name(product)
        price = self.get_element_attribute(AppiumBy.XPATH, xpath)
        if "%" in price:
            price = price.split('\n')[3]
            price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
            return price
        else:
            price = price.split('\n')[1]
            price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
            return price
            
    def click_product(self, product):
        from Pages.product_page import ProductPage
        xpath = self.product_name(product)
        self.click_element(AppiumBy.XPATH, xpath)
        return ProductPage(self.driver)
    
    def get_product_name_two(self, product):
        xpath = self.product_name(product)
        prod = self.get_element_attribute(AppiumBy.XPATH, xpath)
        return prod
    
    def get_product_price_two(self, price):
        xpath = self.product_price(price)
        price = self.get_element_attribute(AppiumBy.XPATH, xpath)
        price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
        return price