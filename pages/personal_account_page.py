# Page Object для страницы личного кабинета.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators


class PersonalAccountPage(BasePage):
    # Page Object страницы личного кабинета.
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PersonalAccountLocators()
    
    def click_orders_history(self):
        # Кликнуть на раздел 'История заказов'.
        self.click(self.locators.ORDERS_HISTORY_BUTTON)
    
    def click_profile(self):
        # Кликнуть на раздел 'Профиль'.
        self.click(self.locators.PROFILE_BUTTON)
    
    def click_logout(self):
        # Кликнуть на кнопку 'Выход'.
        self.click(self.locators.LOGOUT_BUTTON)
    
    def is_on_profile_page(self):
        # Проверить, что находимся на странице профиля.
        # Проверяем URL или наличие элемента "Профиль"
        wait = WebDriverWait(self.driver, 10)
        try:
            # Проверяем URL
            if "/account" in self.driver.current_url:
                return True
            
            # Проверяем наличие элемента "Профиль"
            element = wait.until(EC.presence_of_element_located(self.locators.PROFILE_BUTTON))
            return element is not None and element.is_displayed()
        except:
            return False

