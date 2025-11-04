# Page Object для страницы ленты заказов.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.orders_feed_locators import OrdersFeedLocators


class OrdersFeedPage(BasePage):
    # Page Object страницы ленты заказов.
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrdersFeedLocators()
    
    def click_order(self, order_index=0):
        # Кликнуть на заказ.
        orders = self.find_elements(self.locators.ORDER_ITEM)
        if orders and order_index < len(orders):
            # Скроллим к элементу и кликаем
            self.driver.execute_script("arguments[0].scrollIntoView(true);", orders[order_index])
            try:
                orders[order_index].click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", orders[order_index])
            
            # Ждем либо перехода на /feed/{order_id}, либо появления модального окна
            wait = WebDriverWait(self.driver, 10)
            wait.until(lambda d: "/feed/" in d.current_url and d.current_url != self.base_url + "/feed" or 
                      EC.presence_of_element_located(self.locators.ORDER_MODAL)(d))
    
    def is_order_modal_opened(self):
        # Проверить, открыто ли модальное окно заказа.
        # На странице /feed/{order_id} модальное окно может быть всегда видимым
        wait = WebDriverWait(self.driver, 5)
        try:
            # Проверяем наличие модального окна или переход на страницу деталей заказа
            if "/feed/" in self.driver.current_url and self.driver.current_url != self.base_url + "/feed":
                # На странице деталей заказа модальное окно должно быть видимым
                wait.until(EC.presence_of_element_located(self.locators.ORDER_MODAL))
                return True
            else:
                # На странице ленты проверяем видимость модального окна
                return self.is_element_visible(self.locators.ORDER_MODAL, timeout=5)
        except:
            return False
    
    def close_order_modal(self):
        # Закрыть модальное окно заказа.
        self.click(self.locators.MODAL_CLOSE_BUTTON)
        # Ждем закрытия модального окна
        self.wait_for_element_to_disappear(self.locators.ORDER_MODAL)
    
    def get_total_orders_count(self):
        # Получить счетчик 'Выполнено за все время'.
        try:
            text = self.get_text(self.locators.TOTAL_ORDERS_COUNT, timeout=5)
            return int(text) if text else 0
        except Exception:
            return 0
    
    def get_today_orders_count(self):
        # Получить счетчик 'Выполнено за сегодня'.
        try:
            text = self.get_text(self.locators.TODAY_ORDERS_COUNT, timeout=5)
            return int(text) if text else 0
        except Exception:
            return 0
    
    def get_in_progress_orders(self):
        # Получить список номеров заказов в работе.
        try:
            # Ищем заказы в разделе "В работе" напрямую
            # Используем более широкий поиск, чтобы найти все возможные номера заказов
            order_elements = self.driver.find_elements(By.XPATH, 
                "//*[contains(@class, 'OrderFeed')]//*[contains(@class, 'number')] | "
                "//*[contains(@class, 'OrderFeed')]//p[contains(@class, 'digits')] | "
                "//*[contains(text(), 'В работе')]/following::*[contains(@class, 'number')] | "
                "//*[contains(text(), 'В работе')]/following::p[contains(@class, 'digits')]"
            )
            
            orders = []
            for elem in order_elements:
                text = elem.text.strip()
                if text:
                    try:
                        order_num = int(''.join(filter(str.isdigit, text)))
                        if order_num > 0:
                            orders.append(order_num)
                    except:
                        pass
            
            return orders
        except Exception:
            return []
    
    def is_order_in_progress(self, order_number):
        # Проверить, есть ли заказ в разделе 'В работе'.
        orders = self.get_in_progress_orders()
        return order_number in orders

