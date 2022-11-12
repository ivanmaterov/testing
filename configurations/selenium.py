import pytest
from _pytest.fixtures import SubRequest
from selenium.webdriver.remote.webdriver import WebDriver


class SeleniumConfigurationPlugin:
    LOCALE = "ru, ru_RU"

    @pytest.fixture(scope="session")
    def webdriver_name(self, request: SubRequest) -> str:
        return request.config.getoption("--webdriver")

    @pytest.fixture(scope="session")
    def window_size(self, request: SubRequest) -> tuple[int]:
        return request.config.getoption("--webdriver-window-size").split(",")

    @pytest.fixture(scope="session")
    def implicitly_wait(self, request: SubRequest) -> int:
        return int(request.config.getoption("--webdriver-implicitly-wait"))

    @pytest.fixture
    def chrome_options(self, chrome_options):
        preferences = {
            "intl.accept_languages": self.LOCALE,
        }
        chrome_options.add_experimental_option("prefs", preferences)
        return chrome_options

    @pytest.fixture
    def webdriver(
        self,
        selenium: WebDriver,
        window_size: tuple[int],
        implicitly_wait: int,
    ) -> WebDriver:
        webdriver = selenium
        webdriver.set_window_size(*window_size)
        webdriver.implicitly_wait(implicitly_wait)
        return webdriver
