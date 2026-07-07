from playwright.sync_api import Page
from pages.login.sign_in_page import SignInPage

def login_platform(setup_browser_instance: Page, get_login_credentials: dict) -> None:
    """
    Logs in to the IceWarp browser app using the provided credentials.
    """

    login_page = SignInPage(setup_browser_instance)

    login_page.navigate_to_login_page(get_login_credentials["host"])
    login_page.fill_user_name(get_login_credentials["username"])

    password_input_page = login_page.click_continue_button()
    password_input_page.fill_password(get_login_credentials["password"])
    password_input_page.click_sign_in_button()