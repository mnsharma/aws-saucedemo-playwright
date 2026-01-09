import allure


@allure.feature("Checkout")
@allure.story("Complete Purchase")
def test_complete_checkout(checkout_page):
    checkout_page.enter_customer_info(
        first_name="Mohan",
        last_name="Sharma",
        postal_code="302001"
    )

    checkout_page.finish_checkout()
    assert checkout_page.is_checkout_complete()
