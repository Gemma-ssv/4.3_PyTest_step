import pytest
from pages.product_page import ProductPage


params = [
    '?promo=offer0',
]

@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" + param for param in params
])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link) 
    page.open()
    page.go_to_caart_page_2()


@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" + param for param in params
])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link) 
    page.open()
    page.go_to_caart_page_3()

@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" + param for param in params
])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link) 
    page.open()
    page.go_to_caart_page_4()
