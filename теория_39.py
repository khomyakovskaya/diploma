# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'теория_39.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Teoria39Window(object):
    def setupUi(self, Teoria39Window):
        Teoria39Window.setObjectName("Teoria39Window")
        Teoria39Window.resize(1053, 677)
        Teoria39Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Teoria39Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
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
        self.btn_return39 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_return39.sizePolicy().hasHeightForWidth())
        self.btn_return39.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_return39.setFont(font)
        self.btn_return39.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_return39.setObjectName("btn_return39")
        self.horizontalLayout.addWidget(self.btn_return39)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_oglavlenie39 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btn_oglavlenie39.setFont(font)
        self.btn_oglavlenie39.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_oglavlenie39.setObjectName("btn_oglavlenie39")
        self.horizontalLayout.addWidget(self.btn_oglavlenie39)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_glavnaya39 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_glavnaya39.setFont(font)
        self.btn_glavnaya39.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_glavnaya39.setObjectName("btn_glavnaya39")
        self.horizontalLayout.addWidget(self.btn_glavnaya39)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("рис25.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(211, 239, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        Teoria39Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Teoria39Window)
        self.statusbar.setObjectName("statusbar")
        Teoria39Window.setStatusBar(self.statusbar)

        self.retranslateUi(Teoria39Window)
        QtCore.QMetaObject.connectSlotsByName(Teoria39Window)

    def retranslateUi(self, Teoria39Window):
        _translate = QtCore.QCoreApplication.translate
        Teoria39Window.setWindowTitle(_translate("Teoria39Window", "АУК"))
        self.textBrowser.setHtml(_translate("Teoria39Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">Блокировка на запрет открытия задвижек и включение ЗЗУ на горелки    № 2,3, 5,8 (1, 4, 6, 7) снимается после ввода защиты по погасанию общего факела в топке переводом ключа управления 2ПЗ в положение &quot;Включено&quot;.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">Оперативному персоналу КТО, совместно с оперативным персоналом ЦТАИ производить опробование защит на &quot;сигнал&quot;, в соответствии с графиком опробования защит энергоблоков.</span><span style=\" font-size:8pt;\"> </span></p></body></html>"))
        self.btn_return39.setText(_translate("Teoria39Window", "Назад"))
        self.btn_oglavlenie39.setText(_translate("Teoria39Window", "Оглавление"))
        self.btn_glavnaya39.setText(_translate("Teoria39Window", "На главную"))
        self.label_3.setText(_translate("Teoria39Window", "Условия локальных защит и блокировок котлоагрегата \n"
" и его  вспомогательного оборудования"))
        self.label.setText(_translate("Teoria39Window", "Рис. 25. Схема газового тракта котла"))
