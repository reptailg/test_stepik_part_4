from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    # в корзине нет товаров
    def not_product_in_basket(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_BUTTON_BLOCK), "Product in basket"

    # в корзине есть товар
    def product_in_basket(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_BUTTON_BLOCK), "Basket is clear!"

    # есть надпись, что корзина пуста
    def text_basket_is_clear(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_CLEAR), "Basket is not clear!"

    # нет надписи, что корзина пуста
    def not_text_basket_is_clear(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_CLEAR), "Basket is clear!"
