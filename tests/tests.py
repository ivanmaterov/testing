from pages.main_page import MainPage


def test_toggle_between_pages(main_page: MainPage):
    """Test clicks by navigation links and checks navigation has appropriate text."""
    navigation = main_page.navigation
    for link in navigation.get_navigation_links():
        link.click()
        navigation.wait_until_navigation_display_page(link.get_text())


def test_find_product_using_search_field(main_page: MainPage):
    """Test finds a product using search field."""
    search_field = main_page.search_field
    search_field.fill_search_field('Диван-трансформер')
    product_cards = search_field.get_product_cards()
    product_card = product_cards[0]
    product_name = product_card.name
    product_detail_page = product_card.open_detail_page()
    assert product_detail_page.name == product_name
