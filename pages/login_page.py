# Page Object для страницы входа.

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    # Page Object страницы входа.
    
    def __init__(self, driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()
    
    def enter_email(self, email):
        # Ввести email.
        self.send_keys(self.locators.EMAIL_INPUT, email)
    
    def enter_password(self, password):
        # Ввести пароль.
        self.send_keys(self.locators.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        # Кликнуть на кнопку 'Войти'.
        self.click(self.locators.LOGIN_BUTTON)
    
    def click_register_link(self):
        # Кликнуть на ссылку 'Зарегистрироваться'.
        self.click(self.locators.REGISTER_LINK)
    
    def click_forgot_password_link(self):
        # Кликнуть на ссылку 'Восстановить пароль'.
        self.click(self.locators.FORGOT_PASSWORD_LINK)
    
    def login(self, email, password):
        # Выполнить вход.
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

