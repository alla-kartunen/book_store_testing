# Тест-кейс "Shop: отображение страницы товара"

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)

# driver.find_element_by_id("menu-item-50").click()
#
# driver.get("http://practice.automationtesting.in/my-account/") # добавлено из-за рекламного фрейма
#
# driver.find_element_by_id("username").send_keys("1111@jjj.com")
# driver.find_element_by_id("password").send_keys("3zz696bj")
# driver.find_element_by_name("login").click()
#
# driver.find_element_by_id("menu-item-40").click()

# driver.find_element_by_xpath("//img[@title='Mastering HTML5 Forms']").click()
#
# title_check = driver.find_element_by_class_name("entry-title")
# title_text = title_check.text
# if title_text == "HTML5 Forms":
#     print("Заголовок соответствует названию книги: " + title_text)
# else:
#     print("Заголовок не соответствует названию книги: " + title_text)


# Тест-кейс "Shop: количество товаров в категории"

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)

# driver.find_element_by_id("menu-item-50").click()

# driver.get("http://practice.automationtesting.in/my-account/") # добавлено из-за рекламного фрейма
#
# driver.find_element_by_id("username").send_keys("1111@jjj.com")
# driver.find_element_by_id("password").send_keys("3zz696bj")
# driver.find_element_by_name("login").click()
#
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_link_text("HTML").click()
#
# count_items = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
# if len(count_items) == 3:
#     print("В разделе 3 товара")
# else:
#     print("Ошибка. Количество товаров в разделе: " + str(len(count_items)))


# Тест-кейс "Shop: сортировка товаров"

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)

# driver.find_element_by_id("menu-item-50").click()
#
# driver.get("http://practice.automationtesting.in/my-account/") # добавлено из-за рекламного фрейма
#
# driver.find_element_by_id("username").send_keys("1111@jjj.com")
# driver.find_element_by_id("password").send_keys("3zz696bj")
# driver.find_element_by_name("login").click()
#
# driver.find_element_by_id("menu-item-40").click()
# sorted_by = driver.find_element_by_css_selector("[value='menu_order']")
# sorted_by_checked = sorted_by.get_attribute("selected")
# if sorted_by_checked is not None:
#     print("В селекторе выбран верный атрибут")
# else:
#     print("В селекторе выбран неверный атрибут")
#
# from selenium.webdriver.support.select import Select
# selector_name = driver.find_element_by_class_name("orderby")
# select = Select(selector_name)
# select.select_by_value("price-desc")
#
# sorted_by = driver.find_element_by_css_selector("[value='price-desc']")
# sorted_by_checked = sorted_by.get_attribute("selected")
# if sorted_by_checked is not None:
#     print("В селекторе выбран верный атрибут")
# else:
#     print("В селекторе выбран неверный атрибут")


# Тест-кейс "Shop: отображение, скидка товара"

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait5 = WebDriverWait(driver, 5)

# driver.find_element_by_id("menu-item-50").click()

# driver.get("http://practice.automationtesting.in/my-account/") # добавлено из-за рекламного фрейма

# driver.find_element_by_id("username").send_keys("1111@jjj.com")
# driver.find_element_by_id("password").send_keys("3zz696bj")
# driver.find_element_by_name("login").click()

# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector("[title='Android Quick Start Guide']").click()

# price_old = driver.find_element_by_css_selector("del > span")
# price_old_check = price_old.text
# assert price_old_check == "₹600.00"

# price_new = driver.find_element_by_css_selector("ins > span")
# price_new_check = price_new.text
# assert price_new_check == "₹450.00"

# img_click = wait5.until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "[itemprop='image']")) )
# driver.find_element_by_css_selector("[itemprop='image']").click()

# img_close = wait5.until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) )
# driver.find_element_by_class_name("pp_close").click()


# Тест-кейс "Shop: проверка цены в корзине"

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)

# driver.find_element_by_id("menu-item-50").click()
#
# driver.get("http://practice.automationtesting.in/my-account/") # добавлено из-за рекламного фрейма
#
# driver.find_element_by_id("username").send_keys("1111@jjj.com")
# driver.find_element_by_id("password").send_keys("3zz696bj")
# driver.find_element_by_name("login").click()
#
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
#
# number_of_items = driver.find_element_by_class_name("cartcontents")
# number_of_items_check = number_of_items.text
# assert number_of_items_check == "1 Item"
#
# amount = driver.find_element_by_class_name("amount")
# amount_check = amount.text
# assert amount_check == "₹180.00"
#
# driver.find_element_by_id("wpmenucartli").click()
#
# amount_in_basket = driver.find_element_by_css_selector(".woocommerce-Price-amount.amount")
# amount_in_basket_check = amount_in_basket.text
# assert amount_in_basket_check == "₹180.00"


# Тест-кейс "Shop: работа в корзине"

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 15)
#
# driver.find_element_by_id("menu-item-40").click()
#
# driver.get("http://practice.automationtesting.in/shop/") # добавлено из-за рекламного фрейма
#
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
#
# wait_for_added = wait.until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, ".post-182 > .added_to_cart")) )
# driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']").click()
#
# driver.find_element_by_id("wpmenucartli").click()
#
# driver.find_element_by_css_selector("[data-product_id='182']").click()
#
# wait_for_undo = wait.until(
#     EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-message")) )
#
# driver.find_element_by_css_selector(".woocommerce-message > a").click()
#
# input = driver.find_element_by_css_selector("tbody > :nth-child(1) input")
# input.clear()
# input.send_keys("3")
#
# driver.find_element_by_css_selector("[value='Update Basket']").click()
#
# qty_js = driver.find_element_by_css_selector("tbody > :nth-child(1) input")
# qty_js_check = qty_js.get_attribute("value")
# assert qty_js_check == "3"
#
# wait_for_update = wait.until(
#     EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-message")) )
#
# apply_coupon_btn = driver.find_element_by_name("apply_coupon")
# apply_coupon_btn.click()
#
# error = driver.find_element_by_class_name("woocommerce-error")
# error_check = error.text
# assert error_check == "Please enter a coupon code."

# Тест-кейс "Shop: покупка товара"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

driver.find_element_by_id("menu-item-40").click()

driver.get("http://practice.automationtesting.in/shop/") # добавлено из-за рекламного фрейма
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()

wait_for_basket = wait.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "cartcontents"), "1 Item") )
driver.find_element_by_id("wpmenucartli").click()

wait_for_checkout = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "wc-proceed-to-checkout")) )
driver.find_element_by_css_selector(".wc-proceed-to-checkout a").click()

wait_for_input = wait.until(
    EC.visibility_of_element_located((By.ID, "billing_first_name")) )

driver.find_element_by_id("billing_first_name").send_keys("First")
driver.find_element_by_id("billing_last_name").send_keys("Last")
driver.find_element_by_id("billing_email").send_keys("email@mail.ru")
driver.find_element_by_id("billing_phone").send_keys("+1 (566) 762-5373")

driver.find_element_by_id("s2id_billing_country").click() # селектор
driver.find_element_by_id("s2id_autogen1_search").send_keys("king")
driver.find_element_by_id("select2-results-1").click()

driver.find_element_by_id("billing_address_1").send_keys("27 Rocky Nobel Drive")
driver.find_element_by_id("billing_city").send_keys("London")
driver.find_element_by_id("billing_postcode").send_keys("EC1A 1AA")

driver.execute_script("window.scrollBy(0, 700);") # 600 оказалось мало

time.sleep(5)
driver.find_element_by_id("payment_method_cheque").click()

driver.find_element_by_id("place_order").click()

wait_for_place_order = wait.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received.") )

wait_for_info = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot :nth-child(3) td"), "Check Payments") )

driver.quit()