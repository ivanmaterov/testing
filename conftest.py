from _pytest.config.argparsing import Parser
from selenium.webdriver.remote.webdriver import WebDriver
import pytest
import os


pytest_plugins = (
    'configurations.plugin'
)


@pytest.fixture
def user_webdriver(webdriver: WebDriver) -> WebDriver:
    import ipdb; ipdb.set_trace()
    webdriver.get(os.environ['BASE_URL'])
    return webdriver


def pytest_addoption(parser: Parser):
    """Set up cmd args."""
    parser.addoption(
        "--webdriver-window-size",
        action="store",
        default="1920,1080",
        help="Size of browser window in pixels",
    )
    parser.addoption(
        "--webdriver-implicitly-wait",
        action="store",
        default=2,
    )
