# Page Object для главной страницы.

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    # Page Object главной страницы Stellar Burgers.
    
    def __init__(self, driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
    
    def click_constructor(self):
        # Кликнуть на кнопку 'Конструктор'.
        self.click(self.locators.CONSTRUCTOR_BUTTON)
    
    def click_orders_feed(self):
        # Кликнуть на кнопку 'Лента заказов'.
        self.click(self.locators.ORDERS_FEED_BUTTON)
    
    def click_personal_account(self):
        # Кликнуть на кнопку 'Личный кабинет'.
        self.click(self.locators.PERSONAL_ACCOUNT_BUTTON)
    
    def click_ingredient(self, ingredient_type="bun"):
        # Кликнуть на ингредиент.
        if ingredient_type == "bun":
            self.click(self.locators.INGREDIENT_BUN)
        elif ingredient_type == "sauce":
            self.click(self.locators.INGREDIENT_SAUCE)
        elif ingredient_type == "filling":
            self.click(self.locators.INGREDIENT_FILLING)
    
    def is_ingredient_modal_opened(self):
        # Проверить, открыто ли модальное окно с деталями ингредиента.
        return self.is_element_visible(self.locators.INGREDIENT_DETAILS_MODAL)
    
    def close_ingredient_modal(self):
        # Закрыть модальное окно.
        self.click(self.locators.MODAL_CLOSE_BUTTON)
    
    def add_ingredient_to_constructor(self, ingredient_type="bun"):
        # Добавить ингредиент в конструктор.
        if ingredient_type == "bun":
            self.drag_and_drop(self.locators.INGREDIENT_BUN, self.locators.CONSTRUCTOR_AREA)
        elif ingredient_type == "sauce":
            self.drag_and_drop(self.locators.INGREDIENT_SAUCE, self.locators.CONSTRUCTOR_AREA)
        elif ingredient_type == "filling":
            self.drag_and_drop(self.locators.INGREDIENT_FILLING, self.locators.CONSTRUCTOR_AREA)
    
    def get_ingredient_counter(self, ingredient_type="bun"):
        # Получить счетчик ингредиента.
        if ingredient_type == "bun":
            element = self.find_element(self.locators.INGREDIENT_BUN)
        elif ingredient_type == "sauce":
            element = self.find_element(self.locators.INGREDIENT_SAUCE)
        elif ingredient_type == "filling":
            element = self.find_element(self.locators.INGREDIENT_FILLING)
        
        try:
            counter = element.find_element(*self.locators.INGREDIENT_COUNTER)
            return int(counter.text)
        except Exception:
            return 0
    
    def drag_and_drop(self, source_locator, target_locator):
        # Перетащить элемент.
        from selenium.webdriver.common.action_chains import ActionChains
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        ActionChains(self.driver).drag_and_drop(source, target).perform()
    
    def click_order_button(self):
        # Кликнуть на кнопку 'Оформить заказ'.
        self.click(self.locators.ORDER_BUTTON)
    
    def is_order_modal_opened(self):
        # Проверить, открыто ли модальное окно заказа.
        return self.is_element_visible(self.locators.ORDER_MODAL)
    
    def get_order_number(self, timeout=15):
        # Получить номер заказа.
        return self.get_text(self.locators.ORDER_NUMBER, timeout)

