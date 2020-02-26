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
    input1 = browser.find_element_by_xpath('.//*[@name = "login-username"]')
    input1.send_keys('tester5555@gmail.grutu')
    # вводим валидную почту
    input2 = browser.find_element_by_xpath('.//*[@name = "login-password"]')
    input2.send_keys('test4auth2345')
    # вводим невалидный пароль в поле ввода
    button = browser.find_element_by_xpath('.//*[@name = "login_submit"]')
    button.click()
    # нажимаем кнопку войти
    time.sleep(3)
    text1 = browser.find_element_by_xpath('(.//*[@class="alert alert-danger"])[2]')
    text = text1.text

    assert "Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть чувствительны к регистру." == text


finally:

    # закрываем браузер после всех манипуляций
    browser.quit()

