# Тест-кейс "Shop: скидка товара"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(5)
wait5 = WebDriverWait(driver, 5)

driver.find_element_by_id("menu-item-50").click()  # Нажать на "My Account"
# Залогиниться
driver.find_element_by_id("username").send_keys("1111@jjj.com")
driver.find_element_by_id("password").send_keys("3zz696bj")
driver.find_element_by_name("login").click()

# В разделе "Shop" выбрать книгу "Android Quick Start Guide"
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector("[title='Android Quick Start Guide']").click()
# Проверка старой цены
price_old = driver.find_element_by_css_selector("del > span")
price_old_check = price_old.text
assert price_old_check == "₹600.00"
# Проверка цены со скидкой
price_new = driver.find_element_by_css_selector("ins > span")
price_new_check = price_new.text
assert price_new_check == "₹450.00"

driver.quit()