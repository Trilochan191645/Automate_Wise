import re
from token import EXACT_TOKEN_TYPES
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Open login page
    page.goto("http://69.62.123.60:3010/admin/login")

    # Login
    page.get_by_role("textbox", name="email@example.com").fill("test@user.com")
    page.get_by_role("textbox", name="••••••••").fill("Test@123")
    page.get_by_role("button", name="Login").click()

    # Dashboard loaded
   # expect(page.get_by_role("link", name="HTR Care Supp.")).to_be_visible() 
    # Go to Homepage
    page.get_by_role("link", name="Homepage").click()
    expect(page.get_by_role("heading", name="Homepage")).to_be_visible()
    expect(page.get_by_role("link", name="Edit Page")).to_be_visible()
    expect(page.get_by_role("heading", name="Hero Section")).to_be_visible()

    # Click Edit Page
    page.get_by_role("link", name="Edit Page").click()
    expect(expect(page.locator("text=HTR Care")).to_be_visible()).to_be_visible()

    # Update SEO fields
    page.locator('input[name="metaTitle"]').fill("HTR Care | Supported Accommodations updated")
    page.locator('input[name="focusKeyword"]').fill("test keywords updated")
    page.locator('textarea[name="metaDescription"]').fill("Sample description test")

    # Save
    page.get_by_role("button", name="Save Changes").click()

    # Close
    context.close()
    browser.close()


# Run script from terminal
with sync_playwright() as playwright:
    run(playwright)
