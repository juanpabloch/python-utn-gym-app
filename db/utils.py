"""Funciones y Clases utiles para la app"""
import os
from pathlib import Path

def get_data(Model, query):
    """Funcion para realizar una peticion a la base de datos"""
    results = Model.select().where(query).limit(1) 
    return results[0] if len(results) > 0 else None


def select_all(Model):
    """Retorna todos los elementos de una tabla en la base de datos"""
    return [data for data in Model.select().dicts()]


class RegistroLogError(Exception):
    """Clase para registro de un log de errores"""
    BASE_DIR = os.path.dirname((os.path.abspath(Path(__file__).parent)))
    ruta = os.path.join(BASE_DIR, 'errorLog.txt')
    
    def __init__(self, error, fecha, proceso, *args: object) -> None:
        self.error = error
        self.fecha = fecha
        self.proceso = proceso
        
    def registrar_error(self):
        log = open(self.ruta, 'a')
        log.write(f'{self.fecha} -- info: {self.proceso} -- error: {self.error}\n')
        log.close()
        