import os
from pathlib import Path

def get_data(Model, query):
    results = Model.select().where(query).limit(1) 
    return results[0] if len(results) > 0 else None


def select_all(Model):
    return [data for data in Model.select().dicts()]


class RegistroLogError(Exception):
    BASE_DIR = os.path.dirname((os.path.abspath(Path(__file__).parent)))
    ruta = os.path.join(BASE_DIR, 'errorLog.txt')
    
    def __init__(self, error, fecha, *args: object) -> None:
        self.error = error
        self.fecha = fecha
        
    def registrar_error(self):
        log = open(self.ruta, 'a')
        log.write(f'{self.fecha} -- error: {self.error}\n')
        log.close()
        