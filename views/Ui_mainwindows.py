# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainWindows2(object):
    def setupUi(self, MainWindows2):
        if not MainWindows2.objectName():
            MainWindows2.setObjectName(u"MainWindows2")
        MainWindows2.resize(1411, 806)
        MainWindows2.setStyleSheet(u"background-color:#ffffff;")
        self.OptionsFrame = QFrame(MainWindows2)
        self.OptionsFrame.setObjectName(u"OptionsFrame")
        self.OptionsFrame.setGeometry(QRect(-1, 0, 241, 821))
        self.OptionsFrame.setStyleSheet(u"background-color:rgb(77, 62, 70);")
        self.OptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.OptionsFrame.setFrameShadow(QFrame.Raised)
        self.addSocioBtn = QPushButton(self.OptionsFrame)
        self.addSocioBtn.setObjectName(u"addSocioBtn")
        self.addSocioBtn.setGeometry(QRect(40, 330, 151, 41))
        self.addSocioBtn.setStyleSheet(u"#addSocioBtn{\n"
"color:#fff;\n"
"font-size: 14px;\n"
"font-weight: 600;\n"
"letter-spacing: 2px;\n"
"border:none;\n"
"background-color:rgb(61, 49, 55);\n"
"}")
        self.configDB = QPushButton(self.OptionsFrame)
        self.configDB.setObjectName(u"configDB")
        self.configDB.setGeometry(QRect(40, 430, 151, 41))
        self.configDB.setStyleSheet(u"color:rgb(227, 227, 227);\n"
"font-size: 14px;\n"
"font-weight: 600;\n"
"letter-spacing: 2px;\n"
"border:none;\n"
"background-color:rgb(61, 49, 55);")
        self.createChargeBtn = QPushButton(self.OptionsFrame)
        self.createChargeBtn.setObjectName(u"createChargeBtn")
        self.createChargeBtn.setGeometry(QRect(40, 380, 151, 41))
        self.createChargeBtn.setStyleSheet(u"color:rgb(227, 227, 227);\n"
"font-size: 14px;\n"
"font-weight: 600;\n"
"letter-spacing: 2px;\n"
"border:none;\n"
"background-color:rgb(61, 49, 55);")
        self.docuBtn = QPushButton(self.OptionsFrame)
        self.docuBtn.setObjectName(u"docuBtn")
        self.docuBtn.setGeometry(QRect(40, 730, 151, 41))
        self.docuBtn.setStyleSheet(u"color:rgb(227, 227, 227);\n"
"font-size: 14px;\n"
"font-weight: 600;\n"
"letter-spacing: 2px;\n"
"border:none;\n"
"background-color:rgb(61, 49, 55);")
        self.MembersFrame = QFrame(MainWindows2)
        self.MembersFrame.setObjectName(u"MembersFrame")
        self.MembersFrame.setGeometry(QRect(1000, 0, 421, 821))
        self.MembersFrame.setStyleSheet(u"background-color:rgba(247, 247, 247, 245);")
        self.MembersFrame.setFrameShape(QFrame.StyledPanel)
        self.MembersFrame.setFrameShadow(QFrame.Raised)
        self.selectSocioLabel = QLabel(self.MembersFrame)
        self.selectSocioLabel.setObjectName(u"selectSocioLabel")
        self.selectSocioLabel.setGeometry(QRect(24, 309, 371, 161))
        font = QFont()
        font.setFamily(u"Verdana")
        font.setBold(True)
        font.setWeight(62)
        self.selectSocioLabel.setFont(font)
        self.selectSocioLabel.setStyleSheet(u"font-size:20px; \n"
"color:#3c2934;\n"
"letter-spacing: 2px;\n"
"font-weight: 500;")
        self.selectSocioLabel.setAlignment(Qt.AlignCenter)
        self.selectSocioLabel.setWordWrap(True)
        self.SocioInfoFrame = QFrame(self.MembersFrame)
        self.SocioInfoFrame.setObjectName(u"SocioInfoFrame")
        self.SocioInfoFrame.setEnabled(True)
        self.SocioInfoFrame.setGeometry(QRect(0, 0, 421, 811))
        self.SocioInfoFrame.setStyleSheet(u"background-color: rgb(253, 253, 253);\n"
"")
        self.SocioInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.SocioInfoFrame.setFrameShadow(QFrame.Raised)
        self.socioMainNameLabel = QLabel(self.SocioInfoFrame)
        self.socioMainNameLabel.setObjectName(u"socioMainNameLabel")
        self.socioMainNameLabel.setEnabled(False)
        self.socioMainNameLabel.setGeometry(QRect(20, 30, 391, 61))
        self.socioMainNameLabel.setStyleSheet(u"font-size:25px; \n"
"color:#3c2934;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"font-weight: 600;\n"
"")
        self.label = QLabel(self.SocioInfoFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 200, 271, 31))
        self.SocioStateLabel = QLabel(self.SocioInfoFrame)
        self.SocioStateLabel.setObjectName(u"SocioStateLabel")
        self.SocioStateLabel.setGeometry(QRect(40, 240, 351, 31))
        self.SocioStateLabel.setStyleSheet(u"background-color: #F5F5F5;\n"
"border-radius: 5px;\n"
"color: #392D33;\n"
"padding: 5px 10px;\n"
"font-size: 14px;\n"
"letter-spacing:5px;")
        self.label_2 = QLabel(self.SocioInfoFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 310, 251, 31))
        self.SocioDateLabel = QLabel(self.SocioInfoFrame)
        self.SocioDateLabel.setObjectName(u"SocioDateLabel")
        self.SocioDateLabel.setGeometry(QRect(40, 350, 351, 31))
        self.SocioDateLabel.setStyleSheet(u"background-color: #F5F5F5;\n"
"border-radius: 5px;\n"
"color: #392D33;\n"
"padding: 5px 10px;\n"
"font-size: 14px;\n"
"letter-spacing:5px;")
        self.label_3 = QLabel(self.SocioInfoFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 420, 181, 31))
        self.SocioPlanInfoLabel = QLabel(self.SocioInfoFrame)
        self.SocioPlanInfoLabel.setObjectName(u"SocioPlanInfoLabel")
        self.SocioPlanInfoLabel.setGeometry(QRect(40, 460, 351, 81))
        self.SocioPlanInfoLabel.setStyleSheet(u"background-color: #F5F5F5;\n"
"border-radius: 5px;\n"
"color: #392D33;\n"
"padding: 5px 10px;\n"
"font-size: 14px;\n"
"letter-spacing:5px;")
        self.SocioPlanInfoLabel.setWordWrap(True)
        self.SocioPlanLabel = QLabel(self.SocioInfoFrame)
        self.SocioPlanLabel.setObjectName(u"SocioPlanLabel")
        self.SocioPlanLabel.setGeometry(QRect(210, 420, 121, 31))
        self.label_4 = QLabel(self.SocioInfoFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 560, 131, 31))
        self.SocioDiscountLabel = QLabel(self.SocioInfoFrame)
        self.SocioDiscountLabel.setObjectName(u"SocioDiscountLabel")
        self.SocioDiscountLabel.setGeometry(QRect(40, 600, 351, 31))
        self.SocioDiscountLabel.setStyleSheet(u"background-color: #F5F5F5;\n"
"border-radius: 5px;\n"
"color: #392D33;\n"
"padding: 5px 10px;\n"
"font-size: 14px;\n"
"letter-spacing:5px;")
        self.SocioDiscountLabel.setWordWrap(True)
        self.SocioDiscountInfoLabel = QLabel(self.SocioInfoFrame)
        self.SocioDiscountInfoLabel.setObjectName(u"SocioDiscountInfoLabel")
        self.SocioDiscountInfoLabel.setGeometry(QRect(160, 560, 121, 31))
        self.SocioEmailLabel = QLabel(self.SocioInfoFrame)
        self.SocioEmailLabel.setObjectName(u"SocioEmailLabel")
        self.SocioEmailLabel.setGeometry(QRect(20, 90, 411, 31))
        self.SocioEmailLabel.setStyleSheet(u"color:#3c2934;\n"
"letter-spacing: 2px;\n"
"text-align: center;")
        self.updateSocioBtn = QPushButton(self.SocioInfoFrame)
        self.updateSocioBtn.setObjectName(u"updateSocioBtn")
        self.updateSocioBtn.setGeometry(QRect(40, 660, 161, 51))
        self.updateSocioBtn.setStyleSheet(u"#updateSocioBtn{\n"
"background-color: #F5F5F5;\n"
"border-radius: 5px;\n"
"color: #392D33;\n"
"padding: 5px;\n"
"font-size: 12px;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"font-weight: 600;\n"
"}\n"
"\n"
"#updateSocioBtn:hover{\n"
"	color: rgb(0, 85, 255);\n"
"	border:1px solid rgb(225, 225, 225);\n"
"}")
        self.banSocioBtn = QPushButton(self.SocioInfoFrame)
        self.banSocioBtn.setObjectName(u"banSocioBtn")
        self.banSocioBtn.setGeometry(QRect(240, 660, 151, 51))
        self.banSocioBtn.setStyleSheet(u"#banSocioBtn{\n"
"background-color: #F5F5F5;\n"
"border-radius: 5px;\n"
"color: #392D33;\n"
"padding: 5px;\n"
"font-size: 12px;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"font-weight: 600;\n"
"}\n"
"\n"
"#banSocioBtn:hover{\n"
"	color: rgb(255, 0, 0);\n"
"	border:1px solid rgb(225, 225, 225);\n"
"}")
        self.deleteSocioBtn = QPushButton(self.SocioInfoFrame)
        self.deleteSocioBtn.setObjectName(u"deleteSocioBtn")
        self.deleteSocioBtn.setGeometry(QRect(240, 720, 151, 51))
        self.deleteSocioBtn.setStyleSheet(u"#deleteSocioBtn{\n"
"background-color: #F5F5F5;\n"
"border-radius: 5px;\n"
"color: #392D33;\n"
"padding: 5px;\n"
"font-size: 12px;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"font-weight: 600;\n"
"}\n"
"\n"
"#deleteSocioBtn:hover{\n"
"	color: rgb(255, 0, 0);\n"
"border:1px solid rgb(225, 225, 225);\n"
"}")
        self.activateSocioBtn = QPushButton(self.SocioInfoFrame)
        self.activateSocioBtn.setObjectName(u"activateSocioBtn")
        self.activateSocioBtn.setGeometry(QRect(40, 720, 161, 51))
        self.activateSocioBtn.setStyleSheet(u"#activateSocioBtn{\n"
"background-color: #F5F5F5;\n"
"border-radius: 5px;\n"
"color: #392D33;\n"
"padding: 5px;\n"
"font-size: 12px;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"font-weight: 600;\n"
"}\n"
"\n"
"#activateSocioBtn:hover{\n"
"	color: rgb(0, 85, 255);\n"
"	border:1px solid rgb(225, 225, 225);\n"
"}")
        self.ListFrame = QFrame(MainWindows2)
        self.ListFrame.setObjectName(u"ListFrame")
        self.ListFrame.setGeometry(QRect(240, 0, 761, 821))
        self.ListFrame.setStyleSheet(u"background-color:#ffffff;")
        self.ListFrame.setFrameShape(QFrame.StyledPanel)
        self.ListFrame.setFrameShadow(QFrame.Raised)
        self.sociosListTable = QTableWidget(self.ListFrame)
        self.sociosListTable.setObjectName(u"sociosListTable")
        self.sociosListTable.setEnabled(True)
        self.sociosListTable.setGeometry(QRect(0, 210, 761, 481))
        self.sociosListTable.setStyleSheet(u"#sociosListTable{\n"
"	border:none;\n"
"	margin:10px;\n"
"}\n"
"\n"
"#sociosListTable thead tr {\n"
"    background-color: #009879;\n"
"    color: #ffffff;\n"
"    text-align: left;\n"
"}\n"
"\n"
"#sociosListTable th,\n"
"#sociosListTable td {\n"
"    padding: 12px 15px;\n"
"}\n"
"")
        self.sociosListTable.setTextElideMode(Qt.ElideMiddle)
        self.sociosListTable.setColumnCount(0)
        self.sociosListTable.verticalHeader().setVisible(False)
        self.sociosCountLabel = QLabel(self.ListFrame)
        self.sociosCountLabel.setObjectName(u"sociosCountLabel")
        self.sociosCountLabel.setGeometry(QRect(190, 700, 91, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.sociosCountLabel.setFont(font1)
        self.countSocioLabel = QLabel(self.ListFrame)
        self.countSocioLabel.setObjectName(u"countSocioLabel")
        self.countSocioLabel.setGeometry(QRect(10, 690, 171, 41))
        self.label_15 = QLabel(self.ListFrame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(90, 70, 651, 101))
        font2 = QFont()
        font2.setFamily(u"Sitka Small")
        font2.setBold(True)
        font2.setWeight(87)
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"font-size:70px; \n"
"color:rgb(227, 227, 227);\n"
"letter-spacing: 0px;\n"
"font-weight: 700;")
        self.label_15.setFrameShape(QFrame.NoFrame)
        self.newSocioFrame = QFrame(MainWindows2)
        self.newSocioFrame.setObjectName(u"newSocioFrame")
        self.newSocioFrame.setGeometry(QRect(240, 0, 761, 801))
        self.newSocioFrame.setFrameShape(QFrame.StyledPanel)
        self.newSocioFrame.setFrameShadow(QFrame.Raised)
        self.planComboBox = QComboBox(self.newSocioFrame)
        self.planComboBox.setObjectName(u"planComboBox")
        self.planComboBox.setGeometry(QRect(500, 240, 191, 31))
        font3 = QFont()
        self.planComboBox.setFont(font3)
        self.planComboBox.setStyleSheet(u"border:1px solid #3c2934; \n"
"color:#3c2934;\n"
"letter-spacing: 2px;\n"
"font-size: 14px\n"
"")
        self.label_5 = QLabel(self.newSocioFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 70, 651, 101))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"font-size:70px; \n"
"color:rgb(227, 227, 227);\n"
"letter-spacing: 0px;\n"
"font-weight: 700;")
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_6 = QLabel(self.newSocioFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(500, 210, 141, 21))
        self.cancelNewSocioBtn = QPushButton(self.newSocioFrame)
        self.cancelNewSocioBtn.setObjectName(u"cancelNewSocioBtn")
        self.cancelNewSocioBtn.setGeometry(QRect(540, 710, 171, 41))
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.cancelNewSocioBtn.setFont(font4)
        self.cancelNewSocioBtn.setStyleSheet(u"#cancelNewSocioBtn{\n"
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
"#cancelNewSocioBtn:hover{\n"
"	color: rgb(255, 0, 0);\n"
"	border:1px solid rgb(225, 225, 225);\n"
"}")
        self.label_7 = QLabel(self.newSocioFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 200, 101, 31))
        self.label_8 = QLabel(self.newSocioFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(90, 380, 71, 31))
        self.newSocioErrorLabel = QLabel(self.newSocioFrame)
        self.newSocioErrorLabel.setObjectName(u"newSocioErrorLabel")
        self.newSocioErrorLabel.setGeometry(QRect(90, 515, 661, 31))
        font5 = QFont()
        font5.setFamily(u"Verdana")
        font5.setPointSize(10)
        self.newSocioErrorLabel.setFont(font5)
        self.newSocioErrorLabel.setLayoutDirection(Qt.LeftToRight)
        self.newSocioErrorLabel.setStyleSheet(u"#newSocioErrorLabel{color: rgb(199, 0, 0);}")
        self.lnameLineEdit = QLineEdit(self.newSocioFrame)
        self.lnameLineEdit.setObjectName(u"lnameLineEdit")
        self.lnameLineEdit.setGeometry(QRect(90, 330, 351, 31))
        self.lnameLineEdit.setFont(font1)
        self.lnameLineEdit.setStyleSheet(u"padding:0 10px;")
        self.sendNewSocioBtn = QPushButton(self.newSocioFrame)
        self.sendNewSocioBtn.setObjectName(u"sendNewSocioBtn")
        self.sendNewSocioBtn.setGeometry(QRect(350, 710, 171, 41))
        self.sendNewSocioBtn.setFont(font4)
        self.sendNewSocioBtn.setStyleSheet(u"#sendNewSocioBtn{\n"
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
"#sendNewSocioBtn:hover{\n"
"	color: rgb(17, 17, 17);\n"
"	border:1px solid rgb(225, 225, 225);\n"
"}")
        self.label_9 = QLabel(self.newSocioFrame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(90, 290, 101, 31))
        self.emailLineEdit = QLineEdit(self.newSocioFrame)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setGeometry(QRect(90, 420, 351, 31))
        self.emailLineEdit.setFont(font1)
        self.emailLineEdit.setStyleSheet(u"padding:0 10px;")
        self.discountComboBox = QComboBox(self.newSocioFrame)
        self.discountComboBox.setObjectName(u"discountComboBox")
        self.discountComboBox.setGeometry(QRect(500, 330, 191, 31))
        self.discountComboBox.setFont(font3)
        self.discountComboBox.setStyleSheet(u"border:1px solid #3c2934; \n"
"color:#3c2934;\n"
"letter-spacing: 2px;\n"
"font-size: 14px")
        self.label_10 = QLabel(self.newSocioFrame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(500, 300, 141, 21))
        self.nameLineEdit = QLineEdit(self.newSocioFrame)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setGeometry(QRect(90, 240, 351, 31))
        self.nameLineEdit.setFont(font1)
        self.nameLineEdit.setStyleSheet(u"padding:0 10px;")
        self.newSocioSuccessLabel = QLabel(self.newSocioFrame)
        self.newSocioSuccessLabel.setObjectName(u"newSocioSuccessLabel")
        self.newSocioSuccessLabel.setGeometry(QRect(360, 570, 351, 31))
        font6 = QFont()
        font6.setFamily(u"Verdana")
        font6.setPointSize(11)
        self.newSocioSuccessLabel.setFont(font6)
        self.newSocioSuccessLabel.setStyleSheet(u"#newSocioSuccessLabel{\n"
"	color: rgb(99, 199, 147);\n"
"}")
        self.nameErrorLabel = QLabel(self.newSocioFrame)
        self.nameErrorLabel.setObjectName(u"nameErrorLabel")
        self.nameErrorLabel.setGeometry(QRect(270, 220, 171, 20))
        self.nameErrorLabel.setLayoutDirection(Qt.RightToLeft)
        self.nameErrorLabel.setStyleSheet(u"color: rgb(199, 0, 0);\n"
"text-align: right;")
        self.nameErrorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lnameErrorLabel = QLabel(self.newSocioFrame)
        self.lnameErrorLabel.setObjectName(u"lnameErrorLabel")
        self.lnameErrorLabel.setGeometry(QRect(270, 310, 171, 20))
        self.lnameErrorLabel.setLayoutDirection(Qt.RightToLeft)
        self.lnameErrorLabel.setStyleSheet(u"color: rgb(199, 0, 0);\n"
"text-align: right;")
        self.lnameErrorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.emailErrorLabel = QLabel(self.newSocioFrame)
        self.emailErrorLabel.setObjectName(u"emailErrorLabel")
        self.emailErrorLabel.setGeometry(QRect(270, 400, 171, 20))
        self.emailErrorLabel.setLayoutDirection(Qt.RightToLeft)
        self.emailErrorLabel.setStyleSheet(u"color: rgb(199, 0, 0);\n"
"text-align: right;")
        self.emailErrorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.updateSocioFrame = QFrame(MainWindows2)
        self.updateSocioFrame.setObjectName(u"updateSocioFrame")
        self.updateSocioFrame.setGeometry(QRect(240, 0, 761, 811))
        self.updateSocioFrame.setStyleSheet(u"")
        self.updateSocioFrame.setFrameShape(QFrame.StyledPanel)
        self.updateSocioFrame.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.updateSocioFrame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(90, 200, 101, 31))
        self.cancelUpdateSocioBtn = QPushButton(self.updateSocioFrame)
        self.cancelUpdateSocioBtn.setObjectName(u"cancelUpdateSocioBtn")
        self.cancelUpdateSocioBtn.setGeometry(QRect(540, 710, 171, 41))
        self.cancelUpdateSocioBtn.setFont(font4)
        self.cancelUpdateSocioBtn.setStyleSheet(u"#cancelUpdateSocioBtn{\n"
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
"#cancelUpdateSocioBtn:hover{\n"
"	color: rgb(255, 0, 0);\n"
"	border:1px solid rgb(225, 225, 225);\n"
"}")
        self.sendUpdateSocioBtn = QPushButton(self.updateSocioFrame)
        self.sendUpdateSocioBtn.setObjectName(u"sendUpdateSocioBtn")
        self.sendUpdateSocioBtn.setGeometry(QRect(350, 710, 171, 41))
        self.sendUpdateSocioBtn.setFont(font4)
        self.sendUpdateSocioBtn.setStyleSheet(u"#sendUpdateSocioBtn{\n"
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
"#sendUpdateSocioBtn:hover{\n"
"	color: rgb(17, 17, 17);\n"
"	border:1px solid rgb(225, 225, 225);\n"
"}")
        self.label_12 = QLabel(self.updateSocioFrame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(90, 400, 141, 31))
        self.planUpdateComboBox = QComboBox(self.updateSocioFrame)
        self.planUpdateComboBox.setObjectName(u"planUpdateComboBox")
        self.planUpdateComboBox.setGeometry(QRect(90, 430, 191, 31))
        self.planUpdateComboBox.setFont(font3)
        self.planUpdateComboBox.setStyleSheet(u"border:1px solid #3c2934; \n"
"color:#3c2934;\n"
"letter-spacing: 2px;\n"
"font-size: 14px")
        self.label_13 = QLabel(self.updateSocioFrame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(90, 70, 651, 101))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"font-size:70px; \n"
"color:rgb(227, 227, 227);\n"
"letter-spacing: 0px;\n"
"font-weight: 700;\n"
"")
        self.label_13.setFrameShape(QFrame.NoFrame)
        self.nameUpdateLineEdit = QLineEdit(self.updateSocioFrame)
        self.nameUpdateLineEdit.setObjectName(u"nameUpdateLineEdit")
        self.nameUpdateLineEdit.setGeometry(QRect(90, 230, 351, 31))
        self.nameUpdateLineEdit.setFont(font1)
        self.nameUpdateLineEdit.setStyleSheet(u"padding:0 10px;")
        self.label_14 = QLabel(self.updateSocioFrame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(90, 300, 101, 31))
        self.lnameUpdateLineEdit = QLineEdit(self.updateSocioFrame)
        self.lnameUpdateLineEdit.setObjectName(u"lnameUpdateLineEdit")
        self.lnameUpdateLineEdit.setGeometry(QRect(90, 330, 351, 31))
        self.lnameUpdateLineEdit.setFont(font1)
        self.lnameUpdateLineEdit.setStyleSheet(u"padding:0 10px;")
        self.lnameErrorLabel_2 = QLabel(self.updateSocioFrame)
        self.lnameErrorLabel_2.setObjectName(u"lnameErrorLabel_2")
        self.lnameErrorLabel_2.setGeometry(QRect(270, 310, 171, 20))
        self.lnameErrorLabel_2.setLayoutDirection(Qt.RightToLeft)
        self.lnameErrorLabel_2.setStyleSheet(u"color: rgb(199, 0, 0);\n"
"text-align: right;")
        self.lnameErrorLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.nameErrorLabel_2 = QLabel(self.updateSocioFrame)
        self.nameErrorLabel_2.setObjectName(u"nameErrorLabel_2")
        self.nameErrorLabel_2.setGeometry(QRect(270, 210, 171, 20))
        self.nameErrorLabel_2.setLayoutDirection(Qt.RightToLeft)
        self.nameErrorLabel_2.setStyleSheet(u"color: rgb(199, 0, 0);\n"
"text-align: right;")
        self.nameErrorLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.MembersFrame.raise_()
        self.OptionsFrame.raise_()
        self.ListFrame.raise_()
        self.newSocioFrame.raise_()
        self.updateSocioFrame.raise_()
        QWidget.setTabOrder(self.createChargeBtn, self.sociosListTable)
        QWidget.setTabOrder(self.sociosListTable, self.addSocioBtn)
        QWidget.setTabOrder(self.addSocioBtn, self.nameLineEdit)
        QWidget.setTabOrder(self.nameLineEdit, self.lnameLineEdit)
        QWidget.setTabOrder(self.lnameLineEdit, self.emailLineEdit)
        QWidget.setTabOrder(self.emailLineEdit, self.planComboBox)
        QWidget.setTabOrder(self.planComboBox, self.discountComboBox)
        QWidget.setTabOrder(self.discountComboBox, self.sendNewSocioBtn)
        QWidget.setTabOrder(self.sendNewSocioBtn, self.cancelNewSocioBtn)
        QWidget.setTabOrder(self.cancelNewSocioBtn, self.updateSocioBtn)
        QWidget.setTabOrder(self.updateSocioBtn, self.banSocioBtn)
        QWidget.setTabOrder(self.banSocioBtn, self.deleteSocioBtn)
        QWidget.setTabOrder(self.deleteSocioBtn, self.configDB)

        self.retranslateUi(MainWindows2)

        QMetaObject.connectSlotsByName(MainWindows2)
    # setupUi

    def retranslateUi(self, MainWindows2):
        MainWindows2.setWindowTitle(QCoreApplication.translate("MainWindows2", u"Form", None))
        self.addSocioBtn.setText(QCoreApplication.translate("MainWindows2", u"Nuevo Socio", None))
        self.configDB.setText(QCoreApplication.translate("MainWindows2", u"Configurar DB", None))
        self.createChargeBtn.setText(QCoreApplication.translate("MainWindows2", u"Crear Cobro", None))
        self.docuBtn.setText(QCoreApplication.translate("MainWindows2", u"Documentaci\u00f3n", None))
        self.selectSocioLabel.setText(QCoreApplication.translate("MainWindows2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Verdana'; font-size:20px; font-weight:496; font-style:normal; letter-spacing:2px;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:400;\"><br /></p></body></html>", None))
        self.socioMainNameLabel.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Estado del Socio</span></p></body></html>", None))
        self.SocioStateLabel.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Fecha de ingreso</span></p></body></html>", None))
        self.SocioDateLabel.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Informacion Plan</span></p></body></html>", None))
        self.SocioPlanInfoLabel.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><br/></p></body></html>", None))
        self.SocioPlanLabel.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Descuentos</span></p></body></html>", None))
        self.SocioDiscountLabel.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><br/></p></body></html>", None))
        self.SocioDiscountInfoLabel.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><br/></p></body></html>", None))
        self.SocioEmailLabel.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.updateSocioBtn.setText(QCoreApplication.translate("MainWindows2", u"Actualizar Socio", None))
        self.banSocioBtn.setText(QCoreApplication.translate("MainWindows2", u"Desactivar Socio", None))
        self.deleteSocioBtn.setText(QCoreApplication.translate("MainWindows2", u"Eliminar Socio", None))
        self.activateSocioBtn.setText(QCoreApplication.translate("MainWindows2", u"Activar Socio", None))
        self.sociosCountLabel.setText(QCoreApplication.translate("MainWindows2", u"#", None))
        self.countSocioLabel.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cantidad de socios: </span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindows2", u"SOCIOS", None))
        self.label_5.setText(QCoreApplication.translate("MainWindows2", u"+ SOCIO", None))
        self.label_6.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Plan del socio: </span></p></body></html>", None))
        self.cancelNewSocioBtn.setText(QCoreApplication.translate("MainWindows2", u"Cancelar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Nombre: </span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Email: </span></p></body></html>", None))
        self.newSocioErrorLabel.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><br/></p></body></html>", None))
        self.sendNewSocioBtn.setText(QCoreApplication.translate("MainWindows2", u"Guardar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Apellido: </span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Descuentos: </span></p></body></html>", None))
        self.newSocioSuccessLabel.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.nameErrorLabel.setToolTip(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nameErrorLabel.setText("")
#if QT_CONFIG(tooltip)
        self.lnameErrorLabel.setToolTip(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lnameErrorLabel.setText("")
#if QT_CONFIG(tooltip)
        self.emailErrorLabel.setToolTip(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.emailErrorLabel.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Nombre: </span></p></body></html>", None))
        self.cancelUpdateSocioBtn.setText(QCoreApplication.translate("MainWindows2", u"Cancelar", None))
        self.sendUpdateSocioBtn.setText(QCoreApplication.translate("MainWindows2", u"Actualizar", None))
        self.label_12.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Plan del socio: </span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindows2", u"ACTUALIZAR", None))
        self.label_14.setText(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Apellido: </span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lnameErrorLabel_2.setToolTip(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lnameErrorLabel_2.setText("")
#if QT_CONFIG(tooltip)
        self.nameErrorLabel_2.setToolTip(QCoreApplication.translate("MainWindows2", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nameErrorLabel_2.setText("")
    # retranslateUi

