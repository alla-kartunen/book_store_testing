# Тест-кейс "Registration: регистрация аккаунта"

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_id("menu-item-50").click()  # Нажать на "My Account"

driver.find_element_by_id("reg_email").send_keys("mail66@mail.ru")  # Ввести email
driver.find_element_by_id("reg_password").send_keys("e24yBqHw22")  # Ввести пароль
registration_btn = driver.find_element_by_name("register")  # Найти кнопку "register"
time.sleep(5)  # EC не срабатывает, кнопка заблокирована
registration_btn.click()  # Нажать на кнопку "register"

driver.quit()