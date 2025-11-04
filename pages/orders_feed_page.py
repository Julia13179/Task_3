# Page Object для страницы ленты заказов.

from pages.base_page import BasePage
from locators.orders_feed_locators import OrdersFeedLocators


class OrdersFeedPage(BasePage):
    # Page Object страницы ленты заказов.
    
    def __init__(self, driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrdersFeedLocators()
    
    def click_order(self, order_index=0):
        # Кликнуть на заказ.
        orders = self.find_elements(self.locators.ORDER_ITEM)
        if orders:
            orders[order_index].click()
    
    def is_order_modal_opened(self):
        # Проверить, открыто ли модальное окно заказа.
        return self.is_element_visible(self.locators.ORDER_MODAL)
    
    def close_order_modal(self):
        # Закрыть модальное окно заказа.
        self.click(self.locators.MODAL_CLOSE_BUTTON)
    
    def get_total_orders_count(self):
        # Получить счетчик 'Выполнено за все время'.
        return int(self.get_text(self.locators.TOTAL_ORDERS_COUNT))
    
    def get_today_orders_count(self):
        # Получить счетчик 'Выполнено за сегодня'.
        return int(self.get_text(self.locators.TODAY_ORDERS_COUNT))
    
    def get_in_progress_orders(self):
        # Получить список номеров заказов в работе.
        try:
            elements = self.find_elements(self.locators.IN_PROGRESS_ORDER_NUMBER, timeout=5)
            return [int(elem.text) for elem in elements if elem.text.strip()]
        except Exception:
            return []
    
    def is_order_in_progress(self, order_number):
        # Проверить, есть ли заказ в разделе 'В работе'.
        orders = self.get_in_progress_orders()
        return order_number in orders

