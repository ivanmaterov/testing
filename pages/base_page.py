from page_object.page import Page
from pages.components.search_field import SearchField


class BasePage(Page):
    @property
    def search_field(self) -> SearchField:
        return
