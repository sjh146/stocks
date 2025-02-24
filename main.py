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
from user_agent import generate_user_agent, generate_navigator
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
    navigator = generate_navigator()
    print(navigator)
    print(navigator['platform'])
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
    
    #Find, click adn type in the search_box
    search_box =driver.find_element(By.CSS_SELECTOR,'#query')
    search_box.click()
    search_box.send_keys('네이버블로그')
    search_btn =driver.find_element(By.CSS_SELECTOR,'#search-btn')
    search_btn.click()
    time.sleep(2)
    
    #Find and click naverblog
    driver.execute_script("window.scrollTo(0, 500)")
    nblog=driver.find_element(By.CSS_SELECTOR,'#main_pack > section.sc_new.sp_nsite._project_channel_site_root._fe_site_collection._prs_vsd_bas > div > div > div.nsite_tit > div > div.nsite_name > a > mark')
    nblog.click()
    time.sleep(1)

    write_btn=driver.find_element(By.CSS_SELECTOR,'#container > div > aside > div > div:nth-child(1) > nav > a:nth-child(2)')
    write_btn.click()

    with sqlite3.connect('blog.db') as conn:
        conn.close()
eel.start('index.html', size=(600, 400))
 #SE-99c10990-f8cf-4208-9ea2-0bda71528e48 > div.se-wrap.se-dnd-wrap > div > div.se-popup.__se-sentry.se-popup-alert.se-popup-alert-confirm > div.se-popup-container.__se-pop-layer > div.se-popup-button-container > button.se-popup-button.se-popup-button-confirm > span