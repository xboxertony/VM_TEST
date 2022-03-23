from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from config import FB_account,FB_pwd

# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()

# print("1")
opts = Options()
opts.add_argument('--no-sandbox')
opts.add_argument('--headless')  #無頭chrome
opts.add_argument('--disable-gpu')
# print("2")

# print(ChromeDriverManager().install())

driver = webdriver.Chrome(chrome_options=opts)

driver.get("https://zh-tw.facebook.com/")

driver.find_element_by_id("email").send_keys(FB_account)

driver.find_element_by_id("pass").send_keys(FB_pwd)

enter = driver.find_element_by_css_selector("[data-testid='royal_login_button']")
enter.click()
time.sleep(3)


driver.get(f"https://www.facebook.com/loserZUN")

tt = driver.find_elements_by_css_selector(f"[aria-posinset='1']")

print(tt.text)