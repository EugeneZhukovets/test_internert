import pytest
import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.parametrize('language',['language'])
def test_guest_should_see_login_link(browser,language):
    browser.get(link)
    element = browser.find_element_by_xpath("//form[@id='add_to_basket_form']/button[@type='submit']")
    assert element.get_attribute('class') == "btn btn-lg btn-primary btn-add-to-basket", \
        f"нет такого {element.get_attribute}"
    
     
    