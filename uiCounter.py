from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,QTimer,QDateTime,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frontInterface = QFrame(self.centralwidget)
        self.frontInterface.setObjectName(u"frontInterface")
        self.frontInterface.setGeometry(QRect(230, 120, 280, 160))
        self.frontInterface.setMinimumSize(QSize(280, 160))
        self.frontInterface.setMaximumSize(QSize(280, 160))
        self.frontInterface.setStyleSheet(u"background-color : #fff;\n"
"border-radius : 10px;")
        self.frontInterface.setFrameShape(QFrame.StyledPanel)
        self.frontInterface.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frontInterface)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.head = QFrame(self.frontInterface)
        self.head.setObjectName(u"head")
        self.head.setMinimumSize(QSize(0, 30))
        self.head.setMaximumSize(QSize(16777215, 30))
        self.head.setStyleSheet(u"border : none;\n"
"border-radius : 0px;\n"
"background-color : transparent;")
        self.head.setFrameShape(QFrame.StyledPanel)
        self.head.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.head)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.title = QFrame(self.head)
        self.title.setObjectName(u"title")
        self.title.setFrameShape(QFrame.StyledPanel)
        self.title.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.title)

        self.headButtons = QFrame(self.head)
        self.headButtons.setObjectName(u"headButtons")
        self.headButtons.setMinimumSize(QSize(50, 0))
        self.headButtons.setMaximumSize(QSize(50, 16777215))
        self.headButtons.setFrameShape(QFrame.StyledPanel)
        self.headButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.headButtons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.headButtons)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(20, 20))
        self.minimizeButton.setMaximumSize(QSize(20, 20))
        self.minimizeButton.setStyleSheet(u"QPushButton{\n"
"	background-color : rgb(50, 50, 50);\n"
"	border : none;\n"
"	border-radius : 10px;\n"
"	color : rgb(104, 104, 104);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color : rgb(49, 255, 66);\n"
"}")

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.closeButton = QPushButton(self.headButtons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(20, 20))
        self.closeButton.setMaximumSize(QSize(20, 20))
        self.closeButton.setLayoutDirection(Qt.LeftToRight)
        self.closeButton.setStyleSheet(u"QPushButton{\n"
"	background-color : rgb(50, 50, 50);\n"
"	border : none;\n"
"	border-radius : 10px;\n"
"	color : rgb(104, 104, 104);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color : rgb(255, 69, 88);\n"
"}")

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout_2.addWidget(self.headButtons)


        self.verticalLayout.addWidget(self.head)

        self.timeDesplay = QFrame(self.frontInterface)
        self.timeDesplay.setObjectName(u"timeDesplay")
        self.timeDesplay.setStyleSheet(u"border : none;\n"
"background-color : transparent;")
        self.timeDesplay.setFrameShape(QFrame.StyledPanel)
        self.timeDesplay.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.timeDesplay)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.desplay = QLabel(self.timeDesplay)
        self.desplay.setObjectName(u"desplay")
        self.desplay.setStyleSheet(u"font: 28pt \"cmr10\";\n"
"color : rgb(0, 0, 0)")
        self.desplay.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.desplay)


        self.verticalLayout.addWidget(self.timeDesplay)

        self.countingButtons = QFrame(self.frontInterface)
        self.countingButtons.setObjectName(u"countingButtons")
        self.countingButtons.setStyleSheet(u"border : none;\n"
"background-color : transparent;")
        self.countingButtons.setFrameShape(QFrame.StyledPanel)
        self.countingButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.countingButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reset = QPushButton(self.countingButtons)
        self.reset.setObjectName(u"reset")
        self.reset.setMinimumSize(QSize(0, 30))
        self.reset.setMaximumSize(QSize(16777215, 30))
        self.reset.setStyleSheet(u"QPushButton{\n"
"	background-color : rgb(65, 122, 255);\n"
"	border :none;\n"
"	border-radius : 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	border : 2px solid rgb(255, 86, 52);\n"
"}")

        self.horizontalLayout.addWidget(self.reset)

        self.start = QPushButton(self.countingButtons)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(0, 30))
        self.start.setMaximumSize(QSize(16777215, 30))
        self.start.setStyleSheet(u"QPushButton{\n"
"	background-color : rgb(65, 122, 255);\n"
"	border :none;\n"
"	border-radius : 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	border : 2px solid rgb(255, 86, 52);\n"
"}")

        self.horizontalLayout.addWidget(self.start)

        self.stop = QPushButton(self.countingButtons)
        self.stop.setObjectName(u"stop")
        self.stop.setMinimumSize(QSize(0, 30))
        self.stop.setMaximumSize(QSize(16777215, 30))
        self.stop.setStyleSheet(u"QPushButton{\n"
"	background-color : rgb(65, 122, 255);\n"
"	border :none;\n"
"	border-radius : 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	border : 2px solid rgb(255, 86, 52);\n"
"}")

        self.horizontalLayout.addWidget(self.stop)


        self.verticalLayout.addWidget(self.countingButtons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minimizeButton.setText("")
        self.closeButton.setText("")
        self.desplay.setText(QCoreApplication.translate("MainWindow", u"label", None))
        self.reset.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
    # retranslateUi

