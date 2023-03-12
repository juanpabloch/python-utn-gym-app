# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lista_cobros.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ListaCobro(object):
    def setupUi(self, ListaCobro):
        if not ListaCobro.objectName():
            ListaCobro.setObjectName(u"ListaCobro")
        ListaCobro.resize(703, 682)
        self.label = QLabel(ListaCobro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 601, 41))
        self.label.setFrameShape(QFrame.Box)
        self.tableListaCobro = QTableWidget(ListaCobro)
        self.tableListaCobro.setObjectName(u"tableListaCobro")
        self.tableListaCobro.setGeometry(QRect(110, 70, 471, 421))
        self.downloadBtn = QPushButton(ListaCobro)
        self.downloadBtn.setObjectName(u"downloadBtn")
        self.downloadBtn.setGeometry(QRect(110, 600, 201, 41))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.downloadBtn.setFont(font)
        self.downloadBtn.setStyleSheet(u"#downloadBtn{\n"
"background-color: #F5F5F5;\n"
"border-radius: 5px;\n"
"color: #392D33;\n"
"padding: 5px;\n"
"font-size: 20px;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"font-weight: 600;\n"
"}\n"
"\n"
"#downloadBtn:hover{\n"
"	color: rgb(17, 17, 17);\n"
"	border:1px solid rgb(225, 225, 225);\n"
"}")
        self.exitBtn = QPushButton(ListaCobro)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setGeometry(QRect(420, 600, 161, 41))
        self.exitBtn.setFont(font)
        self.exitBtn.setStyleSheet(u"#exitBtn{\n"
"background-color: #F5F5F5;\n"
"border-radius: 5px;\n"
"color: #392D33;\n"
"padding: 5px;\n"
"font-size: 20px;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"font-weight: 600;\n"
"}\n"
"\n"
"#exitBtn:hover{\n"
"	color: rgb(255, 0, 0);\n"
"	border:1px solid rgb(225, 225, 225);\n"
"}")
        self.label_2 = QLabel(ListaCobro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 500, 71, 31))
        self.totalLista = QLabel(ListaCobro)
        self.totalLista.setObjectName(u"totalLista")
        self.totalLista.setGeometry(QRect(490, 500, 111, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.totalLista.setFont(font1)
        self.cobro_lista_message = QLabel(ListaCobro)
        self.cobro_lista_message.setObjectName(u"cobro_lista_message")
        self.cobro_lista_message.setGeometry(QRect(120, 550, 451, 41))
        self.cobro_lista_message.setStyleSheet(u"#cobro_lista_message{\n"
"	color: rgb(47, 47, 47);\n"
"	font-size: 12px;\n"
"	text-align: center;\n"
"    font-weight: 500;\n"
"	letter-spacing: 2px;\n"
"}")
        self.cobro_lista_message.setWordWrap(True)

        self.retranslateUi(ListaCobro)

        QMetaObject.connectSlotsByName(ListaCobro)
    # setupUi

    def retranslateUi(self, ListaCobro):
        ListaCobro.setWindowTitle(QCoreApplication.translate("ListaCobro", u"Lista Cobro", None))
        self.label.setText(QCoreApplication.translate("ListaCobro", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Lista de cobros del mes</span></p></body></html>", None))
        self.downloadBtn.setText(QCoreApplication.translate("ListaCobro", u"Generar cobro", None))
        self.exitBtn.setText(QCoreApplication.translate("ListaCobro", u"Salir", None))
        self.label_2.setText(QCoreApplication.translate("ListaCobro", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Total:</span></p></body></html>", None))
        self.totalLista.setText("")
        self.cobro_lista_message.setText("")
    # retranslateUi

