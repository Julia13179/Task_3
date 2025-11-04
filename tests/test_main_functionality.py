# Тесты основного функционала.

import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.orders_feed_page import OrdersFeedPage
from config.web_config import PAGE_PATHS


@allure.feature("Основной функционал")
class TestMainFunctionality:
    # Тесты основного функционала.
    
    @allure.story("Навигация")
    @allure.title("Переход по клику на конструктор")
    def test_go_to_constructor(self, driver):
        # Проверка перехода по клику на 'Конструктор'.
        main_page = MainPage(driver)
        main_page.open(PAGE_PATHS["feed"])
        
        main_page.click_constructor()
        
        assert main_page.is_element_visible(main_page.locators.CONSTRUCTOR_AREA), \
            "Не удалось перейти в конструктор"
    
    @allure.story("Навигация")
    @allure.title("Переход по клику на ленту заказов")
    def test_go_to_orders_feed(self, driver):
        # Проверка перехода по клику на 'Лента заказов'.
        main_page = MainPage(driver)
        main_page.open()
        
        main_page.click_orders_feed()
        
        orders_feed_page = OrdersFeedPage(driver)
        assert orders_feed_page.is_element_visible(orders_feed_page.locators.ORDER_ITEM), \
            "Не удалось перейти в ленту заказов"
    
    @allure.story("Ингредиенты")
    @allure.title("Клик на ингредиент открывает модальное окно")
    def test_ingredient_modal_opens(self, driver):
        # Проверка, что клик на ингредиент открывает модальное окно с деталями.
        main_page = MainPage(driver)
        main_page.open()
        
        main_page.click_ingredient("bun")
        
        assert main_page.is_ingredient_modal_opened(), \
            "Модальное окно с деталями ингредиента не открылось"
    
    @allure.story("Ингредиенты")
    @allure.title("Модальное окно закрывается по клику на крестик")
    def test_ingredient_modal_closes(self, driver):
        # Проверка, что модальное окно закрывается по клику на крестик.
        main_page = MainPage(driver)
        main_page.open()
        
        main_page.click_ingredient("bun")
        main_page.close_ingredient_modal()
        
        assert not main_page.is_ingredient_modal_opened(), \
            "Модальное окно не закрылось"
    
    @allure.story("Конструктор")
    @allure.title("Счетчик ингредиента увеличивается при добавлении")
    def test_ingredient_counter_increases(self, driver):
        # Проверка, что счетчик ингредиента увеличивается при добавлении в заказ.
        main_page = MainPage(driver)
        main_page.open()
        
        initial_count = main_page.get_ingredient_counter("bun")
        
        main_page.add_ingredient_to_constructor("bun")
        
        new_count = main_page.get_ingredient_counter("bun")
        assert new_count > initial_count, \
            "Счетчик ингредиента не увеличился"
    
    @allure.story("Заказ")
    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_create_order(self, driver, test_user):
        # Проверка, что залогиненный пользователь может оформить заказ.
        main_page = MainPage(driver)
        main_page.open()
        
        # Логинимся
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.login(test_user["email"], test_user["password"])
        
        # Добавляем ингредиенты и оформляем заказ
        main_page.open()
        main_page.add_ingredient_to_constructor("bun")
        main_page.add_ingredient_to_constructor("sauce")
        main_page.click_order_button()
        
        assert main_page.is_order_modal_opened(), \
            "Заказ не был оформлен"

