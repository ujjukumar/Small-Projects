# Importing Selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\\Users\\Ujju\\Documents\\Programs\\test\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(10)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
	actions.perform()
	count = int(cookie_count.text.split(" ")[0])
	# print(count)
	for item in items:
		value = int(item.text)
		if value < count:
			upgarde_action = ActionChains(driver)
			upgarde_action.move_to_element(item)
			upgarde_action.click()
			upgarde_action.perform()