from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QAbstractItemView, QTableWidgetItem
from views.Ui_lista_cobros import ListaCobro
import pandas as pd
import os
import datetime

from db.db import CrudDB, PlanesCrud, DiscountCrud


class ListaCobroWindow(QWidget, ListaCobro):
    socio_db = CrudDB()
    planes_db = PlanesCrud()
    discount_db = DiscountCrud()
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.table_config()
        self.populate_charge_table()
        self.exitBtn.clicked.connect(self.close)
        self.downloadBtn.clicked.connect(self.download)
        

    def table_config(self):
        column_headers = ["Nombre", "Email", "Abonar"]
        self.tableListaCobro.setColumnCount(len(column_headers)) 
        self.tableListaCobro.setColumnWidth(0, 150)   
        self.tableListaCobro.setColumnWidth(1, 200)   
        self.tableListaCobro.setColumnWidth(2, 70)   
        self.tableListaCobro.setHorizontalHeaderLabels(column_headers)
        self.tableListaCobro.setSelectionBehavior(QAbstractItemView.SelectRows)
        

    def populate_charge_table(self):
        """ popula la tabla con los datos de los socios """
        data = self.get_total()
        self.totalLista.setText(str(data["total"]))
        self.tableListaCobro.setRowCount(len(data["socios"]))
        for (index_row, row) in enumerate(data["socios"]):
            for (index_cell, cell) in enumerate(row):
                self.tableListaCobro.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        
        
    def get_total(self):
        """ retorna el cobro a los socios """
        socios = self.socio_db.get_all()
        data = []
        total = 0
        for socio in socios:
            if socio['active'] == 1:
                cuota = self.planes_db.get_one(id=int(socio["plan_id"]))
                if socio["discount_id"]:
                    num = self.discount_db.get_one(id=int(socio["discount_id"]))
                    discount = int(num.percentage) * 0.01
                    t_cuota = int(cuota.price) - int((int(cuota.price)*discount))
                else:
                    t_cuota = int(cuota.price)
                data.append((socio["name"], socio["email"], t_cuota))
                total += t_cuota
        return {"total": total, "socios":data}


    def get_total_charge(self):
        socios = self.socio_db.get_all()
        data = []
        total = 0
        for socio in socios:
            if socio['active'] == 1:
                cuota = self.planes_db.get_one(id=int(socio["plan_id"]))
                if socio["discount_id"]:
                    num = self.discount_db.get_one(id=int(socio["discount_id"]))
                    discount = int(num.percentage) * 0.01
                    t_cuota = int(cuota.price) - int((int(cuota.price)*discount))
                    self.socio_db.discount_socio_applications(socio["email"])
                else:
                    t_cuota = int(cuota.price)
                data.append((socio["name"], socio["email"], t_cuota))
                total += t_cuota
        return {"total": total, "socios":data}
    
    
    def download(self):
        data = self.get_total_charge()
        data["socios"].append(("", "", ""))
        data["socios"].append(("TOTAL", "", data["total"]))
        path = os.path.abspath(os.getcwd())
        result = pd.DataFrame(data["socios"])
        result.to_excel(f'{path}/files/cobro-{self.get_date()}.xlsx')
        self.cobro_lista_message.setText(f'Se descargó el archivo "cobro-{self.get_date()}.xlsx" en la carpeta files de la aplicación')


    @staticmethod
    def get_date():
        date = datetime.datetime.now()
        date_str = date.strftime("%d%m%Y")
        return date_str