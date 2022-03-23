from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


opts = Options()
opts.add_argument('--headless')  #無頭chrome
opts.add_argument('--disable-gpu')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),chrome_options=opts)

driver.get("https://zh-tw.facebook.com/")

print(driver.find_element_by_id("email"))

print(driver.find_element_by_id("pass"))