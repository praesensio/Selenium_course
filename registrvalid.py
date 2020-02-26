1.
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/ru/"

try:
    browser = webdriver.Chrome('')
    browser.get(link)
    # загружается главная страницу
    a = browser.find_element_by_id('login_link')
    a.click()
    # переходим на страницу для регистрации либо авторизации
    input1 = browser.find_element_by_xpath('.//*[@name = "registration-email"]')
    input1.send_keys('tester5555@gmail.grutu')
    # вводим валидную почту
    input2 = browser.find_element_by_xpath('.//*[@name = "registration-password1"]')
    input2.send_keys('test4auth')
    # вводим валидный пароль в поле ввода
    input3 = browser.find_element_by_xpath('.//*[@name = "registration-password2"]')
    input3.send_keys('test4auth')
    # вводим валидный пароль в поле для повторного ввода
    button = browser.find_element_by_xpath('.//*[@name = "registration_submit"]')
    button.click()
    # нажимаем кнопку регистрации
    time.sleep(3)
    text1 = browser.find_element_by_xpath('.//*[@class="alertinner wicon"]')
    text = text1.text
    # у теста есть недостаток, надо постоянно менять значение почты, но я читала что это можно делать автоматически как то

    assert "Спасибо за регистрацию!" == text


finally:

    # закрываем браузер после всех манипуляций
    browser.quit()





