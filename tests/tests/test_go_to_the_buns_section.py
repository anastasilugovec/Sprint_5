import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import time  # Удалите, если не будете использовать time.sleep


@pytest.fixture(scope="session")
def driver():
    d = webdriver.Chrome()  # убедитесь, что chromedriver в PATH
    d.maximize_window()
    yield d
    d.quit()


@pytest.fixture(scope="module")
def page_url():
    return "https://stellarburgers.nomoreparties.site/"


class TestGoToTheBunsSection:

    def test_sauce_and_buns_scroll(self, driver, page_url):
        driver.get(page_url)

        # Проверяем наличие раздела конструктора бургеров
        constructor_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.CONSTRUCTOR_SECTION)
        )
        assert constructor_section.is_displayed(), "Раздел конструктора бургеров отсутствует"

        # Нажимаем на кнопку "Соусы"
        sauce_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCE_TAB)
        )
        sauce_tab.click()

        # Ожидание появления элемента внутри раздела Соусы
        spicy_x_sauce = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.SPICY_X_SAUCE)
        )
        assert spicy_x_sauce.is_displayed(
        ), "Элемент внутри раздела Соусы не найден после прокрутки"

        # Нажимаем на кнопку "Булки"
        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BUNS_TAB)
        )
        buns_tab.click()

        # Ожидание появления элемента внутри раздела Булки
        r2d3_bun = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.R2D3_BUN)
        )
        assert r2d3_bun.is_displayed(), "Элемент внутри раздела Булки не найден после прокрутки"
