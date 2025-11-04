# Тесты для восстановления пароля.

import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from config.web_config import PAGE_PATHS


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    # Тесты для восстановления пароля.
    
    @allure.story("Переход на страницу восстановления пароля")
    @allure.title("Переход на страницу восстановления пароля по кнопке")
    def test_go_to_password_recovery_page(self, driver):
        # Проверка перехода на страницу восстановления пароля.
        main_page = MainPage(driver)
        main_page.open(PAGE_PATHS["login"])
        
        login_page = LoginPage(driver)
        login_page.click_forgot_password_link()
        
        password_recovery_page = PasswordRecoveryPage(driver)
        assert password_recovery_page.is_element_visible(password_recovery_page.locators.EMAIL_INPUT), \
            "Страница восстановления пароля не открылась"
    
    @allure.story("Восстановление пароля")
    @allure.title("Ввод почты и клик по кнопке восстановить")
    def test_restore_password(self, driver):
        # Проверка ввода почты и клика по кнопке восстановить.
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open(PAGE_PATHS["forgot_password"])
        
        test_email = "test@example.com"
        password_recovery_page.enter_email(test_email)
        password_recovery_page.click_restore_button()
        
        assert password_recovery_page.is_element_visible(password_recovery_page.locators.PASSWORD_INPUT), \
            "Поле ввода пароля не появилось"
    
    @allure.story("Показ/скрытие пароля")
    @allure.title("Клик по кнопке показать/скрыть пароль подсвечивает поле")
    def test_show_password_button(self, driver):
        # Проверка, что клик по кнопке показать/скрыть пароль делает поле активным.
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open(PAGE_PATHS["reset_password"])
        
        password_recovery_page.click_show_password_button()
        
        assert password_recovery_page.is_password_field_active(), \
            "Поле пароля не стало активным после клика на кнопку показать/скрыть"

