from Pages.home_page import HomePage
from Tests_API.get import get_wishlist

def test_scenario_three(driver):
    data = get_wishlist()
    home_page = HomePage(driver)
    
    # Use the 3 products from wishlist projeto_final as an argument for loop execution
    for index in range(3):
        product_name = data[index]["Product"]  
        actual_price = data[index]["Price"]
        formated_price =  float(actual_price.replace(".", "").replace(",", ".").strip())
        invalid_zipcode = "00000000"
        valid_zipcode = data[index]["Zipcode"]
        delivery_estimate = data[index]["delivery_estimate"]
        delivery_fee = data[index]["shipping_fee"]
        
        # 1. Open App: Launch the Americanas application.
        if home_page.check_popup():
            home_page.close_popup()
            
        # 2. Search for Product: Use the search bar to look for a product from the wishlist.
        search_page = home_page.search_product(product_name)
        
        # 3. Select Product: Tap on the desired product in the search results.
        product_page = search_page.click_product(product_name)
        
        # 4. Validate Product Page:
        # Confirm that the product name and price are correct according to the API response.
        assert product_page.validate_product_name_is_shown_and_expected(product_name), f"Product API: {product_name}, Product NAME: {product_page.get_product_name()}"
        assert product_page.validate_product_price_is_shown_and_expected(actual_price, formated_price), f"Price API:{actual_price}, Price PROD:{product_page.get_product_price(actual_price)}"
        
        product_page.scroll("down")
        # Enter an invalid ZIP code, click "Calculate", and verify that an error message is displayed.
        product_page.search_zipcode(invalid_zipcode)
        assert product_page.validate_zipcode_error_alert_is_shown_and_expected(), "Alert didn't show"
        
        # Enter the valid ZIP code returned by the API and validate the delivery time and shipping cost.
        product_page.search_zipcode(valid_zipcode)
        
        assert product_page.validate_delivery_time_is_shown_and_expected(delivery_estimate), f"DELIVERY ESTIMATE API: {delivery_estimate}"
        assert product_page.validate_delivery_fee_is_shown_and_expected(delivery_fee)
        
        # 5. Add to Cart: Tap the "Buy" button.
        product_page.buy_button()
        # 6. Validate Cart Popup:
        # In the cart popup, confirm the product name and price again.
        assert product_page.validate_product_name_popup_is_shown_and_expected(product_name)
        assert product_page.validate_product_price_popup_is_shown_and_expected(product_name, actual_price)
        
        # Increase the quantity to 2 and check if the quantity field is updated.
        product_page.add_one()
        assert product_page.get_quantity() == 2
        # Decrease the quantity to 1 and check if the decrease button ( - ) becomes inactive.
        product_page.remove_one()
        assert product_page.validate_remove_one_button_is_disable() 
        assert product_page.get_quantity() == 1
        
        # Increase the quantity to 2 again.
        product_page.add_one()
        assert product_page.get_quantity() == 2
        product_quantity = product_page.get_quantity()
        
        # 7. Add and go to cart: Proceed to the cart finalization screen.
        product_page.checkout_button()
        cart_page = product_page.cart_button()
        
        # 8. Validate Cart:
        # Confirm the product name and quantity.
        assert cart_page.validate_product_name_is_expected(product_name)
        assert cart_page.validate_product_quantity_is_expected(product_quantity), f"PRODUCT:{product_quantity}, GETPRODUCT{cart_page.get_product_quantity(product_quantity)}"
        
        # Check if the total product value and the order subtotal are double the unit price.
        new_value = formated_price * product_quantity
        new_value_formatted = str(f"{new_value:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        
        assert cart_page.validate_product_value_is_total_for_two_units(new_value_formatted, new_value)
        
        cart_page.scroll("down")
        assert cart_page.validate_product_subtotal_value_is_total_for_two_units(new_value)
        
        # Repeat the invalid and valid ZIP code test to ensure shipping calculation consistency.
        cart_page.search_zipcode(invalid_zipcode)
        assert cart_page.validate_zipcode_error_alert_is_shown_and_expected(), "Alert didn't show"
        cart_page.search_zipcode(valid_zipcode)
        assert cart_page.validate_delivery_time_is_shown_and_expected(delivery_estimate), f"DELIVERY ESTIMATE API: {delivery_estimate}"
        assert cart_page.validate_delivery_fee_is_shown_and_expected(delivery_fee)
        
        # Confirm that the value on the "Proceed to Checkout" button also reflects the total for two units.
        assert cart_page.validate_proceed_button_price_is_total_for_two_units(new_value)
    
        # 9. Proceed to Checkout: Tap "Proceed to Checkout".
        cart_page.click_proceed_button()
        
        # 10. Validate Redirect: Check if the login/checkout screen is displayed with the message "Enter your email to continue".
        assert cart_page.validate_email_title_is_shown_and_expected(), f"Get Email Title:{cart_page.get_email_title()}"