import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


class TestWiseAdmitLogin:

    BASE_URL = "https://www.wiseadmit.io/"
    VALID_EMAIL = "t.kafle191645@gmail.com"
    VALID_PASSWORD = "2000@Nishan"

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Navigate to login page before each test using POM"""
        self.login = LoginPage(page)
        self.login.navigate(self.BASE_URL)
        return page

    def test_valid_login(self, page: Page):
        """Verify Valid Login"""
        self.login.enter_email(self.VALID_EMAIL)
        self.login.click_login()
        self.login.enter_password(self.VALID_PASSWORD)
        self.login.click_login()

        expect(page.get_by_role("link", name="Dashboard")).to_be_visible(timeout=10000)
        expect(page.get_by_text("Nishan Kafle")).to_be_visible()

    def test_invalid_email_valid_password(self, page: Page):
        """Invalid email + valid password"""
        self.login.enter_email("invalid@email.com")
        self.login.click_login()

        expect(page.get_by_text("Failed to get student")).to_be_visible(timeout=5000)

    def test_valid_email_incorrect_password(self, page: Page):
        """Valid email + incorrect password"""
        self.login.enter_email(self.VALID_EMAIL)
        self.login.click_login()

        self.login.enter_password("WrongPassword123")
        self.login.click_login()

        expect(page.get_by_text("Invalid Credentials")).to_be_visible(timeout=5000)

    def test_email_format_validation(self, page: Page):
        """Invalid email format validation"""

        invalid_emails = [
            "notanemail",
            "missing@domain",
            "@nodomain.com",
            "spaces in@email.com",
            "double@@domain.com"
        ]

        for email in invalid_emails:
            self.login.enter_email(email)
            self.login.click_login()

            expect(page.get_by_text("Invalid Email")).to_be_visible(timeout=3000)
            self.login.enter_email("")  # clear field

    def test_empty_password_validation(self, page: Page):
        """Empty password validation"""
        self.login.enter_email(self.VALID_EMAIL)
        self.login.click_login()

        expect(page.get_by_text("Required")).to_be_visible(timeout=3000)
