"""Модуль login_page.py

Этот модуль содержит класс LoginPage, который наследуется
от базового класса BasePage. Класс предоставляет методы
для проверки корректности отображения страницы входа,
включая проверку URL, наличия формы входа и формы регистрации.
"""

from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    """
    Класс для работы со страницей входа.
    Наследуется от базового класса BasePage и предоставляет методы для проверки корректности отображения страницы входа.
    """

    def should_be_login_page(self):
        """
        Проверяет, что страница входа отображается корректно.
        Вызывает методы для проверки URL, наличия формы входа и формы регистрации.
        """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """
        Проверяет, что текущий URL содержит подстроку 'login'.
        """
        assert "login" in self.browser.current_url, "Login URL is not correct"

    def should_be_login_form(self):
        """
        Проверяет, что форма входа присутствует на странице.
        Использует локатор LOGIN_FORM из класса LoginPageLocators.
        """
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """
        Проверяет, что форма регистрации присутствует на странице.
        Использует локатор REGISTRATION_FORM из класса LoginPageLocators.
        """
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"