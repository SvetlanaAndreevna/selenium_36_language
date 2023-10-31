from selenium.webdriver.common.by import By
import time

def test_add_to_basket(browser):
    browser.implicitly_wait(5)
    browser.get('https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    basket = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    # basket[0].click() # при желании можно проверить и добавить товар в корзину
    time.sleep(5) #добавила, чтобы посмотреть
    assert len(basket) == 1, 'Кнопка добавления в корзину не найдена' # проверяем, что кнопка найдена и что она одна
