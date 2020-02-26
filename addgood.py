from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/ru/"

try:
    browser = webdriver.Chrome('')
    browser.get(link)
    # открываем главную страницу
    a = browser.find_element_by_xpath('//a[contains(text(),"Books")]').click()
    # переходим к покупке книг
    book = browser.find_element_by_css_selector(':nth-child(3) > .product_pod > h3 > a').click()
    # выбираем книгу Coders at Work
    add = browser.find_element_by_css_selector('#add_to_basket_form > .btn').click()
    # добавляем книгу в коризну
    time.sleep(3)
    text1 = browser.find_element_by_xpath('//strong[contains(text(),"Coders at Work")]')
    # убеждаемся что добавлена выбранная книга
    button = browser.find_element_by_css_selector('.alertinner > :nth-child(2) > :nth-child(1)').click()
    # переходим в корзину
    time.sleep(3)
    gotcha = browser.find_element_by_css_selector('.col-sm-4 > h3')
    basket = gotcha.text
    assert "Coders at Work" == basket
    # проверяем что выбранная книга находится в корзине


finally:

    # закрываем браузер после всех манипуляций
    browser.quit()




