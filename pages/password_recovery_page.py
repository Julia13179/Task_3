# Page Object для страницы восстановления пароля.

from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators


class PasswordRecoveryPage(BasePage):
    # Page Object страницы восстановления пароля.
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PasswordRecoveryLocators()
    
    def enter_email(self, email):
        # Ввести email.
        self.send_keys(self.locators.EMAIL_INPUT, email)
    
    def click_restore_button(self):
        # Кликнуть на кнопку 'Восстановить'.
        self.click(self.locators.RESTORE_BUTTON)
    
    def click_show_password_button(self):
        # Кликнуть на кнопку показать/скрыть пароль.
        self.click(self.locators.SHOW_PASSWORD_BUTTON)
    
    def is_password_field_active(self):
        # Проверить, активено ли поле пароля (подсвечено).
        element = self.find_element(self.locators.PASSWORD_INPUT)
        classes = element.get_attribute("class")
        return "input_status_active" in classes and "input__status_error" not in classes

