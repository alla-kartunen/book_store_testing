# Тест-кейс "Shop: отображение заголовка на странице товара"

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_id("menu-item-50").click()  # Нажать на "My Account"
# Залогиниться
driver.find_element_by_id("username").send_keys("1111@jjj.com")
driver.find_element_by_id("password").send_keys("3zz696bj")
driver.find_element_by_name("login").click()

driver.find_element_by_id("menu-item-40").click()  # Открыть раздел "Shop"
driver.find_element_by_xpath("//img[@title='Mastering HTML5 Forms']").click()  # Открыть страницу книги "HTML5 Forms"

# Проверить заголовок на странице книги
title = driver.find_element_by_class_name("entry-title")
title_check = title.text
if title_check == "HTML5 Forms":
    print("Заголовок соответствует названию книги: " + title_check)
else:
    print("Заголовок не соответствует названию книги: " + title_check)

driver.quit()