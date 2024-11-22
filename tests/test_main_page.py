"""Модуль test_main_page.py

Этот модуль содержит набор тестов для проверки функциональности
главной страницы и страницы входа на веб-сайте. 
Тесты используют библиотеку pytest для запуска и библиотеку
selenium для автоматизации браузера.
"""

from pages.main_page import MainPage
from pages.login_page import LoginPage


# Тест: Проверка возможности перехода на страницу входа
def test_guest_can_go_to_login_page(browser):
    """
    Тест проверяет, что гость может перейти на страницу входа с главной страницы.
    """
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

# Тест: Проверка корректности отображения страницы входа
def test_login_page(browser):
    """
    Тест проверяет, что страница входа отображается корректно.
    """
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
