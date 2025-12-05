from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login(page):
    login_page=LoginPage(page)
    dashboard_page=DashboardPage(page)
    
    
    login_page.navigate()   # navigate to url
    
    login_page.login("test@user.com","Test@123")      #authentication
    
    dashboard_page.verify_dashboard_loaded()           # assertion 
    
