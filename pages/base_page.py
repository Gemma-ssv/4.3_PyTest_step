"""Модуль base_page.py

Этот модуль содержит базовый класс BasePage, 
который предоставляет общие методы для работы с веб-страницами.
Класс использует библиотеку selenium для взаимодействия 
с веб-элементами и библиотеку requests для проверки доступности URL.

Returns:
    _type_: _description_
"""

import math
import time
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    """
    Базовый класс для работы с веб-страницами.
    Предоставляет общие методы для открытия страниц, поиска элементов,
    работы с алертами и проверки доступности URL.
    """

    def __init__(self, browser, url, timeout=10):
        """
        Инициализация объекта BasePage.

        :param browser: Объект WebDriver для управления браузером.
        :param url: URL страницы, с которой будет работать объект.
        :param timeout: Время ожидания для неявного ожидания элементов (по умолчанию 10 секунд).
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def open(self):
        """
        Открывает страницу по URL, указанному при инициализации объекта.
        """
        self.browser.get(self.url)
    
    def is_element_present(self, how, what):
        """
        Проверяет, присутствует ли элемент на странице.

        :param how: Способ поиска элемента (например, By.ID, By.CSS_SELECTOR).
        :param what: Значение, по которому ищется элемент (например, 'element_id').
        :return: True, если элемент присутствует, иначе False.
        """
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    def quiz(self):
        """
        Обрабатывает алерт с математическим выражением, вычисляет ответ и вводит его в алерт.
        """
        try:
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
            
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            time.sleep(3)
        except NoAlertPresentException:
            print("No second alert presented")
            
    def is_not_element_present(self, how, what, timeout=4):
        """
        Проверяет, что элемент не присутствует на странице в течение указанного времени.

        :param how: Способ поиска элемента (например, By.ID, By.CSS_SELECTOR).
        :param what: Значение, по которому ищется элемент (например, 'element_id').
        :param timeout: Время ожидания (по умолчанию 4 секунды).
        :return: True, если элемент не присутствует, иначе False.
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False     
    
    def is_disappeared(self, how, what, timeout=4):
        """
        Проверяет, что элемент исчезает со страницы в течение указанного времени.

        :param how: Способ поиска элемента (например, By.ID, By.CSS_SELECTOR).
        :param what: Значение, по которому ищется элемент (например, 'element_id').
        :param timeout: Время ожидания (по умолчанию 4 секунды).
        :return: True, если элемент исчезает, иначе False.
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
    
    def is_request_url(self, url):
        """
        Проверяет, доступен ли указанный URL.

        :param url: URL для проверки.
        :return: True, если URL доступен (статус код 200), иначе False.
        """
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception:
            return False
