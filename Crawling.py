import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mp = QCheckBox('시가', self)
        mp.move(20, 20)
        mp.stateChanged.connect(self.changeTitle)

        tv = QCheckBox('거래량', self)
        tv.move(20, 20)
        tv.stateChanged.connect(self.changeTitle)

        cl = QCheckBox('고가', self)
        cl.move(20, 20)
        cl.stateChanged.connect(self.changeTitle)

        lp = QCheckBox('저가', self)
        lp.move(20, 20)
        lp.stateChanged.connect(self.changeTitle)

        bp = QCheckBox('매수호가', self)
        bp.move(20, 20)
        bp.stateChanged.connect(self.changeTitle)





        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())