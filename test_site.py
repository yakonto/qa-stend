import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()

def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser


def test_open_site_s6(browser):
    browser.get("https://demoblaze.com/")
    galaxy_s6 = browser.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]')
    galaxy_s6.click()
    title = browser.find_element(By.CSS_SELECTOR, value='h2')
    assert title.text == "Samsung galaxy s6"

def test_two_monitors(browser):
    browser.get("https://demoblaze.com/")
    # Кликаем по категории "Monitors"
    monitor_link = browser.find_element(By.XPATH, "//a[text()='Monitors']")
    monitor_link.click()

    # Ждём загрузки товаров (лучше использовать WebDriverWait вместо time.sleep)
    time.sleep(2)
    #WebDriverWait(browser, 10)

    # Находим все карточки товаров
    monitors = browser.find_elements(By.CSS_SELECTOR, ".card")

    # Проверяем, что отображается ровно 2 монитора
    assert len(monitors) == 2, f"Ожидалось 2 монитора, но найдено {len(monitors)}"