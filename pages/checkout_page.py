import allure


class CheckoutPage:

    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    COMPLETE_HEADER = ".complete-header"

    def __init__(self, page):
        self.page = page

    @allure.step("Enter checkout information")
    def enter_customer_info(self, first_name, last_name, postal_code):
        self.page.fill(self.FIRST_NAME, first_name)
        self.page.fill(self.LAST_NAME, last_name)
        self.page.fill(self.POSTAL_CODE, postal_code)
        self.page.click(self.CONTINUE_BUTTON)

    @allure.step("Finish checkout")
    def finish_checkout(self):
        self.page.click(self.FINISH_BUTTON)

    @allure.step("Verify checkout completed")
    def is_checkout_complete(self):
        return self.page.locator(self.COMPLETE_HEADER).is_visible()
