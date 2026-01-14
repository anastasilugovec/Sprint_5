import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
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


class TestLogout:
    def test_logout(self, driver, page_url):
        driver.get(page_url)

        # Клик на кнопку "Личный кабинет"
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )
        account_button.click()

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

        # Проверяем, что перешли на главную страницу
        try:
            WebDriverWait(driver, 5).until(EC.url_to_be(page_url))
        except TimeoutException:
            assert False, f"Переход на главную страницу не произошел после авторизации. Текущий URL: {driver.current_url}"

        # Кликаем на кнопку "Личный кабинет" повторно
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # Проверяем, что перешли на страницу профиля
        try:
            WebDriverWait(driver, 5).until(
                EC.url_to_be(
                    "https://stellarburgers.nomoreparties.site/account/profile")
            )
        except TimeoutException:
            assert False, f"Переход на страницу профиля не произошел. Текущий URL: {driver.current_url}"

        # Нажимаем на кнопку "Выход"
        logout_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        )
        logout_button.click()

        # Проверяем, что перешли на страницу логина после выхода
        try:
            WebDriverWait(driver, 5).until(
                EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
            )
        except TimeoutException:
            assert False, "Переход на страницу логина не произошел после выхода."
