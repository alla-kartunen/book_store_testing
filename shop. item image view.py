# Тест-кейс "Shop: просмотр изображения товара"

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
# Нажать на просмотр изображения
img_click = wait5.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[itemprop='image']")) )
driver.find_element_by_css_selector("[itemprop='image']").click()
# Закрыть окно с изображением
img_close = wait5.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) )
driver.find_element_by_class_name("pp_close").click()

driver.quit()