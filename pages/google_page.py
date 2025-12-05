from playwright.sync_api import Page

class GooglePage:
    def __init__(self, page: Page):
        self.page = page

    def accept_cookies(self):
        try:
            self.page.get_by_role("button", name="Accept all").click(timeout=3000)
        except:
            print("No popup")

    def search(self, text):
        self.page.get_by_role("combobox", name="Search").fill(text)
        self.page.keyboard.press("Enter")
