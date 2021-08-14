from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,QTimer,QDateTime,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

import sys
from uiCounter import *



class MainWindow(QMainWindow) : 
    def __init__(self) : 
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #setup shadow 
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 248, 136, 150))

        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        #create fuction that help us to move our interface on the desktop
        def moveWindow(cursor) : 
            if self.isMaximized()==False:
                if cursor.buttons()==Qt.LeftButton : 
                    self.move(self.pos() + cursor.globalPos() - self.clickPosition)
                    self.clickPosition = cursor.globalPos()
                    cursor.accept()

        self.ui.head.mouseMoveEvent = moveWindow

        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        self.ui.closeButton.clicked.connect(lambda: self.close())

        #initialize text on label
        self.ui.desplay.setText("00:00:00")
        #define variables of the counter
        self.sec,self.min,self.hrs = 0, 0, 0
        self.timer = QTimer()
        #connect content of counter function
        self.timer.timeout.connect(self.counter)
        #connect buttons to there fuctions
        self.ui.start.clicked.connect(self.start)
        self.ui.stop.clicked.connect(self.pause)
        self.ui.reset.clicked.connect(self.reset)


        self.show()

    def mousePressEvent(self, event):

        self.clickPosition = event.globalPos()

    #stop counting 
    def pause(self):
        self.timer.stop()
        self.ui.start.setEnabled(True)
        self.ui.stop.setEnabled(False)

    #start counting what ever values of the time
    def start(self):
        self.timer.start(1000)
        self.ui.start.setEnabled(False)
        self.ui.stop.setEnabled(True)

    #reset fuction to reset counting to zero
    def reset(self): 
        self.sec, self.min, self.hrs = 0, 0, 0
        self.ui.desplay.setText("{:0=2d}:{:0=2d}:{:0=2d}".format(self.hrs,self.min,self.sec))
    
    #a simple function to counting seconds, minits and hours
    def counter(self):
        self.sec+=1
        # if seconds are  equal 60 add one on minits and restart counting 
        if self.sec/60==1 :
            self.min+=1
            self.sec = 0
        #if minits are equal 60 add one on hours and restart counting
        elif self.min/60==1 :
            self.hrs+=1
            self.min=0
        #desplay changes in our label
        self.ui.desplay.setText("{:0=2d}:{:0=2d}:{:0=2d}".format(self.hrs,self.min,self.sec))
        


if __name__=='__main__' :
    app =QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_()) 

