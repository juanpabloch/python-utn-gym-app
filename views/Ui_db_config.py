# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'db_config.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class NewDBConfForm(object):
    def setupUi(self, NewDBConfForm):
        if not NewDBConfForm.objectName():
            NewDBConfForm.setObjectName(u"NewDBConfForm")
        NewDBConfForm.resize(885, 539)
        self.label = QLabel(NewDBConfForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 821, 41))
        self.label.setStyleSheet(u"font-size:30px; \n"
"color:#3c2934;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"font-weight: 600;\n"
"")
        self.label.setFrameShape(QFrame.Box)
        self.labelHost = QLabel(NewDBConfForm)
        self.labelHost.setObjectName(u"labelHost")
        self.labelHost.setGeometry(QRect(60, 110, 101, 31))
        self.hostLineEdit = QLineEdit(NewDBConfForm)
        self.hostLineEdit.setObjectName(u"hostLineEdit")
        self.hostLineEdit.setGeometry(QRect(60, 150, 351, 31))
        self.labelDB = QLabel(NewDBConfForm)
        self.labelDB.setObjectName(u"labelDB")
        self.labelDB.setGeometry(QRect(60, 200, 101, 31))
        self.databaseLineEdit = QLineEdit(NewDBConfForm)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")
        self.databaseLineEdit.setGeometry(QRect(60, 240, 351, 31))
        self.labelUser = QLabel(NewDBConfForm)
        self.labelUser.setObjectName(u"labelUser")
        self.labelUser.setGeometry(QRect(60, 290, 101, 31))
        self.userLineEdit = QLineEdit(NewDBConfForm)
        self.userLineEdit.setObjectName(u"userLineEdit")
        self.userLineEdit.setGeometry(QRect(60, 330, 351, 31))
        self.label_5 = QLabel(NewDBConfForm)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(510, 110, 141, 31))
        self.dbComboBox = QComboBox(NewDBConfForm)
        self.dbComboBox.setObjectName(u"dbComboBox")
        self.dbComboBox.setGeometry(QRect(510, 150, 191, 31))
        font = QFont()
        font.setPointSize(12)
        self.dbComboBox.setFont(font)
        self.sendDBConfBtn = QPushButton(NewDBConfForm)
        self.sendDBConfBtn.setObjectName(u"sendDBConfBtn")
        self.sendDBConfBtn.setGeometry(QRect(510, 460, 151, 41))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.sendDBConfBtn.setFont(font1)
        self.sendDBConfBtn.setStyleSheet(u"#sendDBConfBtn{\n"
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
"#sendDBConfBtn:hover{\n"
"	color: rgb(17, 17, 17);\n"
"	border:1px solid rgb(225, 225, 225);\n"
"}")
        self.cancelNewDBBtn = QPushButton(NewDBConfForm)
        self.cancelNewDBBtn.setObjectName(u"cancelNewDBBtn")
        self.cancelNewDBBtn.setGeometry(QRect(700, 460, 151, 41))
        self.cancelNewDBBtn.setFont(font1)
        self.cancelNewDBBtn.setStyleSheet(u"#cancelNewDBBtn{\n"
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
"#cancelNewDBBtn:hover{\n"
"	color: rgb(255, 0, 0);\n"
"	border:1px solid rgb(225, 225, 225);\n"
"}")
        self.passLineEdit = QLineEdit(NewDBConfForm)
        self.passLineEdit.setObjectName(u"passLineEdit")
        self.passLineEdit.setGeometry(QRect(60, 420, 351, 31))
        self.labelPass = QLabel(NewDBConfForm)
        self.labelPass.setObjectName(u"labelPass")
        self.labelPass.setGeometry(QRect(60, 380, 101, 31))
        self.testResultDBLabel = QLabel(NewDBConfForm)
        self.testResultDBLabel.setObjectName(u"testResultDBLabel")
        self.testResultDBLabel.setGeometry(QRect(500, 290, 341, 31))
        font2 = QFont()
        font2.setFamily(u"Verdana")
        font2.setPointSize(12)
        self.testResultDBLabel.setFont(font2)
        self.testResultDBLabel.setStyleSheet(u"")
        self.testDBConfBtn = QPushButton(NewDBConfForm)
        self.testDBConfBtn.setObjectName(u"testDBConfBtn")
        self.testDBConfBtn.setGeometry(QRect(510, 230, 321, 41))
        self.testDBConfBtn.setFont(font1)
        self.testDBConfBtn.setStyleSheet(u"#testDBConfBtn{\n"
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
"#testDBConfBtn:hover{\n"
"	color: rgb(17, 17, 17);\n"
"	border:1px solid rgb(225, 225, 225);\n"
"}")

        self.retranslateUi(NewDBConfForm)

        QMetaObject.connectSlotsByName(NewDBConfForm)
    # setupUi

    def retranslateUi(self, NewDBConfForm):
        NewDBConfForm.setWindowTitle(QCoreApplication.translate("NewDBConfForm", u"new_socio_window", None))
        self.label.setText(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CONFIGURAR DB</span></p></body></html>", None))
        self.labelHost.setText(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Host: </span></p></body></html>", None))
        self.labelDB.setText(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Database: </span></p></body></html>", None))
        self.labelUser.setText(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">User: </span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Seleccionar DB: </span></p></body></html>", None))
        self.sendDBConfBtn.setText(QCoreApplication.translate("NewDBConfForm", u"Agregar", None))
        self.cancelNewDBBtn.setText(QCoreApplication.translate("NewDBConfForm", u"Cancelar", None))
        self.labelPass.setText(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Password: </span></p></body></html>", None))
        self.testResultDBLabel.setText("")
        self.testDBConfBtn.setText(QCoreApplication.translate("NewDBConfForm", u"Testear conexi\u00f3n", None))
    # retranslateUi

