# Тест-кейс "Registration_login: логин в систему"

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_id("menu-item-50").click()  # Нажать на "My Account"

driver.find_element_by_id("username").send_keys("1111@jjj.com")  # Ввести email
driver.find_element_by_id("password").send_keys("3zz696bj")  # Ввести пароль
driver.find_element_by_name("login").click()  # Нажать на кнопку "login"

# Проверить, что есть ссылка "Sign out"
logout_btn = driver.find_element_by_css_selector(".woocommerce-MyAccount-content > p > a")
logout_btn_text = logout_btn.text
if logout_btn_text == ("Sign out"):
    print("В окне аккаунта есть кнопка Sign out")
else:
    print("ERROR: В окне аккаунта нет кнопки Sign out")

driver.quit()