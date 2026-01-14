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


class TestPasswordRecovery:
    def test_password_recovery(self, driver, page_url):
        driver.get(page_url)

        # Ждем, пока ссылка "Восстановить пароль" не станет видимой, максимум 5 секунд
        forgot_password_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.FORGOT_PASSWORD_LINK)
        )

        # Кликаем на ссылку "Восстановить пароль"
        forgot_password_link.click()

        # Ожидаем перехода на страницу восстановления пароля
        WebDriverWait(driver, 5).until(
            EC.url_to_be(
                "https://stellarburgers.nomoreparties.site/forgot-password")
        )

        # Проверяем, что мы действительно на странице восстановления пароля
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/forgot-password", "Переход на страницу восстановления пароля не произошел"

        # Нажимаем на ссылку "Войти" на странице восстановления пароля
        login_from_forgot_password_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGIN_FROM_REGISTER_LINK)
        )
        login_from_forgot_password_link.click()

        # Ожидаем перехода на страницу логина
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )

        # Проверяем, что мы на странице логина
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Переход на страницу логина не произошел"

        # Заполняем поля логина
        email_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.EMAIL_FIELD)
        )
        email_field.send_keys("test30011@mail.com")

        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys("B1234567b1")

        # Нажимаем кнопку "Войти"
        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        # Ожидаем перехода на главную страницу
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )

        # Проверяем, что мы на главной странице
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Переход на главную страницу не произошел"
