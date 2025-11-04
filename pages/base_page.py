# Базовый класс для всех Page Objects.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def find_elements(self, locator, timeout=10):
        # Найти элементы с ожиданием.
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)
    
    def click(self, locator, timeout=10):
        # Кликнуть по элементу.
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
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

