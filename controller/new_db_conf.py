from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget
from views.Ui_db_config import NewDBConfForm
import json
from db.db import Connection, CrudDB
import os
import sys


class NewDBConfWindow(QWidget, NewDBConfForm):
    new_settings = {}
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.populate_db_combobox(["SQLite", "MySQL"])
        self.cancelNewDBBtn.clicked.connect(self.close)
        self.testResultDBLabel.setText("")
        self.testDBConfBtn.clicked.connect(self.check_conn)
        self.sendDBConfBtn.clicked.connect(self.save_data)
        # captura el cambio del combobox
        self.dbComboBox.currentTextChanged.connect(self.hide_fields)
        self.hostLineEdit.hide()
        self.userLineEdit.hide()
        self.passLineEdit.hide()
        
        
    # TODO: falta escondaer los labels con las palabras
    def hide_fields(self):
        if self.dbComboBox.currentText() == "SQLite":
            self.hostLineEdit.hide()
            self.userLineEdit.hide()
            self.passLineEdit.hide()
        else:
            self.hostLineEdit.show()
            self.userLineEdit.show()
            self.passLineEdit.show()
        
        
    def check_input(self):
        type = self.dbComboBox.currentText()
        host = self.hostLineEdit.text()
        database = self.databaseLineEdit.text()
        user = self.userLineEdit.text()
        password = self.passLineEdit.text()
        errors_count = 0
        
        if database == "":
            errors_count += 1
        
        if errors_count == 0:
            self.new_settings = {
                "type"      : type,
                "name"      : database,
                "host"      : host,
                "user"      : user,
                "password"  : password
            }
            return True
        else:
            return False
         
         
    def clear_inputs(self):
        self.hostLineEdit.clear()
        self.databaseLineEdit.clear()
        self.userLineEdit.clear()
        self.passLineEdit.clear()
    
    
    def populate_db_combobox(self, list):
        self.dbComboBox.addItems(list)
        
    
    @staticmethod
    def change_settings(data):
        with open('db/settings.json', "w") as file:
            json.dump(data, file)
    
    
    @staticmethod
    def backup_socios(data):
        with open('db/socios.json', "w") as file:
            json.dump(data, file, default=str, indent=1)
         
        
    
    def check_conn(self):
        self.testResultDBLabel.setText(" ")
        if self.check_input():
            conn = Connection().connection(self.new_settings)
            if conn["status"]:
                self.testResultDBLabel.setText(conn["message"])
            else:
                self.testResultDBLabel.setText(conn["message"])
        else:
            self.testResultDBLabel.setText("Faltan datos")
        
    
    def save_data(self):
        """copia todo lo de la base de datos antigua a la nueva base de datos"""  
        socios = CrudDB()
        lista_socios = socios.get_all()
        if self.check_input():
            self.backup_socios(lista_socios)
            self.change_settings(self.new_settings)
            socios.drop_table()
            # os.execl(sys.executable, sys.executable, *sys.argv)
            os.execv(sys.executable, ['python'] + sys.argv)
        