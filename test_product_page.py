from .product_page import ProductPage
from .main_page import MainPage
import pytest

#product_base_link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.parametrize('promo_code', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, promo_code):
    PRODUCT_URL = ('https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}'.format(promo_code))
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.should_add_product_to_basket()
    page.should_be_success_message()
    page.should_be_correct_basket_total()  #pytest -s
    
"""проверку можно реализовать:
@pytest.mark.parametrize('link', ["okay_link",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "okay_link"])"""