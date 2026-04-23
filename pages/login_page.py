from pages.base_page import BasePage

BASE_URL = "https://practice.expandtesting.com/notes/app/login"

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def navigate_to_login(self):
        self.navigate(BASE_URL)

    def login(self, email, password):
        self.page.get_by_test_id("login-email").fill(email)
        self.page.get_by_test_id("login-password").fill(password)
        self.page.get_by_test_id("login-submit").click()
        self.page.wait_for_url("https://practice.expandtesting.com/notes/app")

    def bad_login(self, email, password):
        self.page.get_by_test_id("login-email").fill(email)
        self.page.get_by_test_id("login-password").fill(password)
        self.page.get_by_test_id("login-submit").click()
    
    def get_alert_message(self):
        self.page.wait_for_selector("[data-testid='alert-message']")
        return self.page.get_by_test_id("alert-message").is_visible()