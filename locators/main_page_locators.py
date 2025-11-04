# Локаторы для главной страницы.

from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы главной страницы Stellar Burgers.
    
    # Кнопки навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//*[contains(text(), 'Конструктор')]")
    ORDERS_FEED_BUTTON = (By.XPATH, "//*[contains(text(), 'Лента Заказов')] | //*[contains(text(), 'Лента заказов')] | //a[contains(@href, '/feed')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account')] | //a[contains(text(), 'Личный Кабинет')] | //a[contains(text(), 'Личный кабинет')] | //p[contains(text(), 'Личный Кабинет')]/parent::a")
    
    # Ингредиенты
    INGREDIENT_BUN = (By.XPATH, "//*[contains(text(), 'Краторная булка N-200i')]/parent::a[@draggable='true'] | //a[@draggable='true' and .//*[contains(text(), 'Краторная булка N-200i')]]")
    INGREDIENT_SAUCE = (By.XPATH, "//*[contains(text(), 'Соус Spicy-X')]/parent::a[@draggable='true'] | //a[@draggable='true' and .//*[contains(text(), 'Соус Spicy-X')]]")
    INGREDIENT_FILLING = (By.XPATH, "//*[contains(text(), 'Говяжий метеорит')]/parent::a[@draggable='true'] | //a[@draggable='true' and .//*[contains(text(), 'Говяжий метеорит')]]")
    
    # Конструктор - зона для перетаскивания (верхняя позиция для булок)
    CONSTRUCTOR_AREA = (By.XPATH, "//*[contains(@class, 'constructor-element') and contains(@class, 'pos_top')] | //*[contains(@class, 'constructor-element_pos_top')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')] | //button[contains(text(), 'Оформить')] | //button[contains(@class, 'Order')]")
    
    # Счетчики ингредиентов
    INGREDIENT_COUNTER = (By.XPATH, "//*[contains(@class, 'counter') and contains(@class, 'num')]")
    
    # Модальное окно деталей ингредиента
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//*[contains(@class, 'Modal') and contains(@class, 'container')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal') and contains(@class, 'close')] | //button[@aria-label='Закрыть'] | //button[contains(@class, 'close')]")
    
    # Заказ
    ORDER_MODAL = (By.XPATH, "//*[contains(@class, 'Modal') and contains(@class, 'container')]")
    ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'text_type_digits-large')] | //p[contains(@class, 'digits-large')] | //*[contains(@class, 'Modal')]//p[contains(@class, 'digits')]")

