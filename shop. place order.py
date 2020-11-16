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

driver.find_element_by_id("menu-item-40").click()  # Открыть раздел "Shop"
driver.execute_script("window.scrollBy(0, 300);")
# Добавить в корзину книгу "HTML5 WebApp Develpment"
driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# Дождаться, пока в корзине верхнего меню появится надпись "1 Item", затем перейти в корзину
wait_for_basket = wait.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "cartcontents"), "1 Item") )
driver.find_element_by_id("wpmenucartli").click()

# Дождаться подгрузки кнопки "Proceed to Checkout", нажать на неё
wait_for_checkout = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "wc-proceed-to-checkout")) )
driver.find_element_by_css_selector(".wc-proceed-to-checkout a").click()

# Дождаться подгрузки первого поля
wait_for_input = wait.until(
    EC.visibility_of_element_located((By.ID, "billing_first_name")) )

# Заполнить обязательные поля
driver.find_element_by_id("billing_first_name").send_keys("First")
driver.find_element_by_id("billing_last_name").send_keys("Last")
driver.find_element_by_id("billing_email").send_keys("email@mail.ru")
driver.find_element_by_id("billing_phone").send_keys("+1 (566) 762-5373")
driver.find_element_by_id("s2id_billing_country").click()  # Селектор выбора страны
driver.find_element_by_id("s2id_autogen1_search").send_keys("king")  # Ввести в поиск по селектору "king"
driver.find_element_by_id("select2-results-1").click()  # Выбрать первый результат поиска
driver.find_element_by_id("billing_address_1").send_keys("27 Rocky Nobel Drive")
driver.find_element_by_id("billing_city").send_keys("London")
driver.find_element_by_id("billing_postcode").send_keys("EC1A 1AA")

driver.execute_script("window.scrollBy(0, 700);")

time.sleep(5)  # EC здесь не работает
driver.find_element_by_id("payment_method_cheque").click()  # Выбрать способ оплаты "Check Payments"

driver.find_element_by_id("place_order").click()  # Нажать на кнопку "Place Order"

# Дождаться надписи "Thank you. Your order has been received."
wait_for_place_order = wait.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received.") )
# Проверить, что выбран способ оплаты "Check Payments"
wait_for_info = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot :nth-child(3) td"), "Check Payments") )

driver.quit()