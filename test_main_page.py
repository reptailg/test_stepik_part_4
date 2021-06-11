import pages.main_page
import pages.login_page
import pages.basket_page
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = pages.main_page.MainPage(browser,
                                    link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.should_be_login_link()

    login_page=page.go_to_login_page()# переход на страницу логина
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()

#Гость открывает главную страницу
#Переходит в корзину по кнопке в шапке сайта
#Ожидаем, что в корзине нет товаров
#Ожидаем, что есть текст о том что корзина пуста

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page=pages.main_page.MainPage(browser, link)
    page.open()
    page.go_to_basket_button() # перешли в корзину
    link2 = browser.current_url # пытаемся получить линк новой страницы
    #print(link2)
    page2 = pages.basket_page.BasketPage(browser, link2)
    page2.not_product_in_basket()
    page2.text_basket_is_clear()



