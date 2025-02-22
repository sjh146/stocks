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
    items=[]
    def __init__(self):
        super().__init__()
        self.initUI()
   
    def initUI(self):
         
        tv = QCheckBox('1', self)
        tv.move(30, 30)
        tv.stateChanged.connect(self.ServeTv)
        self.setGeometry(300, 300, 300, 200)
        self.show()
  
    def ServeTv(self, state):
        if state == Qt.Checked:
           MyApp.connect()
    
    def resource_path(relative_path):
      
        try:
         # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    
    def connect():
        navigator = generate_navigator()
        print(navigator)
        print(navigator['platform'])
            
        header=generate_user_agent(os='win', device_type='desktop')
        #header='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
        chromedriver_path = MyApp.resource_path("chromedriver.exe")
            
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=' + header)
        options.add_argument("disable-blink-features=AutomationControlled")

        options.add_experimental_option("detach",True)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
            
        #options.add_argument('--headless')
        #options.add_argument('--disable-gpu')  # Optional: run in headless mode
        service = Service(executable_path=chromedriver_path)

        driver = webdriver.Chrome(service=service)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        url='https://finance.naver.com/sise/sise_market_sum.naver?&page='
        driver.get(url)
        print(driver.title)
        time.sleep(1)












if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
