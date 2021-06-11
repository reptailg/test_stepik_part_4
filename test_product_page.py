import pytest

import pages.product_page
import pages.basket_page
import pages.login_page
import time

# тестируем 10 линков
# подготовка списка из 10 линков
mask = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
xfile = 7
links = [mask+str(i) for i in range(10) if i != xfile]
xlink = pytest.param(mask+str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
links.insert(xfile, xlink)

@pytest.mark.need_review
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = pages.product_page.ProductPage(browser, link)
    page.open()
    page.go_to_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.shoud_be_product_in_basket()
    page.shoud_be_price_of_product_in_basket()

class TestUserAddToBasketFromProductPage():
    # открыть страницу регистрации;
    # зарегистрировать нового пользователя;
    # проверить, что пользователь залогинен.
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = pages.product_page.ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = pages.login_page.LoginPage(browser, browser.current_url)
        time.sleep(5)
        login_page.register_new_user(str(time.time()) + "@fakemail.org", "123F5678n0")
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = pages.product_page.ProductPage(browser, link)
        page.open()
        page.go_to_add_product_to_basket()
        page.shoud_be_product_in_basket()
        page.shoud_be_price_of_product_in_basket()

    #Открываем страницу товара
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    @pytest.mark.skip
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page =pages.product_page.ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

#Гость открывает страницу товара
#Переходит в корзину по кнопке в шапке
#Ожидаем, что в корзине нет товаров
#Ожидаем, что есть текст о том что корзина пуста
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page=pages.product_page.ProductPage(browser, link)
    page.open()
    page.go_to_basket_button() # перешли в корзину
    link2 = browser.current_url # пытаемся получить линк новой страницы
    #print(link2)
    page2 = pages.basket_page.BasketPage(browser, link2)
    page2.not_product_in_basket()
    page2.text_basket_is_clear()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = pages.product_page.ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

#Открываем страницу товара
#Добавляем товар в корзину
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page=pages.product_page.ProductPage(browser, link2)
    page.open()
    page.go_to_add_product_to_basket()
    page.should_not_be_success_message()

    #Открываем страницу товара
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page=pages.product_page.ProductPage(browser, link2)
    page.open()
    page.should_not_be_success_message()

#Открываем страницу товара
#Добавляем товар в корзину
#Проверяем, что нет сообщения об успехе с помощью is_disappeared
@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page=pages.product_page.ProductPage(browser, link2)
    page.open()
    page.go_to_add_product_to_basket()
    page.should_be_success_message()

# Проверить наличие ссылки на страницу логина
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = pages.product_page.ProductPage(browser, link)
    page.open()
    page.should_be_login_link()









