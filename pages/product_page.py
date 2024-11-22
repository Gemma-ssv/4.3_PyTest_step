"""Модуль product_page.py

Этот модуль содержит класс ProductPage, который наследуется
от базового класса BasePage. Класс предоставляет методы для
взаимодействия со страницей продукта, включая добавление
продукта в корзину и проверку соответствия данных о продукте.
"""

import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage): 
    """
    Класс для работы со страницей продукта.
    Наследуется от базового класса BasePage и предоставляет методы для взаимодействия со страницей продукта.
    """

    def go_to_caart_page(self):
        """
        Добавляет продукт в корзину и проверяет соответствие данных о продукте.
        """
        time.sleep(3)
        add_cart = self.browser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button")
        name_product = self.browser.find_element(By.CSS_SELECTOR, "html.no-js body#default.default div.container-fluid.page div.page_inner div.content div#content_inner article.product_page div.row div.col-sm-6.product_main h1").text
        price_product = self.browser.find_element(By.CLASS_NAME, "price_color").text
        add_cart.click()
        self.quiz()
        name_product2 = self.browser.find_element(By.CSS_SELECTOR,"#messages > div:nth-child(1) > div > strong").text
        
        cart = self.browser.find_element(By.CSS_SELECTOR,"#messages > div:nth-child(2) > div > strong").text
        
        price_product2 = self.browser.find_element(By.CSS_SELECTOR,"#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong").text
        
        assert name_product == name_product2

        assert cart == 'Deferred benefit offer'
        
        assert price_product == price_product2
    
    def go_to_caart_page_2(self):
        """
        Добавляет продукт в корзину и проверяет, что сообщение об успешном добавлении не появляется.
        """
        time.sleep(3)
        add_cart = self.browser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button")
        add_cart.click()
        self.quiz()    
        assert self.is_not_element_present(By.CSS_SELECTOR,"#messages > div:nth-child(2) > div > strong")
    
    def go_to_caart_page_3(self):
        """
        Проверяет, что сообщение об успешном добавлении продукта в корзину не появляется.
        """
        time.sleep(3)
        assert self.is_not_element_present(By.CSS_SELECTOR,"#messages > div:nth-child(2) > div > strong")
    
    def go_to_caart_page_4(self):
        """
        Добавляет продукт в корзину и проверяет, что сообщение об успешном добавлении исчезает.
        """
        time.sleep(3)
        add_cart = self.browser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button")
        add_cart.click()
        self.quiz() 
        assert self.is_disappeared(By.CSS_SELECTOR,"#messages > div:nth-child(2) > div > strong")
        