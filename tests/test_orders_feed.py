# Тесты для ленты заказов.

import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.orders_feed_page import OrdersFeedPage
from pages.personal_account_page import PersonalAccountPage
from config.web_config import PAGE_PATHS
from tests.helpers import login_user, create_order


@allure.feature("Лента заказов")
class TestOrdersFeed:
    # Тесты для ленты заказов.
    
    @allure.story("Детали заказа")
    @allure.title("Клик на заказ открывает модальное окно")
    def test_order_modal_opens(self, driver):
        # Проверка, что клик на заказ открывает модальное окно с деталями.
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open(PAGE_PATHS["feed"])
        
        orders_feed_page.click_order(0)
        
        assert orders_feed_page.is_order_modal_opened(), \
            "Модальное окно с деталями заказа не открылось"
    
    @allure.story("История заказов")
    @allure.title("Заказы из истории отображаются в ленте")
    def test_orders_from_history_in_feed(self, driver, test_user):
        # Проверка, что заказы пользователя из истории отображаются в ленте заказов.
        main_page = MainPage(driver)
        main_page.open()
        
        # Логинимся
        login_user(driver, test_user["email"], test_user["password"])
        
        # Переходим в историю заказов
        main_page.click_personal_account()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.wait_for_element_to_be_visible(personal_account_page.locators.ORDERS_HISTORY_BUTTON)
        personal_account_page.click_orders_history()
        
        # Ждем загрузки истории заказов
        personal_account_page.wait_for_element_to_be_visible(personal_account_page.locators.ORDERS_HISTORY_BUTTON, timeout=5)
        
        # Переходим в ленту заказов
        main_page.click_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.wait_for_element_to_be_visible(orders_feed_page.locators.ORDER_ITEM, timeout=5)
        
        assert orders_feed_page.is_element_visible(orders_feed_page.locators.ORDER_ITEM), \
            "Заказы не отображаются в ленте"
    
    @allure.story("Счетчики заказов")
    @allure.title("Счетчик выполнено за все время увеличивается")
    def test_total_orders_counter_increases(self, driver, test_user):
        # Проверка, что счетчик 'Выполнено за все время' увеличивается при создании заказа.
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open(PAGE_PATHS["feed"])
        
        initial_count = orders_feed_page.get_total_orders_count()
        
        # Создаем заказ
        main_page = MainPage(driver)
        login_user(driver, test_user["email"], test_user["password"])
        
        create_order(driver, main_page)
        
        # Ждем закрытия модального окна заказа
        main_page.wait_for_element_to_disappear(main_page.locators.ORDER_MODAL, timeout=15)
        
        # Проверяем счетчик
        orders_feed_page.open(PAGE_PATHS["feed"])
        orders_feed_page.wait_for_element_to_be_visible(orders_feed_page.locators.TOTAL_ORDERS_COUNT, timeout=5)
        new_count = orders_feed_page.get_total_orders_count()
        
        assert new_count >= initial_count, \
            "Счетчик 'Выполнено за все время' не увеличился"
    
    @allure.story("Счетчики заказов")
    @allure.title("Счетчик выполнено за сегодня увеличивается")
    def test_today_orders_counter_increases(self, driver, test_user):
        # Проверка, что счетчик 'Выполнено за сегодня' увеличивается при создании заказа.
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open(PAGE_PATHS["feed"])
        
        initial_count = orders_feed_page.get_today_orders_count()
        
        # Создаем заказ
        main_page = MainPage(driver)
        login_user(driver, test_user["email"], test_user["password"])
        
        create_order(driver, main_page)
        
        # Ждем закрытия модального окна заказа
        main_page.wait_for_element_to_disappear(main_page.locators.ORDER_MODAL, timeout=15)
        
        # Проверяем счетчик
        orders_feed_page.open(PAGE_PATHS["feed"])
        orders_feed_page.wait_for_element_to_be_visible(orders_feed_page.locators.TODAY_ORDERS_COUNT, timeout=5)
        new_count = orders_feed_page.get_today_orders_count()
        
        assert new_count >= initial_count, \
            "Счетчик 'Выполнено за сегодня' не увеличился"
    
    @allure.story("Заказы в работе")
    @allure.title("Номер заказа появляется в разделе в работе")
    def test_order_in_progress(self, driver, test_user):
        # Проверка, что номер заказа появляется в разделе 'В работе' после оформления.
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open(PAGE_PATHS["feed"])
        
        # Создаем заказ
        main_page = MainPage(driver)
        login_user(driver, test_user["email"], test_user["password"])
        
        create_order(driver, main_page)
        
        # Получаем номер заказа
        main_page.wait_for_element_to_be_visible(main_page.locators.ORDER_NUMBER, timeout=15)
        order_number_text = main_page.get_order_number(timeout=5)
        order_number = int(''.join(filter(str.isdigit, order_number_text)))
        
        # Закрываем модальное окно
        main_page.close_ingredient_modal()
        
        # Проверяем в разделе "В работе"
        orders_feed_page.open(PAGE_PATHS["feed"])
        orders_feed_page.wait_for_element_to_be_visible(orders_feed_page.locators.IN_PROGRESS_SECTION, timeout=5)
        
        assert orders_feed_page.is_order_in_progress(order_number), \
            f"Заказ {order_number} не появился в разделе 'В работе'"

