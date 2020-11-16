# Тест-кейс "Shop: работа в корзине"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 15)

driver.find_element_by_id("menu-item-40").click()  # Открыть раздел "Shop"
driver.execute_script("window.scrollBy(0, 300);")
# Добавить в корзину книгу "HTML5 WebApp Develpment"
driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# Дождаться, пока у книги "HTML5 WebApp Develpment" появится надпись "added to cart"
wait_for_added = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".post-182 > .added_to_cart")) )
# Добавить в корзину книгу "JS Data Structures and Algorithm"
driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']").click()

driver.find_element_by_id("wpmenucartli").click()  # Перейти в корзину
# Удалить из корзины книгу "HTML5 WebApp Develpment"
driver.find_element_by_css_selector("[data-product_id='182']").click()
# Дождаться, пока появится сообщение об удалении
wait_for_undo = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-message")) )
# Отменить удаление через ссылку "Undo"
driver.find_element_by_css_selector(".woocommerce-message > a").click()

# Очистить поле количества, ввести количество, равное 3
gty_of_items = driver.find_element_by_css_selector("tbody > :nth-child(1) input")
gty_of_items.clear()
gty_of_items.send_keys("3")
# Нажать на кнопку "Update Basket"
driver.find_element_by_css_selector("[value='Update Basket']").click()
# Дождаться обновления корнизы и проверить, что количество равно 3
wait_for_update = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-message")))
qty_js = driver.find_element_by_css_selector("tbody > :nth-child(1) input")
qty_js_check = qty_js.get_attribute("value")
assert qty_js_check == "3"

# Нажать на кнопку "Apply Coupon"
apply_coupon_btn = driver.find_element_by_name("apply_coupon")
apply_coupon_btn.click()
# Проверить, что появилось сообщение с текстом об ошибке
error = driver.find_element_by_class_name("woocommerce-error")
error_check = error.text
assert error_check == "Please enter a coupon code."

driver.quit()