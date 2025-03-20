import pytest
from .product_page import ProductPage
from .main_page import MainPage

@pytest.mark.parametrize('promo_code', [0,1,2,3,4,5,6, pytest.param(7, marks=pytest.mark.xfail), 8,9])
def test_guest_can_add_product_to_basket(browser):
    PRODUCT_URL = ('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}'.format(promo_code))
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.solve_quiz_and_get_code()
    page.add_to_basket()
    page.should_be_success_message()
    page.should_be_correct_basket_total()
    
    
"""можно так: @pytest.mark.parametrize('link', ["okay_link",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "okay_link"])"""