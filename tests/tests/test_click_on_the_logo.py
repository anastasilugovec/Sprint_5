import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver


class TestClickOnTheLogo:
    def test_profile_to_logo(self, driver, page_url):
        driver.get(page_url)

        # Заполняем поля логина
        email_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.EMAIL_FIELD)
        )
        email_field.send_keys("test30011@mail.com")

        password_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.PASSWORD_FIELD)
        )
        password_field.send_keys("B1234567b1")

        # Нажимаем на кнопку "Войти"
        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        )
        login_button.click()

        # Ожидание перехода на главную страницу
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/", \
            "Переход на главную страницу не произошел"

        # Кликаем на кнопку "Личный кабинет"
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # Проверяем переход на страницу профиля
        WebDriverWait(driver, 5).until(
            EC.url_to_be(
                "https://stellarburgers.nomoreparties.site/account/profile")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile", \
            "Переход на страницу профиля не произошел"

        # Кликаем на логотип
        logo_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGO_LINK)
        )
        logo_link.click()

        # Проверяем переход на главную страницу
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/", \
            "Переход на главную страницу не произошел после нажатия на логотип"
