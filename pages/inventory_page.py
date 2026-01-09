import allure


class InventoryPage:

    INVENTORY_CONTAINER = ".inventory_list"
    INVENTORY_ITEM = ".inventory_item"
    ADD_TO_CART_BUTTON = "button[data-test^='add-to-cart']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    def __init__(self, page):
        self.page = page

    @allure.step("Verify inventory page is loaded")
    def is_loaded(self):
        return self.page.url.endswith("/inventory.html") and \
               self.page.locator(self.INVENTORY_CONTAINER).is_visible()

    @allure.step("Get number of products displayed")
    def get_product_count(self):
        return self.page.locator(self.INVENTORY_ITEM).count()

    @allure.step("Add first product to cart")
    def add_first_product_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()

    @allure.step("Get cart badge count")
    def get_cart_count(self):
        return int(self.page.locator(self.CART_BADGE).inner_text())

    @allure.step("Navigate to cart page")
    def go_to_cart(self):
        self.page.click(self.CART_LINK)
