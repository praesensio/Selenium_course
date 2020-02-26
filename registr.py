from selenium import webdriver
import time



link = "http://selenium1py.pythonanywhere.com/ru/"

try:
    browser = webdriver.Chrome('')
    browser.get(link)
    # открываем главную страницу
    a = browser.find_element_by_id('login_link')
    a.click()
    #открываем страницу регистрации и авторизации
    input1 = browser.find_element_by_xpath('.//*[@name = "registration-email"]')
    input1.send_keys('test@gmail.ru')
    # заполняем поле почта валидным значением
    input2 = browser.find_element_by_xpath('.//*[@name = "registration-password1"]')
    input2.send_keys('123890')
    # заполняем поле ввода пароля невалидным значением
    input3 = browser.find_element_by_xpath('.//*[@name = "registration-password2"]')
    input3.send_keys('123890')
    # заполняем поле повторного ввода пароля невалидным значением
    button = browser.find_element_by_xpath('.//*[@name = "registration_submit"]')
    button.click()
    # нажимаем кнопку регистрации
    time.sleep(3)
    text1 = browser.find_element_by_xpath('.//*[@class="alert alert-danger"]')
    text= text1.text

    assert "Опаньки! Мы нашли какие-то ошибки - пожалуйста, проверьте сообщения об ошибках ниже и попробуйте еще раз" == text


finally:

    # закрываем браузер после всех манипуляций
    browser.quit()

