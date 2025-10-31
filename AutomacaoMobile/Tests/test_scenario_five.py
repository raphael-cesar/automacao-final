from Pages.home_page import HomePage
from Tests_API.get import get_wishlist
import time

def test_scenario_five(driver):
    data = get_wishlist()
    home_page = HomePage(driver)
    index = 0
    
    # Use the 3 products from wishlist projeto_final as an argument for loop execution
    for index in range(3):
        # 1. Access Website/App: Open the Americanas website or app.
        if home_page.check_popup():
            home_page.close_popup()
            
        # 2. Search for Product: Search for a product that exists in your API Wishlist.
        search_page = home_page.search_product(data[index]["Product"])
        # 3. Validate Grid View: In the grid view, confirm that the product title and price are correct.
        product_name = data[index]["Product"]  
        actual_price = data[index]["Price"]
        actual_price =  float(actual_price.replace(".", "").replace(",", ".").strip())
        
        print(search_page.get_product_name(index))
        assert search_page.validate_product_name_is_shown_and_expected(product_name, index), f"Product API: {product_name}, Product NAME: {search_page.get_product_name(index)}"
        print(search_page.get_product_price(index))
        assert search_page.validate_product_price_is_shown_and_expected(actual_price, index), f"Price API:{actual_price}, Price PROD:{search_page.get_product_price(index)}"
        
        # 4. Validate List View: Switch to the list view and confirm the title and price again.
        search_page.switch_list_grid()
        
        assert search_page.validate_product_name_is_shown_and_expected(product_name, index), f"Product API: {product_name}, Product NAME: {search_page.get_product_name(index)}"
        assert search_page.validate_product_price_is_shown_and_expected(actual_price, index), f"Price API:{actual_price}, Price PROD:{search_page.get_product_price(index)}"
        
        # 5. Access Product Page: Click on the product to see its details.
        product_page = search_page.click_product(index)

        # 6. Validate Details Page: Confirm for the last time that the product title and price are correct.
        assert product_page.validate_product_name_is_shown_and_expected(product_name), f"Product API: {product_name}, Product NAME: {product_page.get_product_name()}"
        assert product_page.validate_product_price_is_shown_and_expected(actual_price, index), f"Price API:{actual_price}, Price PROD:{product_page.get_product_price(index)}"
        
        home_page = product_page.back_menu()