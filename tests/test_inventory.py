import allure


@allure.feature("Inventory")
@allure.story("Inventory Listing")
def test_inventory_page_loaded(inventory_page):
    assert inventory_page.is_loaded()
    assert inventory_page.get_product_count() > 0


@allure.feature("Inventory")
@allure.story("Add to Cart")
def test_add_item_to_cart(inventory_page):
    inventory_page.add_first_product_to_cart()
    assert inventory_page.get_cart_count() == 1
