
import eel
import sys
import pyperclip
import time
import sqlite3
from selenium import webdriver
import os
import sys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import ollama
from fake_useragent import UserAgent
eel.init('web')
@eel.expose
def insert_blog(uun, uid, upw):
    with sqlite3.connect('blog.db') as conn:
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS blog ( uun TEXT PRIMARY KEY AUTOINCREMENT, uid TEXT NOT NULL, upw TEXT NOT NULL)')
        c.execute("INSERT INTO blog (uun, uid, upw) VALUES (?, ?, ?)", (uun, uid, upw))
        c.execute("SELECT * FROM blog ")
        results = c.fetchall()
        for result in results:
            print(result)
        
        conn.commit()
        crawl(uid,upw)
        
@eel.expose
def delete_blog(sdata):
    with sqlite3.connect('blog.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM blog WHERE uun = ?', (sdata,))
        conn.commit()
        
    
@eel.expose
def resource_path(relative_path):
      
        try:
         # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
 
@eel.expose
def crawl(uid,upw):
    #ua=UserAgent()
   # header =ua.chrome
    #print(header)
    chromedriver_path =resource_path("chromedriver.exe")     
    header='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')  # Optional: run in headless mode
    options.add_argument('user-agent=:' + header)
    options.add_argument("disable-blink-features=AutomationControlled")
   # options.add_argument(r'user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default')
    options.add_experimental_option("detach",True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    #options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
    # --enable-logging --v=1
    service= Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service,options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    time.sleep(1)
    print(driver.title)
    driver.maximize_window()
    #로그인 메뉴 클릭
    driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
     
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
    
    driver.get('https://blog.naver.com/{}?Redirect=Write&'.format(uid))
    time.sleep(5)
    try:
        iframe_list = driver.find_elements('css selector', 'iframe')
        #iframe = iframe_list[0]
        print(iframe_list)
        #iframe_name = iframe.get_attribute('name')
        #driver.switch_to.frame(iframe_name)
        #driver.find_elements('css selector', '종료 버튼 css selector')[0].click()
        driver.switch_to.window(driver.window_handles[0]) 

    except:
        print('임시저장창없음')

    time.sleep(2)
    driver.switch_to.frame('mainFrame')
    time.sleep(4)
  
    actions=ActionChains(driver)
    title=driver.find_element(By.XPATH,'//span[contains(text(),"제목")]')
    actions.click(title).perform()
    
    actions.send_keys('블로그제목입니다.').perform()
    
    article=driver.find_element(By.XPATH,'//span[contains(text(),"본문에 #을 이용하여 태그를 사용해보세요! (최대 30개)")]')
    actions.click(article).perform()
    
    #blog_title=ollama.chat(model='llama3',messages=[
        #{
            #'role':'user',
            #'content':'give me one simple blog title',

        #},
    
    #])
    
    time.sleep(2)
    #actions.send_keys(blog_title['message']['content']).perform()

    
       
eel.start('index.html', size=(600, 400))
