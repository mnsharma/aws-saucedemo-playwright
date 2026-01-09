import pytest
import allure
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def login_page(page, base_url):
    login = LoginPage(page, base_url)
    login.open()
    return login


@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"


@pytest.fixture
def inventory_page(login_page, page):
    login_page.login("standard_user", "secret_sauce")
    return InventoryPage(page)


@pytest.fixture
def cart_page(inventory_page):
    inventory_page.add_first_product_to_cart()
    inventory_page.go_to_cart()
    return CartPage(inventory_page.page)


@pytest.fixture
def checkout_page(cart_page):
    cart_page.go_to_checkout()
    return CheckoutPage(cart_page.page)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )