# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'теория_8.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Teoria8Window(object):
    def setupUi(self, Teoria8Window):
        Teoria8Window.setObjectName("Teoria8Window")
        Teoria8Window.resize(1041, 686)
        Teoria8Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Teoria8Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setStyleSheet("background-color: rgb(191, 216, 230);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 12, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(211, 239, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_return8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_return8.sizePolicy().hasHeightForWidth())
        self.btn_return8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_return8.setFont(font)
        self.btn_return8.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_return8.setObjectName("btn_return8")
        self.horizontalLayout.addWidget(self.btn_return8)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_oglavlenie8 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btn_oglavlenie8.setFont(font)
        self.btn_oglavlenie8.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_oglavlenie8.setObjectName("btn_oglavlenie8")
        self.horizontalLayout.addWidget(self.btn_oglavlenie8)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_glavnaya8 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_glavnaya8.setFont(font)
        self.btn_glavnaya8.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_glavnaya8.setObjectName("btn_glavnaya8")
        self.horizontalLayout.addWidget(self.btn_glavnaya8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btn_dalee8 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_dalee8.setFont(font)
        self.btn_dalee8.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_dalee8.setObjectName("btn_dalee8")
        self.horizontalLayout.addWidget(self.btn_dalee8)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 11, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("background-color: rgb(191, 216, 230);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 10, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("рис6.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 7, 0, 1, 1)
        Teoria8Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Teoria8Window)
        self.statusbar.setObjectName("statusbar")
        Teoria8Window.setStatusBar(self.statusbar)

        self.retranslateUi(Teoria8Window)
        QtCore.QMetaObject.connectSlotsByName(Teoria8Window)

    def retranslateUi(self, Teoria8Window):
        _translate = QtCore.QCoreApplication.translate
        Teoria8Window.setWindowTitle(_translate("Teoria8Window", "АУК"))
        self.label_6.setText(_translate("Teoria8Window", "Горелочные устройства"))
        self.textBrowser_2.setHtml(_translate("Teoria8Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">На периферийном и центральнном каналах установлены завихрители, обеспечивающие крутку газо-воздушной смеси при температуре окружающего воздуха в диапазоне от минус 30°С (с использованием рециркуляции подогретого воздуха) до плюс 45°С. Расход мазута на горелку при номинальной нагрузке котла составляет 8,9 т/ч. Расход газа на горелку при номинальной нагрузке котла составляет 10,5</span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">×</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">10</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt; vertical-align:super;\">3</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> нм</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt; vertical-align:super;\">3</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">/ч. Для сжигания мазута применяются паромеханические форсунки типа &quot;Эдипол&quot;. Каждая горелка имеет два газовых канала - центральный и периферийный.</span><span style=\" font-size:8pt;\"> </span></p></body></html>"))
        self.btn_return8.setText(_translate("Teoria8Window", "Назад"))
        self.btn_oglavlenie8.setText(_translate("Teoria8Window", "Оглавление"))
        self.btn_glavnaya8.setText(_translate("Teoria8Window", "На главную"))
        self.btn_dalee8.setText(_translate("Teoria8Window", "Далее"))
        self.label.setText(_translate("Teoria8Window", "Рис. 6. Схема подачи газа в топку котла"))
