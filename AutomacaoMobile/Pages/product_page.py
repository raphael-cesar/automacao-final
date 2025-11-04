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
        self.ZIPCODE_ALERT_ID = '//android.widget.ImageView[@content-desc="Frete indisponível para o CEP: 00000-000"]'
        
        self.BUY_BUTTON_XPATH = '//android.view.View[@content-desc="comprar"]'
        
        self.ADD_ONE_XPATH = '//android.widget.ImageView[@resource-id="Aumentar quantidade em 1"]'
        
        self.REMOVE_ONE_XPATH = '//android.widget.ImageView[@resource-id="Reduzir quantidade em 1"]'
        
        self.QUANTITY_XPATH = '//android.view.View[@resource-id="Fechar modal carrinho"]//android.widget.EditText'
        
        self.CHECKOUT_BUTTON_XPATH = '//android.widget.Button[@content-desc="adicionar e continuar comprando"]'
        
        self.CART_ICON_XPATH = '//android.widget.ImageView[@resource-id="Carrinho"]'

    # Locator
    def product_name(self, product):
        return f"//android.view.View[contains(@content-desc, '{product}')]"
    
    def product_name_price_popup(self, product):
        return f"//android.widget.ImageView[contains(@content-desc, '{product}')]"
    
    def product_price(self, price):
        return f"//android.view.View[contains(@content-desc, '{price}')]"
    
    def delivery_path(self, delivery):
        return f"//android.view.View[contains(@content-desc, '{delivery}')]"
    
    def search_zipcode(self, data):
        self.click_element(AppiumBy.XPATH, self.ZIPCODE_INPUT_XPATH)
        self.find_element(AppiumBy.XPATH, self.ZIPCODE_INPUT_XPATH).clear()
        self.send_keys_to_element(AppiumBy.XPATH, self.ZIPCODE_INPUT_XPATH, data)
        self.click_element(AppiumBy.ACCESSIBILITY_ID, self.CALCULATE_ZIPCODE_BUTTON_ACC_ID)
    
    # Getters
    def get_product_name(self, product):
        xpath = self.product_name(product)
        prod = self.get_element_attribute(AppiumBy.XPATH, xpath)
        return prod
    
    def get_product_price(self, price):
        xpath = self.product_price(price)
        price = self.get_element_attribute(AppiumBy.XPATH, xpath)
        price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
        return price
    
    def get_product_name_popup(self, product):
        xpath = self.product_name_price_popup(product)
        prod = self.get_element_attribute(AppiumBy.XPATH, xpath)
        return prod
    
    def get_zipcode_error(self):
        return self.get_element_attribute(AppiumBy.XPATH, self.ZIPCODE_ALERT_ID)
    
    def get_delivery_fee(self, delivery):
        xpath = self.delivery_path(delivery)
        prod = self.get_element_attribute(AppiumBy.XPATH, xpath)
        return prod
    
    def get_quantity(self):
        return int(self.get_element_text(AppiumBy.XPATH, self.QUANTITY_XPATH))
    
    # Click & Buttons
    def back_menu(self):
        from Pages.home_page import HomePage
        self.click_element(AppiumBy.XPATH, self.BACK_BUTTON_XPATH)
        self.click_element(AppiumBy.XPATH, self.BACK_BUTTON_2_XPATH)
        self.click_element(AppiumBy.XPATH, self.CANCEL_SEARCH_XPATH) 
        return HomePage(self.driver) 
    
    def buy_button(self):
        self.click_element(AppiumBy.XPATH, self.BUY_BUTTON_XPATH)
        
    def add_one(self):
        self.click_element(AppiumBy.XPATH, self.ADD_ONE_XPATH)
        
    def remove_one(self):
        self.click_element(AppiumBy.XPATH, self.REMOVE_ONE_XPATH)
        
    def checkout_button(self):
        self.click_element(AppiumBy.XPATH, self.CHECKOUT_BUTTON_XPATH)
        
    def cart_button(self):
        from Pages.cart_page import CartPage
        self.click_element(AppiumBy.XPATH, self.CART_ICON_XPATH)
        return CartPage(self.driver)
    
    # Validations
    def validate_product_name_is_shown_and_expected(self, product_name):
        return self.get_product_name(product_name) == product_name
    
    def validate_product_name_popup_is_shown_and_expected(self, product_name):
        return product_name in self.get_product_name_popup(product_name)
    
    def validate_product_price_is_shown_and_expected(self, get_product_price, product_price):
        return self.get_product_price(get_product_price) == product_price
    
    def validate_product_price_popup_is_shown_and_expected(self, get_product_price, product_price):
        return product_price in self.get_product_name_popup(get_product_price)
    
    def validate_zipcode_error_alert_is_shown_and_expected(self):
        return "Frete indisponível" in self.get_zipcode_error()
    
    def validate_delivery_fee_is_shown_and_expected(self, delivery_fee):
        return delivery_fee in self.get_delivery_fee(delivery_fee)
    
    def validate_delivery_time_is_shown_and_expected(self, delivery_time):
        return delivery_time in self.get_delivery_fee(delivery_time)
    
    def validate_remove_one_button_is_disable(self):
        return self.is_element_enabled(AppiumBy.XPATH, self.REMOVE_ONE_XPATH)