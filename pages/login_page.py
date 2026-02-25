from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("/login")

    def get_username_input(self):
        return self.page.locator("#username")

    def get_password_input(self):
        return self.page.locator("#password")

    def get_login_button(self):
        return self.page.get_by_role("button", name="Login")

    def get_flash_message(self):
        return self.page.locator("#flash")

    def login(self, username: str, password: str):
        self.get_username_input().fill(username)
        self.get_password_input().fill(password)
        self.get_login_button().click()

