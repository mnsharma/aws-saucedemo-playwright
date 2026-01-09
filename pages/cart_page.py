import allure


class CartPage:

    CART_URL_PART = "/cart.html"
    CART_ITEM = ".cart_item"
    CHECKOUT_BUTTON = "#checkout"
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"

    def __init__(self, page):
        self.page = page

    @allure.step("Verify cart page is loaded")
    def is_loaded(self):
        return self.CART_URL_PART in self.page.url

    @allure.step("Get cart items count")
    def get_items_count(self):
        return self.page.locator(self.CART_ITEM).count()

    @allure.step("Click continue shopping")
    def continue_shopping(self):
        self.page.click(self.CONTINUE_SHOPPING_BUTTON)

    @allure.step("Proceed to checkout")
    def go_to_checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)
