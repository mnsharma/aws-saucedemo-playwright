import allure
import pytest
from pages.inventory_page import InventoryPage


@allure.feature("Login")
@allure.story("Negative Login")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        ("standard_user", "wrong_password", "Username and password do not match"),
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
        (None, None, "Username is required"),
    ],
    ids=[
        "invalid_password",
        "locked_user",
        "empty_credentials",
    ]
)
def test_login_negative_cases(login_page, username, password, expected_error):
    if username is None and password is None:
        login_page.click_login()
    else:
        login_page.login(username, password)

    assert expected_error in login_page.get_error_message()


@allure.feature("Login")
@allure.story("Positive Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success(login_page, page):
    inventory = InventoryPage(page)
    login_page.login("standard_user", "secret_sauce")
    assert inventory.is_loaded()
