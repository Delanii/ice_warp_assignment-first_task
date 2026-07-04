from playwright.sync_api import Page

from pages.login.sign_in_page import SignInPage

def test_create_document(setup_browser_instance: Page,
                         get_login_credentials: dict) -> None:
    """
    """

    login_page = SignInPage(setup_browser_instance)

    login_page.navigate_to_login_page(get_login_credentials["host"])
    login_page.fill_user_name(get_login_credentials["username"])
    login_page.click_continue_button()