import pytest
from playwright.sync_api import Page, expect


class TestURLNavigation:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup before each test"""
        self.page = page
        self.base_url = "http://69.62.123.60:3010/"

    def test_navigate_to_url_and_verify(self):
        """Navigate and verify page loaded successfully"""

        # Navigate to given URL
        response = self.page.goto(self.base_url)

        # Assert response status
        assert response.ok, f"Navigation failed with status: {response.status}"
        assert response.status == 200, f"Expected status 200, got {response.status}"

        # Assert URL is correct
        expect(self.page).to_have_url(self.base_url)

        # Assert page title is not empty
        title = self.page.title()
        assert title is not None and len(title) > 0, "Page title is empty"

        # Assert logo or alternative image text is visible (example)
        logo = self.page.get_by_alt_text("support accomodation")
        expect(logo).to_be_visible()
