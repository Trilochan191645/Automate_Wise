import pytest
from playwright.sync_api import Page, expect


class TestWiseAdmitLogin:
    """Test suite for WiseAdmit login functionality"""

    BASE_URL = "https://www.wiseadmit.io/"
    VALID_EMAIL = "t.kafle191645@gmail.com"
    VALID_PASSWORD = "2000@Nishan"

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Navigate to login page before each test"""
        page.goto(self.BASE_URL)
        page.get_by_role("button", name="Are you a student?").click()
        page.get_by_role("button", name="Login").click()
        page.get_by_role("menuitem", name="Login as a Student").click()
        yield page

    def test_valid_login(self, page: Page):
        """Verify Valid Login"""
        page.get_by_role("textbox", name="Email Address").fill(self.VALID_EMAIL)
        page.get_by_role("button", name="Log in").click()

        page.locator("input[name='password']").fill(self.VALID_PASSWORD)
        page.get_by_role("button", name="Log in").click()

        # Assertions
        expect(page.get_by_role("link", name="Dashboard")).to_be_visible(timeout=10000)
        expect(page.get_by_text("Nishan Kafle")).to_be_visible()

    def test_invalid_email_valid_password(self, page: Page):
        """Verify Login Fails with Invalid Email & Valid Password"""
        page.get_by_role("textbox", name="Email Address").fill("invalid@email.com")
        page.get_by_role("button", name="Log in").click()

        expect(page.get_by_text("Failed to get student")).to_be_visible(timeout=5000)

    def test_valid_email_incorrect_password(self, page: Page):
        """Verify Login Fails with Valid Email & Incorrect Password"""
        page.get_by_role("textbox", name="Email Address").fill(self.VALID_EMAIL)
        page.get_by_role("button", name="Log in").click()

        page.locator("input[name='password']").fill("WrongPassword123")
        page.get_by_role("button", name="Log in").click()

        expect(page.get_by_text("Invalid Credentials")).to_be_visible(timeout=5000)

    def test_email_format_validation(self, page: Page):
        """Verify Email Format Validation"""
        invalid_emails = [
            "notanemail",
            "missing@domain",
            "@nodomain.com",
            "spaces in@email.com",
            "double@@domain.com"
        ]

        for email in invalid_emails:
            page.get_by_role("textbox", name="Email Address").fill(email)
            page.get_by_role("button", name="Log in").click()
            expect(page.get_by_text("Invalid Email")).to_be_visible(timeout=3000)
            page.get_by_role("textbox", name="Email Address").clear()

    def test_empty_password_validation(self, page: Page):
        """Verify empty password validation"""
        page.get_by_role("textbox", name="Email Address").fill(self.VALID_EMAIL)
        page.get_by_role("button", name="Log in").click()

        page.locator("input[name='password']").fill("")
        page.get_by_role("button", name="Log in").click()

        expect(page.get_by_text("Required")).to_be_visible(timeout=3000)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080}
    }


if __name__ == "__main__":
    pytest.main(["-v", "--headed"])
