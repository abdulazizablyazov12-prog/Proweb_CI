import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver_chrome():
    options = Options()

    # ИСПРАВЛЕНО: Заставляем Selenium работать с элементами сразу после появления HTML,
    # не дожидаясь загрузки внешних стилей, картинок и аналитических трекеров
    options.page_load_strategy = 'eager'

    # 1. Принудительно задаем десктопный User-Agent, чтобы сайт отдавал десктопную верстку
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

    # 2. Переводим браузер в headless-режим (обязательно используем новый синтаксис)
    options.add_argument("--headless=new")

    # 3. Дополнительные важные флаги стабильности для Linux контейнеров
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Отключаем возможные баги с определением автоматизации
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    # ИСПРАВЛЕНО: Ограничиваем время ожидания загрузки HTML-страницы до 30 секунд
    driver.set_page_load_timeout(30)

    yield driver
    driver.quit()

@pytest.fixture
def driver_edge():
    options = Options()

    # ИСПРАВЛЕНО: Заставляем Selenium работать с элементами сразу после появления HTML,
    # не дожидаясь загрузки внешних стилей, картинок и аналитических трекеров
    options.page_load_strategy = 'eager'

    # 1. Принудительно задаем десктопный User-Agent, чтобы сайт отдавал десктопную верстку
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

    # 2. Переводим браузер в headless-режим (обязательно используем новый синтаксис)
    options.add_argument("--headless=new")

    # 3. Дополнительные важные флаги стабильности для Linux контейнеров
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Отключаем возможные баги с определением автоматизации
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    # ИСПРАВЛЕНО: Ограничиваем время ожидания загрузки HTML-страницы до 30 секунд
    driver.set_page_load_timeout(30)

    yield driver
    driver.quit()

@pytest.fixture
def driver_firefox():
    options = Options()

    # ИСПРАВЛЕНО: Заставляем Selenium работать с элементами сразу после появления HTML,
    # не дожидаясь загрузки внешних стилей, картинок и аналитических трекеров
    options.page_load_strategy = 'eager'

    # 1. Принудительно задаем десктопный User-Agent, чтобы сайт отдавал десктопную верстку
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

    # 2. Переводим браузер в headless-режим (обязательно используем новый синтаксис)
    options.add_argument("--headless=new")

    # 3. Дополнительные важные флаги стабильности для Linux контейнеров
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Отключаем возможные баги с определением автоматизации
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    # ИСПРАВЛЕНО: Ограничиваем время ожидания загрузки HTML-страницы до 30 секунд
    driver.set_page_load_timeout(30)

    yield driver
    driver.quit()

@pytest.fixture
def driver_safari():
    options = Options()

    # ИСПРАВЛЕНО: Заставляем Selenium работать с элементами сразу после появления HTML,
    # не дожидаясь загрузки внешних стилей, картинок и аналитических трекеров
    options.page_load_strategy = 'eager'

    # 1. Принудительно задаем десктопный User-Agent, чтобы сайт отдавал десктопную верстку
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

    # 2. Переводим браузер в headless-режим (обязательно используем новый синтаксис)
    options.add_argument("--headless=new")

    # 3. Дополнительные важные флаги стабильности для Linux контейнеров
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Отключаем возможные баги с определением автоматизации
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    # ИСПРАВЛЕНО: Ограничиваем время ожидания загрузки HTML-страницы до 30 секунд
    driver.set_page_load_timeout(30)

    yield driver
    driver.quit()