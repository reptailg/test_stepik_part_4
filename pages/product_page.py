from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_add_product_to_basket(self):  # добавить продукт в корзину
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def shoud_be_product_in_basket(self):  # проверка продукта в корзине
        messageAddBasket = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_BASKET).text
        productName = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert productName == messageAddBasket, "Product NOT in basket"

    def shoud_be_price_of_product_in_basket(self):  # проверка цены
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.MESSAGE_BASKET_AMOUNT).text, "Product NOT in basket"

    def should_not_be_success_message(self): # упадет, как только увидит искомый элемент. Не появился:тест зеленый
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self): # будет ждать до тех пор, пока элемент не исчезнет
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
                 "Success message not presented, but should be"

