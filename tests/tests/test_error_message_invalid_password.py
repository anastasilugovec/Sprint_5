import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestErrorMessageInvalidPassword:
    def test_error_message_invalid_password(self, driver, page_url):
        driver.get(page_url)

        # Заполняем поля формы регистрации
        name_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.NAME_FIELD)
        )
        name_field.send_keys("Тестовое Имя")

        email_field = driver.find_element(*Locators.EMAIL_FIELD)
        email_field.send_keys("test3002@mail.com")

        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys("1234")  # Неполный пароль

        # Нажимаем на кнопку "Зарегистрироваться"
        submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
        submit_button.click()

        # Явное ожидание появления сообщения об ошибке
        error_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                Locators.ERROR_MESSAGE_INVALID_PASSWORD)
        )

        # Атомарная проверка текста сообщения
        expected_error_message = "Некорректный пароль"
        actual_error_message = error_element.text
        assert actual_error_message == expected_error_message, (
            f"Ожидаемое сообщение: '{expected_error_message}', "
            f"Фактическое сообщение: '{actual_error_message}'"
        )

        # Проверка, что URL остался прежним (не перешли на страницу логина)
        assert driver.current_url != "https://stellarburgers.nomoreparties.site/login", (
            f"Ожидаемое: не переходить на страницу 'https://stellarburgers.nomoreparties.site/login', "
            f"Фактическое: '{driver.current_url}'"
        )
