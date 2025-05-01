import time
from selenium.common import TimeoutException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    try:
        button = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located(("xpath", "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"))
        )
        # Проверка, что кнопка существует и является элементом
        assert button is not None, "Кнопка не найдена. Assert" # Избыточная проверка, но добавлена для Assertб по идее AssertionError тут предостаточно
    except TimeoutException:
        raise AssertionError("Кнопка не найдена. AssertionError")