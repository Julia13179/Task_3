# Локаторы для страницы восстановления пароля.

from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    # Локаторы страницы восстановления пароля.
    
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")

