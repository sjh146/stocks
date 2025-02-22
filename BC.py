


import sys
import pyperclip
import time

from selenium import webdriver
import os
import sys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



import time
def resource_path(relative_path):
      
        try:
         # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
 
chromedriver_path =resource_path("chromedriver.exe")
        

options = webdriver.ChromeOptions()

        
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')  # Optional: run in headless mode
options.add_experimental_option("detach",True)
service= Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service,options=options)
       

time.sleep(1)
print(driver.title)
driver.maximize_window()
#로그인 메뉴 클릭
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

uid = 'sjh146'
upw = 'jhlee836060@'
# Find the username and password fields
tag_id = driver.find_element(By.NAME, 'id')
tag_pw = driver.find_element(By.NAME, 'pw')

# Use pyperclip to copy and paste the username
pyperclip.copy(uid)
tag_id.click()
tag_id.send_keys(Keys.CONTROL, 'v')  # Paste using Ctrl+V
time.sleep(1)

# Use pyperclip to copy and paste the password
pyperclip.copy(upw)
tag_pw.click()
tag_pw.send_keys(Keys.CONTROL, 'v')  # Paste using Ctrl+V
time.sleep(1)

# Find and click the login button
login_btn = driver.find_element(By.CSS_SELECTOR, '.btn_login')
login_btn.click()
time.sleep(2)