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
        self.hide_labels()
        
        
    def hide_fields(self):
        self.erase_errors_labels()
        self.testResultDBLabel.setText('')
        if self.dbComboBox.currentText() == "SQLite":
            self.hide_labels()
        else:
            self.hostLineEdit.show()
            self.userLineEdit.show()
            self.passLineEdit.show()
            self.labelHost.show()
            self.labelUser.show()
            self.labelPass.show()
    
    
    def hide_labels(self):
        self.hostLineEdit.hide()
        self.userLineEdit.hide()
        self.passLineEdit.hide()
        self.labelHost.hide()
        self.labelUser.hide()
        self.labelPass.hide()
    
        
    def check_input(self):
        self.erase_errors_labels()
        db_type = self.dbComboBox.currentText()
        host = self.hostLineEdit.text()
        database = self.databaseLineEdit.text()
        user = self.userLineEdit.text()
        password = self.passLineEdit.text()
        errors_dict = {
            "count": 0,
        }
        # hostErrorLabel, dbErrorLabel, userErrorLabel
        if database == "":
            errors_dict["count"] += 1
            errors_dict["database"] = "Este campo es obligatorio"
        
        if db_type == "MySQL":
            if host == "":
                errors_dict["count"] += 1
                errors_dict["host"] = "Este campo es obligatorio"
                
            if user == "":
                errors_dict["count"] += 1
                errors_dict["user"] = "Este campo es obligatorio"

        
        if errors_dict["count"] == 0:
            self.new_settings = {
                "type"      : db_type,
                "name"      : database,
                "host"      : host,
                "user"      : user,
                "password"  : password
            }
            return True
        else:
            self.write_erros_labels(errors_dict)
            return False
         

    def write_erros_labels(self, data):
        if data.get('database'):
            self.dbErrorLabel.setText(data['database'])
        if data.get('host'):
            self.hostErrorLabel.setText(data['host'])
        if data.get('user'):
            self.userErrorLabel.setText(data['user'])
    
    
    def erase_errors_labels(self):
        self.dbErrorLabel.setText("")
        self.hostErrorLabel.setText("")
        self.userErrorLabel.setText("")
    
         
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
            conn = Connection()
            result = conn.connection(self.new_settings)
            if result["status"]:
                self.testResultDBLabel.setText(result["message"])
                self.testResultDBLabelError.setText(" ")
            else:
                self.testResultDBLabelError.setText(result["message"])
                self.testResultDBLabel.setText(" ")
        else:
            self.testResultDBLabelError.setText("Faltan datos")
            self.testResultDBLabel.setText(" ")
            
        if os.path.isfile(self.new_settings["name"]):
            os.remove(self.new_settings["name"])
        
    
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
        