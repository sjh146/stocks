import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton
from PyQt5.QtCore import Qt
#from CrawlingChrome import items_to_select as cc
#from CrawlingChrome import Crawl 
import pandas as ps  
from selenium import webdriver
from selenium.webdriver.chrome import service

from selenium.webdriver.common.by import By
from io import StringIO
try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    os.chdir(os.getcwd())
class MyApp(QWidget):

    
    items_to_select =[] 
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
        fbtn.clicked.connect(self.Pbtn)

        
        self.setGeometry(300, 300, 300, 200)
        self.show()

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

    
    def Pbtn(self):
        
       self.Crawl()

    
#브라우저
    

    def Crawl():
   
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        options.use_chromium = True
        options.add_experimental_option('detach',True)

        options.binary_location ="C:\Program Files\Google\Chrome\Application\chrome.exe"
        s = service.Service("./chromedriver-win64")
        #"C:/Users/Admin/chromedriver-win64/chromedriver-win64"
        #"./chromedriver-win64"
        browser=webdriver.Chrome(options=options, service = s)
        browser.maximize_window()

        url='https://finance.naver.com/sise/sise_market_sum.naver?&page='
        browser.get(url)

        checkboxes=browser.find_elements(By.NAME,'fieldIds')
        for checkbox in checkboxes:
            if checkbox.is_selected():
                checkbox.click()


        for checkbox in checkboxes:
            parent=checkbox.find_element(By.XPATH,'..')
            label=parent.find_element(By.TAG_NAME,'label')
            # print(label.text)
            if label.text in items_to_select:
                checkbox.click()

        btn_apply=browser.find_element(By.XPATH,'//a[@href="javascript:fieldSubmit()"]')

        btn_apply.click()

        for idx in range(1,40): #1이상 40미만 페이지 반복
        #사전 작업:페이지 이동
    
            browser.get(url+str(idx))# http://naver.com....$page=2
    
    
            df=ps.read_html(StringIO(browser.page_source))[1]
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

        browser.quit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
