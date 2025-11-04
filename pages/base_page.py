# Базовый класс для всех Page Objects.

import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logger = logging.getLogger(__name__)


class BasePage:
    # Базовый класс для всех страниц.
    
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.education-services.ru"
    
    def open(self, path=""):
        # Открыть страницу.
        url = f"{self.base_url}{path}"
        self.driver.get(url)
    
    def find_element(self, locator, timeout=10):
        # Найти элемент с ожиданием.
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException as e:
            logger.error(f"Элемент не найден за {timeout} секунд: {locator}")
            logger.error(f"Текущий URL: {self.driver.current_url}")
            raise
    
    def find_elements(self, locator, timeout=10):
        # Найти элементы с ожиданием.
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)
    
    def click(self, locator, timeout=10):
        # Кликнуть по элементу.
        try:
            # Сначала ждем видимости элемента
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            # Затем скроллим к элементу
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            # Ждем кликабельности
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            # Пробуем обычный клик
            try:
                element.click()
            except Exception:
                # Если не получилось, пробуем через JS
                self.driver.execute_script("arguments[0].click();", element)
        except TimeoutException as e:
            logger.error(f"Элемент не кликабелен за {timeout} секунд: {locator}")
            logger.error(f"Текущий URL: {self.driver.current_url}")
            raise
    
    def send_keys(self, locator, text, timeout=10):
        # Ввести текст в поле.
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator, timeout=10):
        # Получить текст элемента.
        element = self.find_element(locator, timeout)
        return element.text
    
    def is_element_visible(self, locator, timeout=10):
        # Проверить видимость элемента.
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_to_disappear(self, locator, timeout=10):
        # Дождаться исчезновения элемента.
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    
    def wait_for_element_to_be_visible(self, locator, timeout=10):
        # Дождаться появления видимого элемента.
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_url_change(self, original_url, timeout=10):
        # Дождаться изменения URL.
        WebDriverWait(self.driver, timeout).until(
            EC.url_changes(original_url)
        )
    
    def get_current_url(self):
        # Получить текущий URL.
        return self.driver.current_url

