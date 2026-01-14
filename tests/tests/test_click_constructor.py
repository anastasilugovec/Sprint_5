import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


@pytest.fixture(scope="session")
def driver():
    d = webdriver.Chrome()  # убедитесь, что chromedriver в PATH
    yield d
    d.quit()


@pytest.fixture(scope="module")
def page_url():
    return "https://stellarburgers.nomoreparties.site/"


class TestClickConstructor:
    def test_click_constructor(self, driver, page_url):
        driver.get(page_url)

        # Заполняем поля логина
        email_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.EMAIL_FIELD)
        )
        email_field.send_keys("test30011@mail.com")

        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys("B1234567b1")

        # Нажимаем на кнопку "Войти"
        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        # Ожидаем, что произойдет переход на страницу
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )

        # Проверяем, что перешли на главную страницу
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

        # Кликаем на кнопку "Личный кабинет"
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # Ожидаем переход на страницу профиля
        WebDriverWait(driver, 10).until(
            EC.url_to_be(
                "https://stellarburgers.nomoreparties.site/account/profile")
        )

        # Проверяем, что перешли на страницу профиля
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

        # Кликаем на ссылку "Конструктор"
        constructor_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_LINK)
        )
        constructor_link.click()

        # Ожидаем возвращения на главную страницу
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )

        # Проверяем, что перешли на главную страницу
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
