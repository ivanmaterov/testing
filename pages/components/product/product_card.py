from functools import cached_property

from page_object.component import Component
from page_object.element import Element
from page_object.locator import XPathLocator
from page_object.page import Page


class ProductCard(Component):
    """Represents product card in the search selector below search field."""
    def __init__(self, page: Page, base_element: Element):
        """Init base element for product card in the search selector."""
        super().__init__(page)
        self.base_element = base_element
        self.base_locator = base_element.locator

    @cached_property
    def image_link(self) -> str:
        return self.init_element(
            locator=self.base_locator + XPathLocator('//img')
        ).get_attribute('src')

    @cached_property
    def name(self) -> str:
        return self.init_element(
            locator=self.base_locator + XPathLocator('//span[@class="name"]')
        ).get_text()

    @cached_property
    def price(self) -> int:
        raw_data = self.init_element(
            locator=self.base_locator + XPathLocator('//span[@class="price"]')
        ).get_text()
        return int(''.join([symbol for symbol in raw_data if symbol.isdigit()]))

    def open_detail_page(self) -> 'ProductDetailPage':  # noqa
        """Open product detail page."""
        #  because of circular import
        from pages.product_detail_page import ProductDetailPage
        self.base_element.click()
        return ProductDetailPage(webdriver=self.webdriver)
