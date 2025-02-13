import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
   
    a=[]

    MarketPrice='시가'
    TradingVolume='거래량'
    CostLiness='고가'
    LowPrice='저가'
    BidPrice='매수호가'

    def initUI(self):
           
        mp = QCheckBox(self.TradingVolume, self)
        mp.move(30, 30)
        mp.stateChanged.connect(self.changeTitle)

        mp = QCheckBox(self.MarketPrice, self)
        mp.move(30, 60)
        mp.stateChanged.connect(self.changeTitle)      

        mp = QCheckBox(self.CostLiness, self)
        mp.move(30, 90)
        mp.stateChanged.connect(self.changeTitle)


        mp = QCheckBox(self.LowPrice, self)
        mp.move(100, 30)
        mp.stateChanged.connect(self.changeTitle)

        mp = QCheckBox(self.BidPrice, self)
        mp.move(100, 60)
        mp.stateChanged.connect(self.changeTitle)

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
           self.a=self

        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())