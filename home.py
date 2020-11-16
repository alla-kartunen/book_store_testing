# Тест-кейс "Home: добавление комментария"

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0, 600);")

driver.find_element_by_xpath("//img[@title='Selenium Ruby']").click()  # Нажать на книгу "Selenium Ruby"

driver.find_element_by_css_selector(".reviews_tab > a").click()  # Выбрать вкладку "Reviews"

driver.find_element_by_css_selector(".star-5").click()  # Выбрать 5 звёзд
driver.find_element_by_id("comment").send_keys("Nice book!")  # Ввести в поле комментария текст "Nice book!"
driver.find_element_by_id("author").send_keys("Name")  # Ввести имя автора
driver.find_element_by_id("email").send_keys("email@mail.ru")  # Ввести email
driver.find_element_by_id("submit").click()  # Нажать кнопку "Submit"

driver.quit()