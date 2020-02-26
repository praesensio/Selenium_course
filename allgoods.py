from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://selenium1py.pythonanywhere.com/ru/"

try:
    browser = webdriver.Chrome('')
    browser.get(link)
    # открываем главную страницу
    dropdown = Select(browser.find_element_by_class_name('.dropdown-toggle'))
    dropdown.select_by__visible_text("Все товары")
    # выбираем в выпадающем списке "Все товары", но тест должен упасть,так как выпадающий список не работает

finally:

    # закрываем браузер после всех манипуляций
    browser.quit()

