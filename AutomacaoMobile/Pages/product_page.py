from appium.webdriver.common.appiumby import AppiumBy
from Pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Locators
        self.BACK_BUTTON_XPATH = '//android.widget.ImageView[@resource-id="Voltar"]'
        self.BACK_BUTTON_2_XPATH = '//android.view.View[@resource-id="Voltar"]'
        
        self.CANCEL_SEARCH_XPATH = '//android.view.View[@resource-id="Cancelar Busca"]/android.widget.ImageView'
        
        self.ZIPCODE_INPUT_XPATH = '//android.widget.EditText[@resource-id="Digite o CEP"]'
        self.CALCULATE_ZIPCODE_BUTTON_ACC_ID = 'Calcular'
        self.ZIPCODE_ALERT_ID = 'Snackbar alerta'

    # Locator
    def product_name(self, product):
        return f"//android.view.View[contains(@content-desc, '{product}')]"
    
    def product_price(self, price):
        return f"//android.view.View[contains(@content-desc, '{price}')]"
    
    
    def search_zipcode(self, data):
        self.click_element(AppiumBy.XPATH, self.ZIPCODE_INPUT_XPATH)
        self.send_keys_to_element(AppiumBy.XPATH, self.ZIPCODE_INPUT_XPATH, data)
        self.click_element(AppiumBy.ACCESSIBILITY_ID, self.CALCULATE_ZIPCODE_BUTTON_ACC_ID)
    
    def back_menu(self):
        from Pages.home_page import HomePage
        self.click_element(AppiumBy.XPATH, self.BACK_BUTTON_XPATH)
        self.click_element(AppiumBy.XPATH, self.BACK_BUTTON_2_XPATH)
        self.click_element(AppiumBy.XPATH, self.CANCEL_SEARCH_XPATH) 
        return HomePage(self.driver) 
    
    # Getters
    def get_product_name(self, product):
        xpath = self.product_name(product)
        prod = self.get_element_attribute(AppiumBy.XPATH, xpath, "contentDescription")
        return prod
    
    def get_product_price(self, price):
        xpath = self.product_price(price)
        price = self.get_element_attribute(AppiumBy.XPATH, xpath, "contentDescription")
        price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
        return price
    
    # Validations
    def validate_product_name_is_shown_and_expected(self, product_name):
        return self.get_product_name(product_name) == product_name
    
    def validate_product_price_is_shown_and_expected(self, get_product_price, product_price):
        return self.get_product_price(get_product_price) == product_price
    
    def validate_zipcode_error_alert_is_shown_and_expected(self):
        return self.is_element_displayed(AppiumBy.ID, self.ZIPCODE_ALERT_ID)