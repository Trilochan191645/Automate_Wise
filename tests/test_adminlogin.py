import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://69.62.123.60:3010/admin/login")    #navigation 
    
    page.get_by_role("textbox", name="email@example.com").click()      # authenticaton
    page.get_by_role("textbox", name="email@example.com").fill("admin@htrsupport.com")
    page.get_by_role("textbox", name="••••••••").click()
    page.get_by_role("textbox", name="••••••••").fill("Admin@123")
    page.get_by_role("button", name="Login").click()
    
    
    expect(page.get_by_role("link", name="HTR Care Supp.")).to_be_visible()   #assertion
    
    expect(page.get_by_role("link", name="Homepage")).to_be_visible()
    page.get_by_role("link", name="HTR Care Supp.").click()
  
    expect(page.get_by_role("heading", name="Welcome, Admin 👋")).to_be_visible()

