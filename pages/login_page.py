import allure


class LoginPage:

    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    @allure.step("Open login page")
    def open(self):
        self.page.goto(self.base_url)

    @allure.step("Enter username: {username}")
    def enter_username(self, username):
        if username is not None:
            self.page.fill(self.USERNAME, username)

    @allure.step("Enter password")
    def enter_password(self, password):
        if password is not None:
            self.page.fill(self.PASSWORD, password)

    @allure.step("Click login button")
    def click_login(self):
        self.page.click(self.LOGIN_BUTTON)

    @allure.step("Login with username: {username}")
    def login(self, username=None, password=None):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    @allure.step("Read login error message")
    def get_error_message(self):
        return self.page.locator(self.ERROR_MESSAGE).text_content()
