from playwright.sync_api import Page


class SecurePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("/secure")

    def get_title(self):
        return self.page.title()

    def get_logout_button(self):
        return self.page.get_by_role("link", name="Logout")

    def get_page_content(self):
        return self.page.content()
