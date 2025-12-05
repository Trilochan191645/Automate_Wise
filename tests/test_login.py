import os
from dotenv import load_dotenv
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

# Load environment variables
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
VALID_EMAIL = os.getenv("VALID_EMAIL")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")


class TestWiseAdmitLogin:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Navigate to login page using POM"""
        self.login = LoginPage(page)
        self.login.navigate(BASE_URL)
        return page

    def test_valid_login(self, page: Page):
        """Verify Valid Login"""
        self.login.login(VALID_EMAIL, VALID_PASSWORD)
        expect(page.get_by_role("link", name="Dashboard")).to_be_visible(timeout=10000)
        expect(page.get_by_text("Nishan Kafle")).to_be_visible()

    def test_invalid_email_valid_password(self, page: Page):
        """Verify login fails with invalid email & valid password"""
        self.login.enter_email("invalid@email.com")
        self.login.click_login()
        expect(page.get_by_text("Failed to get student")).to_be_visible(timeout=5000)

    def test_valid_email_incorrect_password(self, page: Page):
        """Verify login fails with valid email & wrong password"""
        self.login.enter_email(VALID_EMAIL)
        self.login.click_login()
        self.login.enter_password("WrongPassword123")
        self.login.click_login()
        expect(page.get_by_text("Invalid Credentials")).to_be_visible(timeout=5000)

    def test_email_format_validation(self, page: Page):
        """Verify invalid email formats show validation error"""
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
            self.login.enter_email("")  # clear input

    def test_empty_password_validation(self, page: Page):
        """Verify empty password shows required validation"""
        self.login.enter_email(VALID_EMAIL)
        self.login.click_login()
        expect(page.get_by_text("Required")).to_be_visible(timeout=3000)
