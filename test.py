from selenium import webdriver

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

driver.get("https://zh-tw.facebook.com/")

driver.find_element_by_id("email").send_keys("123")

driver.find_element_by_id("pass").send_keys("123")