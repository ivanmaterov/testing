from functools import cached_property

from page_object.locator import XPathLocator
from pages.main_page import MainPage


class ProductDetailPage(MainPage):
    @cached_property
    def name(self) -> str:
        return self.init_element(
            locator=XPathLocator('//h1[@id="pagetitle"]'),
        ).get_text()
