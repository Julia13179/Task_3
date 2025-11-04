# Тесты для личного кабинета.

import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


@allure.feature("Личный кабинет")
class TestPersonalAccount:
    # Тесты для личного кабинета.
    
    @allure.story("Переход в личный кабинет")
    @allure.title("Переход по клику на личный кабинет")
    def test_go_to_personal_account(self, driver, test_user):
        # Проверка перехода по клику на 'Личный кабинет'.
        main_page = MainPage(driver)
        main_page.open()
        
        # Логинимся
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.login(test_user["email"], test_user["password"])
        
        # Переходим в личный кабинет
        main_page.click_personal_account()
        
        personal_account_page = PersonalAccountPage(driver)
        assert personal_account_page.is_on_profile_page(), \
            "Не удалось перейти в личный кабинет"
    
    @allure.story("История заказов")
    @allure.title("Переход в раздел история заказов")
    def test_go_to_orders_history(self, driver, test_user):
        # Проверка перехода в раздел 'История заказов'.
        main_page = MainPage(driver)
        main_page.open()
        
        # Логинимся
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.login(test_user["email"], test_user["password"])
        
        # Переходим в личный кабинет
        main_page.click_personal_account()
        
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_orders_history()
        
        assert personal_account_page.is_element_visible(personal_account_page.locators.ORDERS_HISTORY_BUTTON), \
            "Не удалось перейти в раздел 'История заказов'"
    
    @allure.story("Выход из аккаунта")
    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, test_user):
        # Проверка выхода из аккаунта.
        main_page = MainPage(driver)
        main_page.open()
        
        # Логинимся
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.login(test_user["email"], test_user["password"])
        
        # Переходим в личный кабинет
        main_page.click_personal_account()
        
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_logout()
        
        # Проверяем, что вернулись на страницу входа
        assert login_page.is_element_visible(login_page.locators.EMAIL_INPUT), \
            "Выход из аккаунта не выполнен"

