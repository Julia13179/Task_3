# Локаторы для страницы личного кабинета.

from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    # Локаторы страницы личного кабинета.
    
    ORDERS_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

