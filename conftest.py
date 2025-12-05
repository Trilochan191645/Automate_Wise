import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
        
@pytest.fixture
def page(browser):
    page=browser.new_page()
    yield page
    page.close()
            
            
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return { 
        **browser_context_args,
        "viewport": { "width": 1920, "height": 1080 }
    }