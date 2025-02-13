import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton
from PyQt5.QtCore import Qt
from CrawlingChrome import items_to_select as cc
from CrawlingChrome import Crawl 

try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    os.chdir(os.getcwd())
class MyApp(QWidget):

    
    
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
           cc.append(self.TradingVolume)

        

    def ServeMp(self, state):
        if state == Qt.Checked:
           cc.append(self.MarketPrice)

       
    def ServeCl(self, state):
        if state == Qt.Checked:
           cc.append(self.CostLiness)

     
    def ServeLp(self, state):
        if state == Qt.Checked:
           cc.append(self.LowPrice)

       
    def ServeBp(self, state):
        if state == Qt.Checked:
           cc.append(self.BidPrice)

       

   

    def Pbtn(self):
        
       Crawl()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
   

