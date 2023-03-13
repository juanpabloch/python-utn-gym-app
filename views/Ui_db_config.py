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
        NewDBConfForm.setAutoFillBackground(False)
        NewDBConfForm.setStyleSheet(u"background-color:#ffffff;")
        self.label = QLabel(NewDBConfForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, -10, 801, 91))
        font = QFont()
        font.setFamily(u"Sitka Small")
        font.setBold(True)
        font.setWeight(87)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size:55px; \n"
"color:rgb(227, 227, 227);\n"
"letter-spacing: 0px;\n"
"font-weight: 700;\n"
"")
        self.label.setFrameShape(QFrame.NoFrame)
        self.labelHost = QLabel(NewDBConfForm)
        self.labelHost.setObjectName(u"labelHost")
        self.labelHost.setGeometry(QRect(60, 110, 101, 31))
        self.hostLineEdit = QLineEdit(NewDBConfForm)
        self.hostLineEdit.setObjectName(u"hostLineEdit")
        self.hostLineEdit.setGeometry(QRect(60, 150, 351, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.hostLineEdit.setFont(font1)
        self.hostLineEdit.setStyleSheet(u"padding:0 10px;")
        self.labelDB = QLabel(NewDBConfForm)
        self.labelDB.setObjectName(u"labelDB")
        self.labelDB.setGeometry(QRect(60, 200, 101, 31))
        self.databaseLineEdit = QLineEdit(NewDBConfForm)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")
        self.databaseLineEdit.setGeometry(QRect(60, 240, 351, 31))
        self.databaseLineEdit.setFont(font1)
        self.databaseLineEdit.setStyleSheet(u"padding:0 10px;")
        self.labelUser = QLabel(NewDBConfForm)
        self.labelUser.setObjectName(u"labelUser")
        self.labelUser.setGeometry(QRect(60, 290, 101, 31))
        self.userLineEdit = QLineEdit(NewDBConfForm)
        self.userLineEdit.setObjectName(u"userLineEdit")
        self.userLineEdit.setGeometry(QRect(60, 330, 351, 31))
        self.userLineEdit.setFont(font1)
        self.userLineEdit.setStyleSheet(u"padding:0 10px;")
        self.label_5 = QLabel(NewDBConfForm)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(510, 110, 141, 31))
        self.dbComboBox = QComboBox(NewDBConfForm)
        self.dbComboBox.setObjectName(u"dbComboBox")
        self.dbComboBox.setGeometry(QRect(510, 150, 191, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.dbComboBox.setFont(font2)
        self.dbComboBox.setStyleSheet(u"border:1px solid #000;")
        self.sendDBConfBtn = QPushButton(NewDBConfForm)
        self.sendDBConfBtn.setObjectName(u"sendDBConfBtn")
        self.sendDBConfBtn.setGeometry(QRect(510, 460, 161, 41))
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.sendDBConfBtn.setFont(font3)
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
        self.cancelNewDBBtn.setFont(font3)
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
        self.passLineEdit.setFont(font1)
        self.passLineEdit.setStyleSheet(u"padding:0 10px;")
        self.labelPass = QLabel(NewDBConfForm)
        self.labelPass.setObjectName(u"labelPass")
        self.labelPass.setGeometry(QRect(60, 380, 101, 31))
        self.testResultDBLabelError = QLabel(NewDBConfForm)
        self.testResultDBLabelError.setObjectName(u"testResultDBLabelError")
        self.testResultDBLabelError.setGeometry(QRect(510, 290, 321, 81))
        font4 = QFont()
        font4.setFamily(u"Verdana")
        font4.setBold(True)
        font4.setWeight(62)
        self.testResultDBLabelError.setFont(font4)
        self.testResultDBLabelError.setStyleSheet(u"#testResultDBLabelError{\n"
"color: rgb(199, 0, 0);\n"
"font-size:18px; \n"
"letter-spacing: 2px;\n"
"font-weight: 500;\n"
"}")
        self.testResultDBLabelError.setWordWrap(True)
        self.testDBConfBtn = QPushButton(NewDBConfForm)
        self.testDBConfBtn.setObjectName(u"testDBConfBtn")
        self.testDBConfBtn.setGeometry(QRect(510, 230, 321, 41))
        self.testDBConfBtn.setFont(font3)
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
        self.hostErrorLabel = QLabel(NewDBConfForm)
        self.hostErrorLabel.setObjectName(u"hostErrorLabel")
        self.hostErrorLabel.setGeometry(QRect(240, 130, 171, 20))
        self.hostErrorLabel.setLayoutDirection(Qt.RightToLeft)
        self.hostErrorLabel.setStyleSheet(u"color: rgb(199, 0, 0);\n"
"text-align: right;")
        self.hostErrorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dbErrorLabel = QLabel(NewDBConfForm)
        self.dbErrorLabel.setObjectName(u"dbErrorLabel")
        self.dbErrorLabel.setGeometry(QRect(240, 220, 171, 20))
        self.dbErrorLabel.setLayoutDirection(Qt.RightToLeft)
        self.dbErrorLabel.setStyleSheet(u"color: rgb(199, 0, 0);\n"
"text-align: right;")
        self.dbErrorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.userErrorLabel = QLabel(NewDBConfForm)
        self.userErrorLabel.setObjectName(u"userErrorLabel")
        self.userErrorLabel.setGeometry(QRect(240, 310, 171, 20))
        self.userErrorLabel.setLayoutDirection(Qt.RightToLeft)
        self.userErrorLabel.setStyleSheet(u"color: rgb(199, 0, 0);\n"
"text-align: right;")
        self.userErrorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.testResultDBLabel = QLabel(NewDBConfForm)
        self.testResultDBLabel.setObjectName(u"testResultDBLabel")
        self.testResultDBLabel.setGeometry(QRect(510, 410, 351, 31))
        font5 = QFont()
        font5.setFamily(u"Verdana")
        font5.setPointSize(11)
        self.testResultDBLabel.setFont(font5)
        self.testResultDBLabel.setStyleSheet(u"#testResultDBLabel{\n"
"	color: rgb(99, 199, 147);\n"
"}")
        self.testResultDBLabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(NewDBConfForm)

        QMetaObject.connectSlotsByName(NewDBConfForm)
    # setupUi

    def retranslateUi(self, NewDBConfForm):
        NewDBConfForm.setWindowTitle(QCoreApplication.translate("NewDBConfForm", u"new_socio_window", None))
        self.label.setText(QCoreApplication.translate("NewDBConfForm", u"CONFIGURACI\u00d3N DB", None))
        self.labelHost.setText(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Host: </span></p></body></html>", None))
        self.labelDB.setText(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Database: </span></p></body></html>", None))
        self.labelUser.setText(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">User: </span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Seleccionar DB: </span></p></body></html>", None))
        self.sendDBConfBtn.setText(QCoreApplication.translate("NewDBConfForm", u"Cambiar DB", None))
        self.cancelNewDBBtn.setText(QCoreApplication.translate("NewDBConfForm", u"Cancelar", None))
        self.labelPass.setText(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Password: </span></p></body></html>", None))
        self.testResultDBLabelError.setText("")
        self.testDBConfBtn.setText(QCoreApplication.translate("NewDBConfForm", u"Testear conexi\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.hostErrorLabel.setToolTip(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.hostErrorLabel.setText("")
#if QT_CONFIG(tooltip)
        self.dbErrorLabel.setToolTip(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dbErrorLabel.setText("")
#if QT_CONFIG(tooltip)
        self.userErrorLabel.setToolTip(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.userErrorLabel.setText("")
        self.testResultDBLabel.setText(QCoreApplication.translate("NewDBConfForm", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

