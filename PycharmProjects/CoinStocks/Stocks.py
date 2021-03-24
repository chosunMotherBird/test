"""
tikers = pyupbit.get_tickers(fiat = "KRW")
print(tikers)

price = pyupbit.get_current_price("KRW-TRX")
print(price)

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pyupbit

form_class = uic.loadUiType("cointest.ui")[0]

class Mywindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)

    def inquiry(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        price = pyupbit.get_current_price("KRW-TRX")
        self.lineEdit.setText(str(price))

app = QApplication(sys.argv)
window = Mywindow()
window.show()
app.exec_()




