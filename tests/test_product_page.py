"""Модуль test_product_page.py

Этот модуль содержит набор тестов для проверки функциональности страницы 
продукта на веб-сайте. Тесты используют библиотеку pytest для
параметризации ссылок на страницы и библиотеку selenium для автоматизации браузера.
"""
import pytest
from pages.product_page import ProductPage

# Список параметров для тестирования различных вариантов страницы
params = [
    '?promo=offer0',
]

# Тест: Проверка, что после добавления продукта в корзину, сообщение об успешном добавлении не отображается
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" + param for param in params
])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    """
    Тест проверяет, что после добавления продукта в корзину, сообщение об успешном добавлении не отображается.
    """
    page = ProductPage(browser, link) 
    page.open()
    page.go_to_caart_page_2()

# Тест: Проверка, что сообщение об успешном добавлении продукта в корзину не отображается, если продукт не был добавлен
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" + param for param in params
])
def test_guest_cant_see_success_message(browser, link):
    """
    Тест проверяет, что сообщение об успешном добавлении продукта в корзину не отображается, если продукт не был добавлен.
    """
    page = ProductPage(browser, link) 
    page.open()
    page.go_to_caart_page_3()

# Тест: Проверка, что сообщение об успешном добавлении продукта в корзину исчезает после добавления продукта
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" + param for param in params
])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    """
    Тест проверяет, что сообщение об успешном добавлении продукта в корзину исчезает после добавления продукта.
    """
    page = ProductPage(browser, link) 
    page.open()
    page.go_to_caart_page_4()
