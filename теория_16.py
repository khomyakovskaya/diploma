# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'теория_16.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Teoria16Window(object):
    def setupUi(self, Teoria16Window):
        Teoria16Window.setObjectName("Teoria16Window")
        Teoria16Window.resize(1041, 686)
        Teoria16Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Teoria16Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("рис11.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(211, 239, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setStyleSheet("background-color: rgb(191, 216, 230);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 7, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_return16 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_return16.sizePolicy().hasHeightForWidth())
        self.btn_return16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_return16.setFont(font)
        self.btn_return16.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_return16.setObjectName("btn_return16")
        self.horizontalLayout.addWidget(self.btn_return16)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_oglavlenie16 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btn_oglavlenie16.setFont(font)
        self.btn_oglavlenie16.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_oglavlenie16.setObjectName("btn_oglavlenie16")
        self.horizontalLayout.addWidget(self.btn_oglavlenie16)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_glavnaya16 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_glavnaya16.setFont(font)
        self.btn_glavnaya16.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_glavnaya16.setObjectName("btn_glavnaya16")
        self.horizontalLayout.addWidget(self.btn_glavnaya16)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btn_dalee16 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_dalee16.setFont(font)
        self.btn_dalee16.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_dalee16.setObjectName("btn_dalee16")
        self.horizontalLayout.addWidget(self.btn_dalee16)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("background-color: rgb(191, 216, 230);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        Teoria16Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Teoria16Window)
        self.statusbar.setObjectName("statusbar")
        Teoria16Window.setStatusBar(self.statusbar)

        self.retranslateUi(Teoria16Window)
        QtCore.QMetaObject.connectSlotsByName(Teoria16Window)

    def retranslateUi(self, Teoria16Window):
        _translate = QtCore.QCoreApplication.translate
        Teoria16Window.setWindowTitle(_translate("Teoria16Window", "АУК"))
        self.label_3.setText(_translate("Teoria16Window", "СРЧ - ВРЧ"))
        self.textBrowser.setHtml(_translate("Teoria16Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">Из смесительного коллектора среда девятью трубами </span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">Æ</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> 133</span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">´</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">15 поступает во входные коллекторы СРЧ-ВРЧ </span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">Æ</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> 159</span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">´</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">28. (СРЧ переходит в ВРЧ без разделительных коллекторов, деление поверхности нагрева на СРЧ и ВРЧ условное). Конструктивно СРЧ-ВРЧ выполнена из 9 панелей, каждая из которых образована 23 змеевиками из труб </span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">Æ</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> 32</span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">´</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">6. Всего в СРЧ-ВРЧ 207 змеевиков на один поток. Горизонтальные змеевики панелей СРЧ-ВРЧ имеют 16 подъемов.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">Пройдя панели СРЧ и ВРЧ (рис. 11), среда поступает в 9 выходных коллекторов </span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">Æ</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> 159</span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">´</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">28, из которых 9 трубами </span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">Æ</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> 133</span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">´</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">15 в смесительный коллектор </span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">Æ</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> 325</span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">´</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">45. Из коллектора пар шестью трубами </span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">Æ</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> 133</span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">´</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">15 поступает в три вертикальных камеры </span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">Æ</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> 219</span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">´</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">32 экрана поворотной камеры, расположенных на фронтовой стене топки в верхней её части. </span></p></body></html>"))
        self.btn_return16.setText(_translate("Teoria16Window", "Назад"))
        self.btn_oglavlenie16.setText(_translate("Teoria16Window", "Оглавление"))
        self.btn_glavnaya16.setText(_translate("Teoria16Window", "На главную"))
        self.btn_dalee16.setText(_translate("Teoria16Window", "Далее"))
        self.label_2.setText(_translate("Teoria16Window", "Рис. 11. СРЧ и ВРЧ в прямоточном котле"))
