from Pages.home_page import HomePage
from Tests_API.get import get_wishlist

def test_testes(driver):
    data = get_wishlist()
    home_page = HomePage(driver)
    product_name = data[2]["Product"]
    product_price = data[2]["Price"]
    product_price =  float(product_price.replace(".", "").replace(",", ".").strip())
    
    teste = home_page.search_product_teste(product_name)
        
    # 3. Validate Grid View: In the grid view, confirm that the product title and price are correct.
    print(teste.product_name(product_name))
    print(teste.get_product_name(product_name))
    print(teste.get_product_price(product_name))
    teste.click_product(product_name)
    
    print(teste.get_product_name_two(product_name))
    print(teste.get_product_price_two(product_price))
    