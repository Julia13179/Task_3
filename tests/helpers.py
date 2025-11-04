# Вспомогательные функции для тестов.

from pages.main_page import MainPage
from pages.login_page import LoginPage


def login_user(driver, email, password):
    # Вспомогательная функция для логина пользователя.
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_personal_account()
    login_page = LoginPage(driver)
    login_page.login(email, password)


def create_order(driver, main_page):
    # Вспомогательная функция для создания заказа.
    main_page.open()
    main_page.add_ingredient_to_constructor("bun")
    main_page.add_ingredient_to_constructor("sauce")
    main_page.click_order_button()

