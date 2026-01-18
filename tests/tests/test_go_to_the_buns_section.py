import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestIngredientsTabs:

    def test_switch_tabs_and_verify_active(self, driver, page_url):
        driver.get(page_url)

        # Проверка, что по умолчанию активен раздел "Булки" (или другой)
        active_buns_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_BUNS_TAB)
        )
        assert active_buns_tab.is_displayed(
        ), "Активная вкладка 'Булки' не отображается по умолчанию"

        # Проверка наличия элементов в активной вкладке
        buns_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.BUNS_CONTAINER)
        )
        assert buns_container.is_displayed(), "Контейнер с булками не отображается"

        # Переход к разделу "Соусы"
        sauce_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCE_TAB)
        )
        sauce_tab.click()

        # Проверка смены активного таба
        active_sauce_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SAUCE_TAB)
        )
        assert active_sauce_tab.is_displayed(), "Таб 'Соусы' не стал активным после клика"

        # Проверка наличия элементов внутри раздела "Соусы"
        spicy_x_sauce = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.SPICY_X_SAUCE)
        )
        assert spicy_x_sauce.is_displayed(), "Элемент внутри раздела 'Соусы' не найден"

        # Аналогично для раздела "Начинки"
        # Можно повторить для другого раздела, если нужно
