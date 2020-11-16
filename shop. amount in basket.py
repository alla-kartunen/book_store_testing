# Тест-кейс "Shop: проверка цены в корзине"

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

# В разделе "Shop" добавить в корзину книгу "HTML5 WebApp Develpment"
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()

# Проверка, что в корзине 1 товар
number_of_items = driver.find_element_by_class_name("cartcontents")
number_of_items_check = number_of_items.text
assert number_of_items_check == "1 Item"
# Проверка, что стоимость товаров в корзине в верхнем меню равна "₹180.00"
amount = driver.find_element_by_class_name("amount")
amount_check = amount.text
assert amount_check == "₹180.00"

driver.find_element_by_id("wpmenucartli").click()  # Перейти в корзину

# Проверка, что стоимость товаров на странице корзины равна "₹180.00"
amount_in_basket = driver.find_element_by_css_selector(".woocommerce-Price-amount.amount")
amount_in_basket_check = amount_in_basket.text
assert amount_in_basket_check == "₹180.00"

driver.quit()