from PySide2.QtWidgets import QApplication
from controller.main_window import SocioWindow
from db.db import Connection

# cargamos la app con los datos iniciales
conn = Connection()
conn.connection()
conn.create_and_populate_tables()

if __name__ == '__main__':
    print("Executing App")
    app = QApplication()
    window = SocioWindow()
    window.show()
    
    app.exec_()