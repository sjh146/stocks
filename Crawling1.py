import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton
from PyQt5.QtCore import Qt

import pandas as ps  
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from io import StringIO
from user_agent import generate_user_agent, generate_navigator
import time

class MyApp(QWidget):
    def resource_path(relative_path):
      
        try:
         # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    
    navigator = generate_navigator()
    print(navigator)
    print(navigator['platform'])
        
    header=generate_user_agent(os='win', device_type='desktop')
    #header='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    chromedriver_path = resource_path("chromedriver.exe")
        
    options = webdriver.ChromeOptions()
    options.add_argument('user-agent=' + header)
    options.add_argument("disable-blink-features=AutomationControlled")

    options.add_experimental_option("detach",True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
        
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')  # Optional: run in headless mode
    service = Service(executable_path=chromedriver_path)
    

    MarketPrice='시가'
    TradingVolume='거래량'
    CostLiness='고가'
    LowPrice='저가'
    BidPrice='매수호가'
    
    def __init__(self):
        super().__init__()
        self.initUI()
   
    def initUI(self):
         
        tv = QCheckBox(self.TradingVolume, self)
        tv.move(30, 30)
        tv.stateChanged.connect(self.ServeTv)

        mp = QCheckBox(self.MarketPrice, self)
        mp.move(30, 60)
        mp.stateChanged.connect(self.ServeMp)      

        cl = QCheckBox(self.CostLiness, self)
        cl.move(30, 90)
        cl.stateChanged.connect(self.ServeCl)


        lp = QCheckBox(self.LowPrice, self)
        lp.move(100, 30)
        lp.stateChanged.connect(self.ServeLp)

        bp = QCheckBox(self.BidPrice, self)
        bp.move(100, 60)
        bp.stateChanged.connect(self.ServeBp)

        fbtn = QPushButton('완료',self)
        fbtn.move(100,90)
        fbtn.setCheckable(False)
        fbtn.clicked.connect(self.Crawl)

        
        self.setGeometry(300, 300, 300, 200)
        self.show()
    items_to_select =[] 
    def ServeTv(self, state):
        if state == Qt.Checked:
           self.items_to_select.append(self.TradingVolume)

        

    def ServeMp(self, state):
        if state == Qt.Checked:
           self.items_to_select.append(self.MarketPrice)

       
    def ServeCl(self, state):
        if state == Qt.Checked:
           self.items_to_select.append(self.CostLiness)

     
    def ServeLp(self, state):
        if state == Qt.Checked:
           self.items_to_select.append(self.LowPrice)

       
    def ServeBp(self, state):
        if state == Qt.Checked:
           self.items_to_select.append(self.BidPrice)

    def resource_path(relative_path):
      
        try:
         # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    
    def Crawl(self):
        
        driver = webdriver.Chrome(service=MyApp.service)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        url='https://finance.naver.com/sise/sise_market_sum.naver?&page='
        driver.get(url)
        print(driver.title)
        time.sleep(1)
        

        checkboxes=driver.find_elements(By.NAME,'fieldIds')
        for checkbox in checkboxes:
            if checkbox.is_selected():
                checkbox.click()


        for checkbox in checkboxes:
            parent=checkbox.find_element(By.XPATH,'..')
            label=parent.find_element(By.TAG_NAME,'label')
            # print(label.text)
            if label.text in MyApp.items_to_select:
                checkbox.click()

        btn_apply=driver.find_element(By.XPATH,'//a[@href="javascript:fieldSubmit()"]')

        btn_apply.click()

        for idx in range(1,40): #1이상 40미만 페이지 반복
        #사전 작업:페이지 이동
    
            driver.get(url+str(idx))# http://naver.com....$page=2
    
    
            df=ps.read_html(StringIO(driver.page_source))[1]
            df.dropna(axis='index',how='all',inplace=True)
            df.dropna(axis='columns',how='all',inplace=True)
            if len(df)==0:# 더이상가져올 데이터 없으면?
                break

        #파일 저장
            f_name='sise.csv'
            if os.path.exists(f_name):#파일이 있다면?헤더 제외
                df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
            else:#파일이 없다면? 헤더포함
                df.to_csv(f_name, encoding='utf-8-sig', index=False)
    
            print(f'{idx}페이지완료')
        
        driver.quit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
