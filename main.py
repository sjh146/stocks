
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
from user_agent import generate_user_agent
from openai import OpenAI
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
    userAgent = generate_user_agent()
    header = userAgent
    print(header)
    chromedriver_path =resource_path("chromedriver.exe")     
    #header='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')  # Optional: run in headless mode
    options.add_argument('user-agent=:' + header)
    options.add_argument("disable-blink-features=AutomationControlled")

    options.add_experimental_option("detach",True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
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
    
   
    time.sleep(2)

    client = OpenAI(api_key="sk-fade8f7c781e42aab15ec3c019e87a50", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "'피치 마켓' 키워드로 글을 쓸거고 블로그 로직을 철저히 준수하면서 해당 용어의 뜻, 중요성,장단점,실제사례(난이도를 주제로), 시사점에 대해서 경험이 포함된 글을 1500자~1800자 수준으로 써줘. 추가적으로 필수적인 부분은 문서에 지나친 단어의 반복이 발생하면 안된다는 점이다. 독창적이면서도, 정보가 정확한 글을 작성해줘야되! 마치 사람이 글을 쓰는 것 처럼 말이야! 타인의 글을 그대로 베끼거나 중복된 문서는 절대 안되. 너의 생각을 담아줘! SEO(search engine optimazation) 최적화 작업도 같이 부탁할게. 다만 단어들이 자주 반복되지 않도록 다른 용어로 대체해서 사용해줘 블로그 로직의 핵심은 동일한 단어가 반복되지 않아야 하기 때문이야! 인간이 쓴 글 처럼 자연스럽게 부탁할게! 기계가 쓴 글로 판독이 되면 절대 안되!"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

    print(response.choices[0].message.content)
    actions.send_keys(response.choices[0].message.content).perform()
    
    
       
eel.start('index.html', size=(600, 400))
