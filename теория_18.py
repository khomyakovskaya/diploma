# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'теория_18.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Teoria18Window(object):
    def setupUi(self, Teoria18Window):
        Teoria18Window.setObjectName("Teoria18Window")
        Teoria18Window.resize(1041, 686)
        Teoria18Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Teoria18Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("рис12.png"))
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
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(211, 239, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setStyleSheet("background-color: rgb(191, 216, 230);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 8, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_return18 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_return18.sizePolicy().hasHeightForWidth())
        self.btn_return18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_return18.setFont(font)
        self.btn_return18.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_return18.setObjectName("btn_return18")
        self.horizontalLayout.addWidget(self.btn_return18)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_oglavlenie18 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btn_oglavlenie18.setFont(font)
        self.btn_oglavlenie18.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_oglavlenie18.setObjectName("btn_oglavlenie18")
        self.horizontalLayout.addWidget(self.btn_oglavlenie18)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_glavnaya18 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_glavnaya18.setFont(font)
        self.btn_glavnaya18.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_glavnaya18.setObjectName("btn_glavnaya18")
        self.horizontalLayout.addWidget(self.btn_glavnaya18)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btn_dalee18 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_dalee18.setFont(font)
        self.btn_dalee18.setStyleSheet("background-color: rgb(211, 239, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_dalee18.setObjectName("btn_dalee18")
        self.horizontalLayout.addWidget(self.btn_dalee18)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("background-color: rgb(191, 216, 230);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 4, 0, 1, 1)
        Teoria18Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Teoria18Window)
        self.statusbar.setObjectName("statusbar")
        Teoria18Window.setStatusBar(self.statusbar)

        self.retranslateUi(Teoria18Window)
        QtCore.QMetaObject.connectSlotsByName(Teoria18Window)

    def retranslateUi(self, Teoria18Window):
        _translate = QtCore.QCoreApplication.translate
        Teoria18Window.setWindowTitle(_translate("Teoria18Window", "АУК"))
        self.label_2.setText(_translate("Teoria18Window", "Рис. 12. Встроенный сепаратор"))
        self.textBrowser_2.setHtml(_translate("Teoria18Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> Пройдя конический рассекатель и лопатки завихрителя, поток разделяется: вода отбрасывается к наружным стенкам и через горизонтальный штуцер, по трубопроводу </span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">Æ</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> 219</span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">´</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">30 с дроссельным клапаном Д-2 Ду-100, направляется в растопочный расширитель, а пар - через диффузор в нижнем донышке по трубопроводу с дроссельными клапаном Д-З Ду-100 - в коллектор за встроенной задвижкой </span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">Æ</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> 325</span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">´</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\">45, на котором установлен пароохладитель (впрыск 1), а из него десятью трубами </span><span style=\" font-family:\'Symbol\'; font-size:14pt;\">Æ</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> 106х14 подводится к ШПП 1 ст. </span></p></body></html>"))
        self.label_4.setText(_translate("Teoria18Window", "Встроенные сепараторы"))
        self.btn_return18.setText(_translate("Teoria18Window", "Назад"))
        self.btn_oglavlenie18.setText(_translate("Teoria18Window", "Оглавление"))
        self.btn_glavnaya18.setText(_translate("Teoria18Window", "На главную"))
        self.btn_dalee18.setText(_translate("Teoria18Window", "Далее"))
