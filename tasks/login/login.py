from playwright.sync_api import Page

from fragments.app.app_header import AppHeaderFragment

from pages.login.sign_in_page import SignInPage
from pages.app.dashboard_page import DashboardPage

def login_platform(page: Page, get_login_credentials: dict,
                   app_header: AppHeaderFragment) -> DashboardPage:
    """
    Logs in to the IceWarp browser app using the provided credentials.
    """

    login_page = SignInPage(page)

    login_page.navigate_to_login_page(get_login_credentials["host"])
    login_page.fill_user_name(get_login_credentials["username"])

    password_input_page = login_page.click_continue_button()
    password_input_page.fill_password(get_login_credentials["password"])
    password_input_page.click_sign_in_button()

    return DashboardPage(page, app_header)