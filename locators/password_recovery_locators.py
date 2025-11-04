# Локаторы для страницы восстановления пароля.

from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    # Локаторы страницы восстановления пароля.
    
    EMAIL_INPUT = (By.XPATH, "//input[@type='email' or @name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' or @name='Пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, ".//div[@class='input__icon input__icon-action'] | //div[contains(@class, 'input__icon')]")
    # Локатор для проверки активного состояния поля (с подсветкой)
    ACTIVE_PASSWORD_FIELD = (By.XPATH, ".//div[contains(@class, 'input_status_active')] | .//div[contains(@class, 'input') and contains(@class, 'status_active')]")

