from playwright.sync_api import Page

class AppHeaderFragment:

    def __init__(self, page: Page,
                username: str):

        self.page = page
        self.avatar_button_locator = ("//a[.//div[@class = 'component-avatar--image' and @data-email = '" +
                                          username + "']]")