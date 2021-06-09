import pages.main_page
import pages.login_page

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_go_to_login_page(browser):
    page = pages.main_page.MainPage(browser,
                                    link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.should_be_login_link()

    login_page=page.go_to_login_page()# переход на страницу логина
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()

