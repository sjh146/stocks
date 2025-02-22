
import sys
import pyperclip
import time

from selenium import webdriver
import os
import sys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from user_agent import generate_user_agent, generate_navigator

navigator = generate_navigator()
print(navigator)
print(navigator['platform'])


def resource_path(relative_path):
      
        try:
         # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
 
chromedriver_path =resource_path("chromedriver.exe")
header=generate_user_agent(os='win', device_type='desktop')
#header='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')  # Optional: run in headless mode
options.add_argument('user-agent=' + header)
options.add_argument("disable-blink-features=AutomationControlled")

options.add_experimental_option("detach",True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

service= Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service,options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

time.sleep(1)
print(driver.title)
driver.maximize_window()

driver.get('https://www.deepseek.com/')
stbt = driver.find_element(By.CSS_SELECTOR, 'body > main > div.w-full.bg-center.bg-cover.px-8 > div.flex.flex-col.items-center.w-full.pt-24.md\:pt-32.pb-20.md\:pb-40 > div.grid.grid-cols-1.md\:grid-cols-2.gap-8.w-full.max-w-3xl > a > div.text-xl.font-bold.mb-2.text-branding')
stbt.click()
time.sleep(5)
#driver.find_element(By.CSS_SELECTOR,'ihOWn1 > div > label > input[type=checkbox]')