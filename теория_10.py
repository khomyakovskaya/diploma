# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'теория_10.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Teoria10Window(object):
    def setupUi(self, Teoria10Window):
        Teoria10Window.setObjectName("Teoria10Window")
        Teoria10Window.resize(1041, 686)
        Teoria10Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Teoria10Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(211, 239, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setStyleSheet("background-color: rgb(191, 216, 230);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 10, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_return10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_return10.sizePolicy().hasHeightForWidth())
        self.btn_return10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_return10.setFont(font)
        self.btn_return10.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_return10.setObjectName("btn_return10")
        self.horizontalLayout.addWidget(self.btn_return10)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_oglavlenie10 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btn_oglavlenie10.setFont(font)
        self.btn_oglavlenie10.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_oglavlenie10.setObjectName("btn_oglavlenie10")
        self.horizontalLayout.addWidget(self.btn_oglavlenie10)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_glavnaya10 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_glavnaya10.setFont(font)
        self.btn_glavnaya10.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_glavnaya10.setObjectName("btn_glavnaya10")
        self.horizontalLayout.addWidget(self.btn_glavnaya10)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btn_dalee10 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_dalee10.setFont(font)
        self.btn_dalee10.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_dalee10.setObjectName("btn_dalee10")
        self.horizontalLayout.addWidget(self.btn_dalee10)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 9, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("background-color: rgb(191, 216, 230);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("рис7.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        Teoria10Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Teoria10Window)
        self.statusbar.setObjectName("statusbar")
        Teoria10Window.setStatusBar(self.statusbar)

        self.retranslateUi(Teoria10Window)
        QtCore.QMetaObject.connectSlotsByName(Teoria10Window)

    def retranslateUi(self, Teoria10Window):
        _translate = QtCore.QCoreApplication.translate
        Teoria10Window.setWindowTitle(_translate("Teoria10Window", "АУК"))
        self.label.setText(_translate("Teoria10Window", "Паровой тракт"))
        self.textBrowser.setHtml(_translate("Teoria10Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">- потолочный экран (ПЭ),</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">- ширмы (ШПП),</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">- конвективный пароперегреватель (КПП в/д).</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">На трубопроводе между ПЭ и ШПП расположена встроенная задвижка (ВЗ), которая байпасируется встроенными сепараторами с соответствующей дроссельной арматурой. Тракт промежуточного пароперегревателя состоит из двух потоков. По ходу пара в каждом потоке последовательно установлено две ступени пароперегревателя.</span><span style=\" font-size:8pt;\"> </span></p></body></html>"))
        self.btn_return10.setText(_translate("Teoria10Window", "Назад"))
        self.btn_oglavlenie10.setText(_translate("Teoria10Window", "Оглавление"))
        self.btn_glavnaya10.setText(_translate("Teoria10Window", "На главную"))
        self.btn_dalee10.setText(_translate("Teoria10Window", "Далее"))
        self.label_3.setText(_translate("Teoria10Window", "Рис. 7. Пароводяной тракт котла ТГМП-314П"))
