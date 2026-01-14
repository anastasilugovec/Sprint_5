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


class TestGoToTheToppingsSection:
    def test_go_to_the_toppings_section(self, driver, page_url):
        driver.get(page_url)

        # Проверяем наличие раздела конструктора бургеров
        constructor_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.CONSTRUCTOR_SECTION)
        )
        assert constructor_section.is_displayed(), "Раздел конструктора бургеров отсутствует"

        # Запоминаем текущую позицию скролла перед нажатием
        initial_scroll_position = driver.execute_script(
            "return window.scrollY;")

        # Нажимаем на кнопку "Начинки"
        fillings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.FILLINGS_TAB)
        )
        fillings_tab.click()

        # Ждем, пока скролл достигнет новой позиции
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script(
                "return window.scrollY;") > initial_scroll_position
        )

        # Проверяем, что элемент "Мясо бессмертных моллюсков Protostomia" появился и отображается
        protostomia_meat = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.PROTOSTOMIA_MEAT)
        )
        assert protostomia_meat.is_displayed(), "Скролл до раздела 'Начинки' не произошел"
