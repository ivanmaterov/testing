import pytest

from pages.main_page import MainPage


@pytest.fixture
def main_page(user_webdriver) -> MainPage:
    return MainPage(webdriver=user_webdriver)
