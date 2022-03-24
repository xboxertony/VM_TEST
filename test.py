from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from config import FB_account,FB_pwd

# driver = webdriver.Chrome(executable_path='./chromedriver.exe')

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

driver.get("https://www.instagram.com/")

time.sleep(5)

driver.find_element_by_css_selector("[name='username']").send_keys(FB_account)

driver.find_element_by_css_selector("[name='password']").send_keys(FB_pwd)

enter = driver.find_element_by_css_selector("[type='submit']")
enter.click()
time.sleep(5)

print("ok")

driver.get("https://www.instagram.com/yga0721/")

time.sleep(10)

a = driver.find_element_by_class_name("XBGH5")

print(a.text)


# driver.get(f"https://www.facebook.com/loserZUN")

# tt = driver.find_elements_by_css_selector(f"[aria-posinset='1']")

# for i in tt:
#     print(i.text)