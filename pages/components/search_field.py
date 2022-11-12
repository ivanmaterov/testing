from functools import cached_property

from page_object.component import Component
from page_object.element import Element
from page_object.locator import XPathLocator
from pages.components.product.product_card import ProductCard


class SearchField(Component):
    """Represents search field on the main page."""
    @cached_property
    def input_element(self) -> Element:
        return self.init_element(
            locator=XPathLocator(
                query='//input[@id="title-search-input"]'
            )
        )

    def fill_search_field(self, text: str):
        """Fill search field with text"""
        self.input_element.fill(text)

    def get_product_cards(self) -> list[ProductCard]:
        card_elements = self.init_elements(
            locator=XPathLocator(
                query='//div[@class="content"]/a[@class="item"]'
            )
        )
        return [ProductCard(self.page, elem) for elem in card_elements]
