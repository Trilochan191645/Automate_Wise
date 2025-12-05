from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.cvs.com/")

    # Click "Find out more"
    page.get_by_role("link", name="Find out more about CVS").click()

    # Handle iframe popup safely
    frame = page.frame_locator("iframe[title='Invitation to provide feedback']")
    try:
        frame.get_by_role("button", name="No, thanks").click()
    except:
        pass  # Popup may not always appear

    # Validate logo
    expect(page.get_by_role("link", name="CVS Health Logo")).to_be_visible()

    # Validate search input
    expect(page.get_by_role("combobox")).to_be_visible()

    # Handle popup for Careers
    with page.expect_popup() as popup_info:
        page.get_by_role("contentinfo").get_by_role(
            "link", name="Careers Opens in a new window"
        ).click()

    page1 = popup_info.value

    # Accept cookie banner if present
    try:
        page1.get_by_role("button", name="Accept").click(timeout=5000)
    except:
        pass

    # Close chatbot if present
    try:
        page1.get_by_role("button", name="Close Chatbot Window").click(timeout=5000)
    except:
        pass

    # Open hamburger menu on the main page
    page.locator("//div[@class='phw-hamburger-block phw-d-lg-block phw-d-none']").click()

    # Navigate to Careers link (Python syntax)
    page.get_by_text("Careers", exact=True).click()

    # Click Innovation and Technology
    page.get_by_role("link", name="Innovation and Technology").click()

    # Search Innovation Jobs
    page.get_by_text("Search Innovation And Technology Jobs", exact=True).click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
