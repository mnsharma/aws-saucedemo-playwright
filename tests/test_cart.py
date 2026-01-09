import allure


@allure.feature("Cart")
@allure.story("View Cart")
def test_cart_page_loaded(cart_page):
    assert cart_page.is_loaded()
    assert cart_page.get_items_count() == 1


@allure.feature("Cart")
@allure.story("Continue Shopping")
def test_continue_shopping_from_cart(cart_page):
    cart_page.continue_shopping()
    assert "/inventory.html" in cart_page.page.url
