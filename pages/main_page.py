# Page Object для главной страницы.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop as seletools_drag_and_drop
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    # Page Object главной страницы Stellar Burgers.
    
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
        
        # Ждем перехода на страницу личного кабинета
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda d: "/account" in d.current_url or "/login" in d.current_url)
    
    def click_ingredient(self, ingredient_type="bun"):
        # Кликнуть на ингредиент.
        if ingredient_type == "bun":
            self.click(self.locators.INGREDIENT_BUN)
        elif ingredient_type == "sauce":
            self.click(self.locators.INGREDIENT_SAUCE)
        elif ingredient_type == "filling":
            self.click(self.locators.INGREDIENT_FILLING)
    
    def is_ingredient_modal_opened(self, timeout=10):
        # Проверить, открыто ли модальное окно с деталями ингредиента.
        return self.is_element_visible(self.locators.INGREDIENT_DETAILS_MODAL, timeout=timeout)
    
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
        # Определяем локатор ингредиента
        if ingredient_type == "bun":
            ingredient_locator = self.locators.INGREDIENT_BUN
        elif ingredient_type == "sauce":
            ingredient_locator = self.locators.INGREDIENT_SAUCE
        elif ingredient_type == "filling":
            ingredient_locator = self.locators.INGREDIENT_FILLING
        else:
            return 0

        try:
            # Находим элемент ингредиента через WebDriverWait
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.presence_of_element_located(ingredient_locator))
            
            # Ищем счетчик внутри элемента ингредиента
            counters = element.find_elements(By.XPATH, ".//p[contains(@class, 'counter_counter__num')] | .//p[contains(@class, 'counter') and contains(@class, 'num')] | .//div[contains(@class, 'counter')]//p")
            if counters:
                text = counters[0].text.strip()
                return int(text) if text else 0
            
            return 0
        except Exception:
            return 0
    
    def drag_and_drop(self, source_locator, target_locator):
        # Перетащить элемент в конструктор.
        # Ждем видимости элементов перед drag and drop
        wait = WebDriverWait(self.driver, 10)
        source = wait.until(EC.visibility_of_element_located(source_locator))
        target = wait.until(EC.visibility_of_element_located(target_locator))
        
        # Используем seletools для drag and drop (работает с React DnD в обоих браузерах)
        seletools_drag_and_drop(self.driver, source, target)
    
    def click_order_button(self):
        # Кликнуть на кнопку 'Оформить заказ'.
        self.click(self.locators.ORDER_BUTTON)
        
        # Ждем появления модального окна заказа и текста "готовить" (подтверждение создания заказа)
        wait = WebDriverWait(self.driver, 15)
        wait.until(
            lambda d: EC.presence_of_element_located(self.locators.ORDER_MODAL)(d) and
            ("готовить" in d.page_source.lower() or "готовят" in d.page_source.lower())
        )
    
    def is_order_modal_opened(self):
        # Проверить, открыто ли модальное окно заказа.
        return self.is_element_visible(self.locators.ORDER_MODAL)
    
    def get_order_number(self, timeout=15):
        # Получить номер заказа.
        return self.get_text(self.locators.ORDER_NUMBER, timeout)

