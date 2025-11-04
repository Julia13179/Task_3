# Локаторы для страницы ленты заказов.

from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    # Локаторы страницы ленты заказов.
    
    ORDER_ITEM = (By.CLASS_NAME, "OrderHistory_listItem__")
    ORDER_MODAL = (By.CLASS_NAME, "Modal_modal__container__")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__']")
    
    # Счетчики
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[contains(@class, 'OrderFeed_title__') and contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(@class, 'OrderFeed_title__') and contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    
    # Заказы в работе
    IN_PROGRESS_SECTION = (By.XPATH, "//p[text()='В работе']/following-sibling::div")
    IN_PROGRESS_ORDER_NUMBER = (By.CLASS_NAME, "OrderFeed_number__")

