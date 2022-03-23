from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.set_headless(headless=True)

driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get("https://zh-tw.facebook.com/")

driver.find_element_by_id("email").send_keys("123")

driver.find_element_by_id("pass").send_keys("123")