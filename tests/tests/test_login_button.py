import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver


class TestLoginButtom:
    def test_login_button(driver, page_url):
        # Переход на стартовую страницу
    driver.get(page_url)

    # Ждем, пока кнопка "Войти в аккаунт" станет кликабельной (максимум 5 секунд)
    login_account_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.LOGIN_ACCOUNT_BUTTON)
    )

    # Кликаем на кнопку "Войти в аккаунт"
    login_account_button.click()

    # Ждем, пока произойдет переход на страницу логина
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    # Проверяем, что мы действительно на странице логина
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Переход на страницу логина не произошел"

    # Заполняем поле email
    email_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.EMAIL_FIELD)
    )
    email_field.send_keys("test30011@mail.com")

    # Заполняем поле пароля
    password_field = driver.find_element(*Locators.PASSWORD_FIELD)
    password_field.send_keys("B1234567b1")

    # Нажимаем кнопку "Войти"
    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    login_button.click()

    # Ждем, пока произойдет переход на главную страницу
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    # Проверяем, что мы действительно на главной странице
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Переход на главную страницу не произошел"

    # Кликаем на кнопку "Личный кабинет"
    account_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
    )
    account_button.click()

    # Ждем, пока произойдет переход на страницу профиля
    WebDriverWait(driver, 5).until(
        EC.url_to_be(
            "https://stellarburgers.nomoreparties.site/account/profile")
    )

    # Проверяем, что мы на странице профиля
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile", "Переход на страницу профиля не произошел"
