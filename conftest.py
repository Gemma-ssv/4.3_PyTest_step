"""
conftest.py

Этот модуль содержит фикстуры и конфигурацию для pytest.
Он предоставляет фикстуру browser, которая настраивает браузер Chrome с указанным языком.
"""

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    """
    Добавляет опцию командной строки для указания языка браузера.

    Параметры:
    parser (argparse.ArgumentParser): Объект парсера, к которому добавляется опция.
    """
    parser.addoption('--language', action='store', default='en',
                     help="Выберите язык: например, 'en', 'ru', 'es', 'fr' и т.д.")

@pytest.fixture(scope="function")
def browser(request):
    """
    Фикстура для настройки браузера Chrome с указанным языком.

    Параметры:
    request (pytest.FixtureRequest): Объект запроса фикстуры, содержащий информацию о текущем тестовом запросе.

    Возвращает:
    webdriver.Chrome: Настроенный экземпляр браузера Chrome.
    """
    user_language = request.config.getoption("language")
    print(f"\nЗапуск браузера для теста с языком: {user_language}..")
    
    options = webdriver.ChromeOptions()
    options.add_argument(f"--lang={user_language}")
    
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nЗакрытие браузера..")
    browser.quit()