import pytest
from playwright.sync_api import Playwright, Page

import json

from typing import Generator

def pytest_addoption(parser: pytest.Parser) -> None:
    """
    Adds the pytest CLI option to run the test suite with the specified browser. The default browser is Chromium, but you can also select Firefox by using the `--browsername` option when running the tests.
    """

    parser.addoption(
        "--browsername", action = "store", default = "chromium", help = "Select the browser to run the tests."
    )

@pytest.fixture
def setup_browser_instance(playwright: Playwright,
                           request: pytest.FixtureRequest) -> Generator[Page, None, None]:
    """
    This fixture generates a browser instance, context, and the initial `Page` object for each test and each browser selected with the `--browsername` option. 
    """

    context = None
    browser = None

    browsername = request.config.getoption("--browsername")

    try:

        match browsername:

            case "chromium":
                browser = playwright.chromium.launch(
                    headless = False,
                    slow_mo = 2000
                )

            case "firefox":
                browser = playwright.firefox.launch()

            case _:
                raise Exception("Unknown browser specified. Launch test with the chromium, firefox, or both browsers.")

        context = browser.new_context()  # type: ignore
        page = context.new_page()

        yield page
    
    except Exception as e:
        pytest.fail(reason = str(e))

    finally:

        if context is not None:
            context.close()

        if browser is not None:
            browser.close()

@pytest.fixture
def get_login_credentials() -> dict:
    """
    This fixture gets test credentials and returns them as a dictionary.
    """

    with open("credentials/login.json", "r") as credentials_file:
        credentials = json.load(credentials_file)

    return credentials
