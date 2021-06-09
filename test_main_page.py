import pages.main_page
import pages.login_page

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = pages.main_page.MainPage(browser,
                                    link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page2 = pages.login_page.LoginPage(browser,browser.current_url)
    page2.should_be_login_url()
    page2.should_be_login_form()
    page2.should_be_register_form()

