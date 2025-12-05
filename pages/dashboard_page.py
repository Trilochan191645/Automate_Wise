from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.logo = page.get_by_role("link", name="HTR Care Supp.")
        self.homepage_link = page.get_by_role("link", name="Homepage")
        self.welcome_message = page.get_by_role("heading", name="Welcome, Admin 👋")

    # def verify_dashboard_loaded(self):
    #     expect(self.logo).to_be_visible()
    #     expect(self.homepage_link).to_be_visible()
    #     expect(self.welcome_message).to_be_visible()
    def go_to_homepage(self):
        self.homepage_link.click()

    def verify_homepage_loaded(self):
        expect(self.page.get_by_role("heading", name="Homepage")).to_be_visible()