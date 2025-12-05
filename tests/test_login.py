import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

class TestWiseAdmitLogin:
    """Test suite for WiseAdmit login functionality"""

    BASE_URL = "https://www.wiseadmit.io/"
    VALID_EMAIL = "t.kafle191645@gmail.com"
    VALID_PASSWORD = "2000@Nishan"

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup fixture runs before every test"""
        self.login = LoginPage(page)
        self.login.open_sign_in_page()  # navigate to student login page

    def test_valid_login(self, page: Page):
        """Verify valid login works"""
        self.login.login(self.VALID_EMAIL, self.VALID_PASSWORD)
        self.login.assert_dashboard_visible()                  # wait for dashboard
        self.login.assert_text_visible("Nishan Kafle")        # verify user name

    def test_invalid_email_valid_password(self, page: Page):
        """Verify login fails with invalid email"""
        self.login.login("invalid@email.com", self.VALID_PASSWORD)
        self.login.assert_text_visible("Failed to get student")

    def test_valid_email_incorrect_password(self, page: Page):
        """Verify login fails with valid email and wrong password"""
        self.login.login(self.VALID_EMAIL, "WrongPassword123")
        self.login.assert_text_visible("Invalid Credentials")

    def test_email_format_validation(self, page: Page):
        """Verify email format validation"""
        invalid_emails = [
            "notanemail",
            "missing@domain",
            "@nodomain.com",
            "spaces in@email.com",
            "double@@domain.com"
        ]
        for email in invalid_emails:
            self.login.login(email)
            self.login.assert_text_visible("Invalid Email")
            self.login.clear_email()

    def test_empty_password_validation(self, page: Page):
        """Verify empty password triggers required validation"""
        self.login.login(self.VALID_EMAIL, password="")
        self.login.assert_text_visible("Required")
