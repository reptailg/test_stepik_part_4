from selenium.webdriver.common.by import By


#class MainPageLocators(): # ушел в BasePage
#    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    MESSAGE_ADD_BASKET = (By.CSS_SELECTOR, "#messages>:first-child>div>strong")
    MESSAGE_BASKET_AMOUNT= (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini>.btn-group>:first-child") # кнопка перехода в корзину

class BasketPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, "#content_inner")
    BASKET_CLEAR = (By.CSS_SELECTOR, "#content_inner>p") # текст о том, что корзина пуста
    BASKET_BUTTON_BLOCK = (By.CSS_SELECTOR, ".btn-block") # перейти к оформлению - если нет - пустая корзина



