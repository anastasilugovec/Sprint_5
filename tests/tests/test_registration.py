from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_new_profile_registration(driver, page_url):
    # Переход на начальную страницу
    driver.get(page_url)

    # Ждем, пока кнопка личного кабинета станет кликабельной (максимум 5 секунд)
    account_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
    )
    # Кликаем по кнопке
    account_button.click()

    # Ждем, пока произойдет переход на страницу входа
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    # Проверяем, что мы действительно на странице входа
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Переход на страницу входа не произошел"

    # Находим и кликаем кнопку регистрации
    register_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
    )
    register_button.click()

    # Ждем, пока произойдет переход на страницу регистрации
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/register")
    )

    # Проверяем, что мы на странице регистрации
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/register", "Переход на страницу регистрации не произошел"

    # Заполняем поля формы регистрации
    name_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.NAME_FIELD)
    )
    name_field.send_keys("Тестовое Имя1")

    email_field = driver.find_element(*Locators.EMAIL_FIELD)
    email_field.send_keys("test30011@mail.com")

    password_field = driver.find_element(*Locators.PASSWORD_FIELD)
    password_field.send_keys("B1234567b1")

    # Нажимаем кнопку "Зарегистрироваться"
    submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
    submit_button.click()

    # Ждем, пока произойдет переход на страницу входа, после регистрации
    try:
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )
    except TimeoutException:
        print("Регистрация не прошла успешно")
        raise

    # Проверяем, что мы действительно перешли на страницу входа
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Регистрация прошла успешно"
