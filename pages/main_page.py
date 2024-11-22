"""Модуль main_page.py

Этот модуль содержит класс MainPage, 
который наследуется от базового класса BasePage.
Класс предоставляет методы для взаимодействия с главной страницей,
включая переход на страницу входа и проверку наличия ссылки на страницу входа.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage): 
    """
    Класс для работы с главной страницей.
    Наследуется от базового класса BasePage и предоставляет методы для взаимодействия с главной страницей.
    """

    def go_to_login_page(self):
        """
        Переходит на страницу входа, нажимая на ссылку входа.
        Использует локатор LOGIN_LINK из класса MainPageLocators.
        """
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        
    def should_be_login_link(self):
        """
        Проверяет, что ссылка на страницу входа присутствует на главной странице.
        Использует локатор LOGIN_LINK из класса MainPageLocators.
        """
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
