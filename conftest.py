import pytest
from playwright.sync_api import Playwright, Page

from typing import Generator

def pytest_addoption(parser: pytest.Parser) -> None:
    """
    """

    parser.addoption(
        "--browsername", action = "store", default = "chromium", help = "Select the browser to run the tests."
    )

@pytest.fixture
def setup_browser_instance(playwright: Playwright,
                           request: pytest.FixtureRequest) -> Generator[Page]:
    """
    This fixture generates a browser instance, context, and the initial `Page` object for each test and each browser selected with the `--browsername` option. 
    """

    context = None
    browser = None

    browsername = request.config.getoption("--browsername")

    try:

        match browsername:

            case "chromium":
                browser = playwright.chromium.launch()

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