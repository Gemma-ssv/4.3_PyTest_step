"""Модуль locators.py

Этот модуль содержит классы, которые определяют локаторы (селекторы)
для различных элементов на веб-страницах. Локаторы используются
для поиска элементов на странице с помощью библиотеки selenium.
"""

from selenium.webdriver.common.by import By

class MainPageLocators():
    """
    Класс, содержащий локаторы для элементов на главной странице.
    """
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    """
    Класс, содержащий локаторы для элементов на странице входа.
    """
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_URL = (By.CSS_SELECTOR, "body")