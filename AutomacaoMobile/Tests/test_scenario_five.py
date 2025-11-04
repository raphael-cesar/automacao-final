from Pages.home_page import HomePage
from Tests_API.get import get_wishlist

def test_scenario_five(driver):
    data = get_wishlist()
    home_page = HomePage(driver)
    index = 0
    
    # Use the 3 products from wishlist projeto_final as an argument for loop execution
    for index in range(3):
        product_name = data[index]["Product"]  
        actual_price = data[index]["Price"]
        formated_price =  float(actual_price.replace(".", "").replace(",", ".").strip())
        
        # 1. Access Website/App: Open the Americanas website or app.
        if home_page.check_popup():
            home_page.close_popup()
            
        # 2. Search for Product: Search for a product that exists in your API Wishlist.
        search_page = home_page.search_product(product_name)
        
        # 3. Validate Grid View: In the grid view, confirm that the product title and price are correct.
        print(search_page.get_product_name(product_name))
        assert search_page.validate_product_name_is_shown_and_expected(product_name), f"Product API: {product_name}, Product NAME: {search_page.get_product_name(product_name)}"
        
        print(search_page.get_product_price(product_name))
        assert search_page.validate_product_price_is_shown_and_expected(formated_price, product_name), f"Price API:{formated_price}, Price PROD:{search_page.get_product_price(product_name)}"
        
        # 4. Validate List View: Switch to the list view and confirm the title and price again.
        search_page.switch_list_grid()
        
        assert search_page.validate_product_name_is_shown_and_expected(product_name), f"Product API: {product_name}, Product NAME: {search_page.get_product_name(product_name)}"
        
        assert search_page.validate_product_price_is_shown_and_expected(formated_price, product_name), f"Price API:{formated_price}, Price PROD:{search_page.get_product_price(product_name)}"
        
        # 5. Access Product Page: Click on the product to see its details.
        product_page = search_page.click_product(product_name)

        # 6. Validate Details Page: Confirm for the last time that the product title and price are correct.
        assert product_page.validate_product_name_is_shown_and_expected(product_name), f"Product API: {product_name}, Product NAME: {product_page.get_product_name()}"
        assert product_page.validate_product_price_is_shown_and_expected(actual_price, formated_price), f"Price API:{actual_price}, Price PROD:{product_page.get_product_price(actual_price)}"
        
        home_page = product_page.back_menu()