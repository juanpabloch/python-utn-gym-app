from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from views.Ui_mainwindows import MainWindows2
import re  

from .lista_cobros_windows import ListaCobroWindow
from .new_db_conf import NewDBConfWindow

from db.db import CrudDB, PlanesCrud, DiscountCrud
import webbrowser

import os
from pathlib import Path

this_directory = os.path.dirname(Path(__file__).parent)

class SocioWindow(QWidget, MainWindows2):
    socio_db = CrudDB()
    plan_db = PlanesCrud()
    discount_db = DiscountCrud()
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.selectSocioLabel.setText("Seleccionar un Socio de la lista")
        self.addSocioBtn.clicked.connect(self.open_new_socio)
        self.updateSocioBtn.clicked.connect(self.open_update_socio)
        self.deleteSocioBtn.clicked.connect(self.delete_socio)
        # self.updateSociosList.clicked.connect(self.populate_table)
        self.banSocioBtn.clicked.connect(self.deactivate_socio)
        self.activateSocioBtn.clicked.connect(self.activate_socio)
        self.createChargeBtn.clicked.connect(self.open_lista_cobros)
        self.configDB.clicked.connect(self.open_db_conf)
        self.table_config()
        self.populate_table()
        self.SocioInfoFrame.hide()
        self.populate_select_plan()
        # new socio
        self.newSocioFrame.hide()
        self.sociosListTable.itemClicked.connect(self.show_member)
        self.cancelNewSocioBtn.clicked.connect(self.close_new_socio)
        self.populate_select_discount()
        self.sendNewSocioBtn.clicked.connect(self.add_socio)
        # update
        self.updateSocioFrame.hide()
        self.cancelUpdateSocioBtn.clicked.connect(self.close_update)
        self.sendUpdateSocioBtn.clicked.connect(self.update_socio)
        # documentacion
        self.docuBtn.clicked.connect(self.open_doc)
        
    
    def open_doc(self):
        webbrowser.open_new_tab('file:///'+ this_directory + '/docs/_build/html/index.html')
    
        
    def open_lista_cobros(self):
        window = ListaCobroWindow(self)
        window.show()
        self.sociosListTable.clearSelection()
        self.SocioInfoFrame.hide() 
    
    
    def open_db_conf(self):
        window = NewDBConfWindow(self)
        window.show()
        self.sociosListTable.clearSelection()
        self.SocioInfoFrame.hide() 
    
    
    def table_config(self):
        column_headers = ["ID", "NOMBRE", "APELLIDO", "EMAIL"]    
        self.sociosListTable.setColumnCount(len(column_headers))
        self.sociosListTable.setColumnWidth(0, 70)
        self.sociosListTable.setColumnWidth(1, 170)
        self.sociosListTable.setColumnWidth(2, 170)
        self.sociosListTable.setColumnWidth(3, 220)
        self.sociosListTable.setHorizontalHeaderLabels(column_headers)
        self.sociosListTable.setSelectionBehavior(QAbstractItemView.SelectRows)
    
    
    def populate_table(self):
        """ popula la tabla con los datos de los socios """
        data = self.socio_db.get_all()
        self.sociosListTable.setRowCount(len(data))
        self.sociosCountLabel.setText(f'# {len(data)}')
        for (index_row, row) in enumerate(data):
            for (index_cell, (cell_type, cell)) in enumerate(row.items()):
                self.sociosListTable.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    
    def delete_socio(self):
        """elimina un socio"""
        selected_row = self.sociosListTable.selectedItems()
        if selected_row:
            result = self.socio_db.delete(selected_row[3].text())
            if result:
                print(f"Socio {selected_row[3].text()} eliminado correctamente")
    
        self.sociosListTable.clearSelection()    
        self.SocioInfoFrame.hide()
        self.populate_table()


    def deactivate_socio(self):
        """desactiva un socio"""
        selected_row = self.sociosListTable.selectedItems()
        if selected_row:
            result = self.socio_db.ban_socio(selected_row[3].text())
            if result:
                print(f"Socio {selected_row[3].text()} inhabilitado")        
        self.sociosListTable.clearSelection()   
        self.SocioInfoFrame.hide()
        self.populate_table()
        
    
    def activate_socio(self):
        """activa un socio"""
        selected_row = self.sociosListTable.selectedItems()
        if selected_row:
            result = self.socio_db.activate_socio(selected_row[3].text())
            if result:
                print(f"Socio {selected_row[3].text()} abilitado")        
        self.sociosListTable.clearSelection()   
        self.SocioInfoFrame.hide()
        self.populate_table()
        
        
    def show_member(self):
        """nos muestra los datos del socio seleccionado"""
        selected_row = self.sociosListTable.selectedItems()
        socio = self.socio_db.get_one(selected_row[3].text())
        plan = self.plan_db.get_one(socio.plan_id)
        discount = self.discount_db.get_one(socio.discount_id)
        self.SocioInfoFrame.show()
        self.socio_data_show(socio, plan, discount)
        
        

    def socio_data_show(self, socio, plan, discount):
        """recopila la informacion del socio"""
        state = "Activo" if socio.active == 1 else "No activo"
        email = socio.email
        full_name = f"{socio.name} {socio.lname}"
        date = socio.created_at.strftime('%Y/%m/%d').split(' ')[0]
        plan_info = plan.data
        plan_name = plan.plan_name.capitalize()
        discount_applications = f'Quedan: {socio.applications_left} aplicaciones' if discount else 'No tiene descuentos'
        discount_percentage = f'{discount.percentage}%' if discount else ''
        
        self.socioMainNameLabel.setText(full_name)
        self.SocioEmailLabel.setText(email)
        self.SocioStateLabel.setText(state)
        if socio.active == 0:
            self.activateSocioBtn.show()
            self.banSocioBtn.hide()
            self.SocioStateLabel.setStyleSheet(
                u"background-color: #F5F5F5;\n"
                "border-radius: 5px;\n"
                "color: rgb(199, 0, 0);\n"
                "padding: 5px 10px;\n"
                "font-size: 14px;\n"
                "letter-spacing:5px;"
            )
        else:
            self.activateSocioBtn.hide()
            self.banSocioBtn.show()
            self.SocioStateLabel.setStyleSheet(
                u"background-color: #F5F5F5;\n"
                "border-radius: 5px;\n"
                "color: #392D33;\n"
                "padding: 5px 10px;\n"
                "font-size: 14px;\n"
                "letter-spacing:5px;"
            )
        self.SocioDateLabel.setText(date)
        self.SocioPlanInfoLabel.setText(plan_info)
        self.SocioPlanLabel.setText(f'({plan_name})')
        self.SocioDiscountLabel.setText(discount_applications)
        self.SocioDiscountInfoLabel.setText(discount_percentage)
        
        
    # New Socio
    def open_new_socio(self):
        self.newSocioFrame.show()
        self.sociosListTable.clearSelection()
        self.ListFrame.hide()
        self.SocioInfoFrame.hide()
        self.selectSocioLabel.setText("Agregar un nuevo Socio")
    
    
    def close_new_socio(self):
        self.newSocioFrame.hide()
        self.newSocioErrorLabel.setText("")
        self.newSocioSuccessLabel.setText("")
        self.selectSocioLabel.setText("Seleccionar un Socio de la lista")
        self.ListFrame.show()
        
        
    def check_input(self, input_type):
        """realiza las validaciones de los campos"""
        self.newSocioErrorLabel.setText("")
        self.erase_errors_labels()
        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        letters_regex = '^[a-zA-Z ]+$'
        
        name = self.nameLineEdit.text() if input_type == 'newSocio' else self.nameUpdateLineEdit.text()
        lname = self.lnameLineEdit.text() if input_type == 'newSocio' else self.lnameUpdateLineEdit.text()
        email = self.emailLineEdit.text()
        
        errors_dict = {
            "count": 0,
        }
        
        if name == "":
            errors_dict["name"] = "Este campo es obligatorio"
            errors_dict["count"] += 1
        elif not re.search(letters_regex, name):
            errors_dict["name"] = "Solo letras"
            errors_dict["count"] += 1
        
        if lname == "":
            errors_dict["lname"] = "Este campo es obligatorio"
            errors_dict["count"] += 1
        elif not re.search(letters_regex, lname):
            errors_dict["lname"] = "Solo letras"
            errors_dict["count"] += 1       
        
        if input_type == 'newSocio' and email == "":
            errors_dict["email"] = "Este campo es obligatorio"
            errors_dict["count"] += 1
        elif input_type == 'newSocio' and not re.search(email_regex, email):
            errors_dict["email"] = "Email invalido"
            errors_dict["count"] += 1
        
        if errors_dict["count"] == 0:
            return True
        else:
            self.newSocioErrorLabel.setText("Error al cargar los datos")
            self.write_erros_labels(errors_dict)
            return False

    
    def write_erros_labels(self, data):
        if data.get('name'):
            self.nameErrorLabel.setText(data['name'])
            self.nameErrorLabel_2.setText(data['name'])
        if data.get('lname'):
            self.lnameErrorLabel.setText(data['lname'])
            self.lnameErrorLabel_2.setText(data['lname'])
        if data.get('email'):
            self.emailErrorLabel.setText(data['email'])
    
    
    def erase_errors_labels(self):
        self.nameErrorLabel.setText("")
        self.nameErrorLabel_2.setText("")
        self.lnameErrorLabel.setText("")
        self.lnameErrorLabel_2.setText("")
        self.emailErrorLabel.setText("")
    

    def add_socio(self):
        """agregar un socio"""
        self.newSocioErrorLabel.setText("")
        self.newSocioSuccessLabel.setText("")
        if self.check_input('newSocio'):
            discount = self.discountComboBox.currentText()
            socio = {
                "name": self.nameLineEdit.text().strip(),
                "lname": self.lnameLineEdit.text().strip(), 
                "email": self.emailLineEdit.text().strip(), 
                "plan": self.planComboBox.currentText(), 
                "descuento": discount.split("%")[0] if discount != "Sin descuento" else None
            }
            result = self.socio_db.create(socio)
            if result["status"]:
                self.clear_inputs()
                self.newSocioSuccessLabel.setText(result["message"])
                self.populate_table()
            else:
                self.newSocioErrorLabel.setText(result["message"])
                
            
            
    def clear_inputs(self):
        self.nameLineEdit.clear()
        self.lnameLineEdit.clear()
        self.emailLineEdit.clear()
        self.planComboBox.setCurrentText('basic')
        self.discountComboBox.setCurrentText('Sin descuento')
    
    
    def populate_select_plan(self):
        result = self.plan_db.get_all()
        lista = []
        for plan in result:
            lista.append(plan["plan_name"])
        
        self.planComboBox.addItems(lista)
        self.planUpdateComboBox.addItems(lista)
        
        
    def populate_select_discount(self):
        result = self.discount_db.get_all()
        lista = ['Sin descuento']
        for disc in result:
            lista.append(str(disc["percentage"])+'%')
        
        self.discountComboBox.addItems(lista)
        
        
    # UPDATE
    def open_update_socio(self):
        """ abre la ventana para actualizar los datos del socio """ 
        selected_row = self.sociosListTable.selectedItems()
        
        if selected_row:
            socio_email = selected_row[3].text()
            self.updateSocioFrame.show()
            self.populate_inputs(socio_email)
            

    def close_update(self):
        self.sociosListTable.clearSelection()
        self.populate_table()
        self.SocioInfoFrame.hide()
        self.updateSocioFrame.hide()
    
    
    def update_socio(self):
        """ Funcion para actualizar los datos del socio """
        selected_row = self.sociosListTable.selectedItems()
        socio_email = selected_row[3].text()
            
        if self.check_input('updateSocio'):
            socio = {
                "name": self.nameUpdateLineEdit.text().strip(),
                "lname": self.lnameUpdateLineEdit.text().strip(), 
                "plan": self.planUpdateComboBox.currentText(),  
            }
            result = self.socio_db.update(socio, socio_email)
            if result:
                self.close_update()
                
                
    def populate_inputs(self, socio_email):
        """llena los datos del formulario actualizar"""
        socio = self.socio_db.get_one(socio_email)
        plan = self.plan_db.get_one(socio.plan_id)
        self.nameUpdateLineEdit.setText(socio.name)
        self.lnameUpdateLineEdit.setText(socio.lname)
        self.planUpdateComboBox.setCurrentText(plan.plan_name)
