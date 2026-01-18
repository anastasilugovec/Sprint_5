import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver


class TestAuthorizationViaPersonalAccount:
    def test_login_button(self, driver, page_url):
        driver.get(page_url)

        # Ожидание, пока кнопка "Войти в аккаунт" станет кликабельной
        login_account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGIN_ACCOUNT_BUTTON)
        )
        # Проверка, что кнопка отображается
        assert login_account_button.is_displayed(
        ), "Кнопка 'Войти в аккаунт' не отображается"
        login_account_button.click()

        # Проверяем переход на страницу логина
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Некорректный URL после перехода на страницу логина"

        # Заполнение логина
        email_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(*Locators.EMAIL_FIELD)
        )
        assert email_field.is_displayed(), "Поле email не отображается"
        email_field.send_keys("test3700@yandex.com")

        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        assert password_field.is_displayed(), "Поле пароля не отображается"
        password_field.send_keys("B1234567b1")

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        assert login_button.is_displayed(), "Кнопка входа не отображается"
        login_button.click()

        # Проверяем переход на главную страницу
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Не удалось перейти на главную страницу"

        # Переходим в Личный кабинет
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(*Locators.ACCOUNT_BUTTON)
        )
        assert account_button.is_displayed(), "Кнопка 'Личный кабинет' не отображается"
        account_button.click()

        # Проверяем страницу профиля
        WebDriverWait(driver, 5).until(
            EC.url_to_be(
                "https://stellarburgers.nomoreparties.site/account/profile")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile", "Некорректный URL профиля"
