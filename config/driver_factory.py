# Фабрика для создания драйверов браузеров.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverFactory:
    # Фабрика для создания драйверов браузеров.
    
    @staticmethod
    def create_driver(browser_name):
        # Создать драйвер для указанного браузера.
        browser_name = browser_name.lower()
        if browser_name == 'chrome':
            options = ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            options = FirefoxOptions()
            driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Неизвестный браузер: {browser_name}. Поддерживаются: chrome, firefox")
        driver.maximize_window()
        return driver
