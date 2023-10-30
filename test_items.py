from selenium.webdriver.common.by import By
import time

def test_add_to_basket(browser):
    browser.implicitly_wait(5)
    browser.get('https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    basket = browser.find_elements(By.ID, 'id_quantity')
    time.sleep(5) #добавила, чтобы посмотреть
    assert basket, 'Кнопка добавления в корзину не найдена'
