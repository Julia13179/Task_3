# Фикстуры для веб-тестов.

import pytest
from config.driver_factory import DriverFactory
from config.api_helper import create_user, delete_user, create_email


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    # Фикстура для создания драйвера браузера.
    # Использует параметризацию pytest для запуска тестов в обоих браузерах.
    # Каждый тест автоматически выполнится один раз в Chrome и один раз в Firefox.
    browser_name = request.param
    driver = DriverFactory.create_driver(browser_name)

    yield driver

    driver.quit()


@pytest.fixture
def test_user():
    # Фикстура для создания тестового пользователя.
    email = create_email()
    password = "test_password123"
    name = "Test User"

    # Создаем пользователя через API
    response = create_user(email, password, name)
    access_token = None

    if response.status_code == 200:
        response_data = response.json()
        if response_data.get("success"):
            access_token = response_data.get("accessToken")
        else:
            raise ValueError(f"Не удалось создать пользователя: {response_data}")
    else:
        raise ValueError(f"Ошибка создания пользователя: {response.status_code}, {response.text}")

    user_data = {
        "email": email,
        "password": password,
        "name": name,
        "access_token": access_token
    }

    yield user_data

    # Удаляем пользователя после теста
    if access_token:
        try:
            delete_user(access_token)
        except Exception as e:
            # Логируем ошибку, но не падаем
            print(f"Не удалось удалить пользователя: {e}")
