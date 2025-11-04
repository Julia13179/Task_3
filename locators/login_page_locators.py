# Локаторы для страницы входа.

from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Локаторы страницы входа.
    
    EMAIL_INPUT = (By.XPATH, "//input[@type='email' or @name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' or @name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

