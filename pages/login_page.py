from playwright.sync_api import Page, expect

class LoginPage:
    """Page Object Model for WiseAdmit login page"""

    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.wiseadmit.io/"

        # Locators
        self.student_button = page.get_by_role("button", name="Are you a student?")
        self.login_button = page.get_by_role("button", name="Login")
        self.login_as_student = page.get_by_role("menuitem", name="Login as a Student")
        self.email_input = page.get_by_role("textbox", name="Email Address")
        self.password_input = page.locator("input[name='password']")
        self.submit_button = page.get_by_role("button", name="Log in")
        self.dashboard_link = page.get_by_role("link", name="Dashboard")

    def open_sign_in_page(self):
        """Navigate to student login page"""
        self.page.goto(self.base_url)
        self.student_button.click()
        self.login_button.click()
        self.login_as_student.click()

    def login(self, email: str, password: str = None):
        """Fill in login credentials"""
        self.email_input.fill(email)
        self.submit_button.click()

        # Only fill password if visible
        if password and self.password_input.is_visible(timeout=3000):
            self.password_input.fill(password)
            self.submit_button.click()

    def assert_dashboard_visible(self):
        expect(self.dashboard_link).to_be_visible(timeout=10000)

    def assert_text_visible(self, text: str):
        expect(self.page.get_by_text(text)).to_be_visible(timeout=5000)

    def clear_email(self):
        self.email_input.clear()
