# Локаторы для главной страницы.

from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы главной страницы Stellar Burgers.
    
    # Кнопки навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[text()='Лента заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный кабинет']")
    
    # Ингредиенты
    INGREDIENT_BUN = (By.XPATH, "//p[text()='Краторная булка N-200i']")
    INGREDIENT_SAUCE = (By.XPATH, "//p[text()='Соус Spicy-X']")
    INGREDIENT_FILLING = (By.XPATH, "//p[text()='Говяжий метеорит (отбивная)']")
    
    # Конструктор
    CONSTRUCTOR_AREA = (By.CLASS_NAME, "BurgerConstructor_basket__container__")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # Счетчики ингредиентов
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter_counter__num__")
    
    # Модальное окно деталей ингредиента
    INGREDIENT_DETAILS_MODAL = (By.CLASS_NAME, "Modal_modal__container__")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__']")
    
    # Заказ
    ORDER_MODAL = (By.CLASS_NAME, "Modal_modal__container__")
    ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'text text_type_digits-large')]")

