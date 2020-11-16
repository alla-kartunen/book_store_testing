# Тест-кейс "Shop: количество товаров в категории HTML"

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
driver.find_element_by_link_text("HTML").click()  # Выбрать категорию "HTML"

count_items = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")  # Найти все товары категории
if len(count_items) == 3:
    print("В разделе 3 товара")
else:
    print("ERROR. Количество товаров в разделе: " + str(len(count_items)))

driver.quit()