# Локаторы для страницы личного кабинета.

from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    # Локаторы страницы личного кабинета.
    
    ORDERS_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(), 'История')] | //a[contains(text(), 'заказов')] | //a[contains(@href, 'order-history')]")
    PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль'] | //a[contains(text(), 'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

