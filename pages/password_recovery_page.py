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
        # Кликаем на иконку показать/скрыть пароль
        self.click(self.locators.SHOW_PASSWORD_BUTTON)
    
    def is_password_field_active(self):
        # Проверить, активено ли поле пароля (подсвечено).
        # Проверяем наличие элемента с классом input_status_active (подсвеченное поле)
        return self.is_element_visible(self.locators.ACTIVE_PASSWORD_FIELD)

