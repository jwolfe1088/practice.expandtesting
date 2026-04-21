from pages.base_page import BasePage

BASE_URL = "https://practice.expandtesting.com/notes/app"

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def navigate_to_home(self):
        self.navigate(BASE_URL)

    def click_login(self):
        self.page.get_by_role("link", name="Login").click()

    