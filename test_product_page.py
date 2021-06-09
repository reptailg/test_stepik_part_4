import pages.product_page
#import time


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = pages.product_page.ProductPage(browser, link)
    page.open()
    page.go_to_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.shoud_be_product_in_basket()
    page.shoud_be_price_of_product_in_basket()
    #time.sleep(120)




