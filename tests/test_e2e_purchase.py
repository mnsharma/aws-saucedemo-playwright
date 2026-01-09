import allure
import pytest


@pytest.mark.serial
@allure.feature("E2E")
@allure.story("Complete Purchase Journey")
@allure.severity(allure.severity_level.BLOCKER)
def test_complete_purchase_flow(login_page, page):
    from pages.inventory_page import InventoryPage
    from pages.cart_page import CartPage
    from pages.checkout_page import CheckoutPage

    # Login
    login_page.login("standard_user", "secret_sauce")

    # Inventory
    inventory = InventoryPage(page)
    assert inventory.is_loaded()
    inventory.add_first_product_to_cart()
    assert inventory.get_cart_count() == 1
    inventory.go_to_cart()

    # Cart
    cart = CartPage(page)
    assert cart.is_loaded()
    assert cart.get_items_count() == 1
    cart.go_to_checkout()

    # Checkout
    checkout = CheckoutPage(page)
    checkout.enter_customer_info("Manoj", "Sharma", "302001")
    checkout.finish_checkout()

    assert checkout.is_checkout_complete()
