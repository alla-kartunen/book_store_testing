# Тест-кейс "Shop: сортировка товаров по цене от большей к меньшей"

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

driver.find_element_by_id("menu-item-40").click()  # Нажать на "Shop"
sorted_by = driver.find_element_by_css_selector("[value='menu_order']")  # Переменная для строки "Default sorting"
sorted_by_checked = sorted_by.get_attribute("selected")  # Наличие атрибута selected для строки "Default sorting"
if sorted_by_checked is not None:
    print("В селекторе выбран верный атрибут")
else:
    print("В селекторе выбран неверный атрибут")

# Выбрать сортировку от большего к меньшему
from selenium.webdriver.support.select import Select
selector_name = driver.find_element_by_class_name("orderby")
select = Select(selector_name)
select.select_by_value("price-desc")

# Проверка, что выбрана сортировка "Sort by price: high to low"
sorted_by_new = driver.find_element_by_css_selector("[value='price-desc']")
sorted_by_new_checked = sorted_by.get_attribute("selected")
if sorted_by_new_checked is not None:
    print("В селекторе выбран верный атрибут")
else:
    print("В селекторе выбран неверный атрибут")

driver.quit()