# Локаторы для страницы ленты заказов.

from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    # Локаторы страницы ленты заказов.
    
    ORDER_ITEM = (By.XPATH, "//*[contains(@class, 'OrderHistory')] | //li[contains(@class, 'OrderHistory')]")
    ORDER_MODAL = (By.XPATH, "//*[contains(@class, 'Modal') and contains(@class, 'container')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal') and contains(@class, 'close')] | //button[@aria-label='Закрыть'] | //button[contains(@class, 'close')]")
    
    # Счетчики
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p | //p[contains(text(), 'Выполнено за все время')]/parent::*/p[last()]")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p | //p[contains(text(), 'Выполнено за сегодня')]/parent::*/p[last()]")
    
    # Заказы в работе
    IN_PROGRESS_SECTION = (By.XPATH, "//p[contains(text(), 'В работе')]/following-sibling::div | //*[contains(@class, 'OrderFeed')]//*[contains(text(), 'В работе')]/following-sibling::div")
    IN_PROGRESS_ORDER_NUMBER = (By.XPATH, "//*[contains(@class, 'OrderFeed')]//*[contains(@class, 'number')] | //*[contains(@class, 'OrderFeed')]//p[contains(@class, 'digits')]")

