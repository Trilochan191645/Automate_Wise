from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.get_by_role("textbox", name="Email Address")
        self.password_input = page.locator("input[name='password']")
        self.login_btn = page.get_by_role("button", name="Log in")

    def navigate(self, base_url: str):
        self.page.goto(base_url)
        self.page.get_by_role("button", name="Are you a student?").click()
        self.page.get_by_role("button", name="Login").click()
        self.page.get_by_role("menuitem", name="Login as a Student").click()

    def enter_email(self, email: str):
        self.email_input.fill(email)

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_btn.click()

    def login(self, email: str, password: str):
        self.enter_email(email)
        self.click_login()
        self.enter_password(password)
        self.click_login()
