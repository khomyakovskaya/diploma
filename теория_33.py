# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'теория_33.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Teoria33Window(object):
    def setupUi(self, Teoria33Window):
        Teoria33Window.setObjectName("Teoria33Window")
        Teoria33Window.resize(1041, 682)
        Teoria33Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Teoria33Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(211, 239, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setStyleSheet("background-color: rgb(191, 216, 230);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 6, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("background-color: rgb(191, 216, 230);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_return33 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_return33.sizePolicy().hasHeightForWidth())
        self.btn_return33.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_return33.setFont(font)
        self.btn_return33.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_return33.setObjectName("btn_return33")
        self.horizontalLayout.addWidget(self.btn_return33)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_oglavlenie33 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btn_oglavlenie33.setFont(font)
        self.btn_oglavlenie33.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_oglavlenie33.setObjectName("btn_oglavlenie33")
        self.horizontalLayout.addWidget(self.btn_oglavlenie33)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_glavnaya33 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_glavnaya33.setFont(font)
        self.btn_glavnaya33.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_glavnaya33.setObjectName("btn_glavnaya33")
        self.horizontalLayout.addWidget(self.btn_glavnaya33)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btn_dalee33 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_dalee33.setFont(font)
        self.btn_dalee33.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_dalee33.setObjectName("btn_dalee33")
        self.horizontalLayout.addWidget(self.btn_dalee33)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("рис21.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        Teoria33Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Teoria33Window)
        self.statusbar.setObjectName("statusbar")
        Teoria33Window.setStatusBar(self.statusbar)

        self.retranslateUi(Teoria33Window)
        QtCore.QMetaObject.connectSlotsByName(Teoria33Window)

    def retranslateUi(self, Teoria33Window):
        _translate = QtCore.QCoreApplication.translate
        Teoria33Window.setWindowTitle(_translate("Teoria33Window", "АУК"))
        self.label_3.setText(_translate("Teoria33Window", "Перечень операций по снижению нагрузки блока до 50 - 60 %"))
        self.btn_return33.setText(_translate("Teoria33Window", "Назад"))
        self.btn_oglavlenie33.setText(_translate("Teoria33Window", "Оглавление"))
        self.btn_glavnaya33.setText(_translate("Teoria33Window", "На главную"))
        self.btn_dalee33.setText(_translate("Teoria33Window", "Далее"))
        self.textBrowser.setHtml(_translate("Teoria33Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">- отключается воздействие регулятора мощности блока на работающий регулятор топлива и к последнему подключается задатчик 50</span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">¸</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">60 % нагрузки.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">Защиты, действующие на снижение нагрузки блока, при отключении одного из двух работающих ДВ, ДС или РВП выводятся автоматически при нагрузке ниже 60 % (по давлению в камере регулирующей ступени), а вводятся автоматически при включении в работу обоих одноименных механизмов.</span><span style=\" font-size:8pt;\"> </span></p></body></html>"))
        self.label_2.setText(_translate("Teoria33Window", "Рис. 21. Схема энергоблока"))
