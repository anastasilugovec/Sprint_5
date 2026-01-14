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


class TestAuthorizationViaPersonalAccount:
    def test_login_button(self, driver, page_url):
        driver.get(page_url)

        # Ожидание, пока кнопка "Войти в аккаунт" станет кликабельной
        login_account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGIN_ACCOUNT_BUTTON)
        )
        login_account_button.click()

        # Проверяем переход на страницу логина
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        # Заполнение логина
        driver.find_element(By.ID, "email").send_keys("test3700@yandex.com")

        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys("B1234567b1")

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        # Проверяем переход на главную страницу
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

        # Переходим в Личный кабинет
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # Проверяем страницу профиля
        WebDriverWait(driver, 5).until(
            EC.url_to_be(
                "https://stellarburgers.nomoreparties.site/account/profile")
        )
