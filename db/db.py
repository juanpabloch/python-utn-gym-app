"""
Archivo donde tenemos la coneccion a la base de datos y el crud de cada modelo

"""
from db import models
from db.seed import populate_tables_dict
from db.utils import get_data, select_all
import json

from datetime import datetime
from db.utils import RegistroLogError

import os
from pathlib import Path

this_directory = os.path.dirname(Path(__file__).parent)

class Connection():
    """Clase que se utiliza para conectarse con la base de datos"""
    db = models.get_settings()
    def __init__(self) -> None:
        self.planes_data = populate_tables_dict()["planes"]
        self.descuentos_data = populate_tables_dict()["descuentos"]
        self.socios_iniciales = populate_tables_dict()["socios"]
        
        
    def connection(self, settings=None):
        """realiza un testeo de la coneccion"""
        try:
            db_text = models.get_settings(settings)
            db_text.connection()
            print("DataBase connected successfully!")
            result = {"status": 1, "message": "Conexión exitosa!"}
        except Exception as e:
            log = RegistroLogError(e, datetime.now())
            log.registrar_error()
            result = {"status": 0, "message": f"Conexión fallida: {e}"}
        
        self.db.close()
        return result
        
    
    def create_and_populate_tables(self):
        """funcion para ingresar datos iniciales de la app"""
        try:
            self.db.connect()
            self.db.create_tables([models.Planes, models.Descuentos, models.Socio, models.Application_left])
            with self.db.atomic():
                models.Planes.insert_many(self.planes_data).execute()
                models.Descuentos.insert_many(self.descuentos_data).execute()
        except Exception as e:
            log = RegistroLogError(e, datetime.now(), 'Creacion de tablas, inicio App')
            log.registrar_error()
        try:
            with self.db.atomic():
                socios_list = select_all(models.Socio)
                initial_data = socios_list if socios_list else self.socios_iniciales
                for socio in initial_data:
                    plan = get_data(models.Planes, models.Planes.id == socio['plan_id'])
                    descuento = get_data(models.Descuentos, models.Descuentos.id == socio['discount_id'])
                    socio_= models.Socio.create(
                        name= socio['name'], 
                        lname= socio['lname'], 
                        email= socio['email'], 
                        plan_id=plan.id, 
                        discount_id=descuento.id if descuento else None,
                        applications_left = socio["applications_left"]
                    )
                    socio_.save()
                    if descuento:
                        models.Application_left.insert(socio_id=socio_.id, applications=descuento.applications).execute()
            print("Tables created and initial data inserted")
        except Exception as e:
            log = RegistroLogError(e, datetime.now(), "Creacion de socios, inicio App")
            log.registrar_error()
        finally:
            self.db.close()
            with open(os.path.join(this_directory, 'socios.conf'), "w") as file:
                json.dump([], file, default=str, indent=1)
        
        
        

    
class CrudDB(Connection):
    def __init__(self) -> None:
        super().__init__()
        
    def create(self, data):
        """ funcion para crear un socio data = {name, lname, email, plan, descuento} """
        try:
            self.db.connect()
            plan = get_data(models.Planes, models.Planes.plan_name == data['plan'])
            descuento = get_data(models.Descuentos, models.Descuentos.percentage == data['descuento'])
            socio_= models.Socio.create(
                name= data['name'], 
                lname= data['lname'], 
                email= data['email'], 
                plan_id=plan, 
                discount_id=descuento, 
                applications_left=descuento.applications
            )
            socio_.save()
            if descuento:
                models.Application_left.insert(socio_id=socio_.id, applications=descuento.applications).execute()
            print("Socio creado con exito!")
            result = {"status": 1, "message": "Socio creado con exito!"}
        except Exception as e:
            log = RegistroLogError(e, datetime.now(), "Create Socio")
            log.registrar_error()
            result = {"status": 0, "message": f"ERROR create: {e}"}
        
        self.db.close()
        return result


    def update(self, data, email):
        """ funcion para actualizar un socio data = {name, lname, plan} """
        try:
            self.db.connect()
            plan = get_data(models.Planes, models.Planes.plan_name == data['plan'])
            models.Socio.update(name=data['name'], lname=data['lname'], plan_id=plan).where(models.Socio.email == email).execute()
            print("Socio actualizado con exito!")
            result = 1
        except Exception as e:
            log = RegistroLogError(e, datetime.now(), "Update Socio")
            log.registrar_error()
            result = 0
        
        self.db.close()
        return result
        
        
    def delete(self, email):
        try:
            self.db.connect()
            models.Socio.delete().where(models.Socio.email == email).execute()
            print("Socio eliminado con exito!")
            result = 1
        except Exception as e: 
            log = RegistroLogError(e, datetime.now(), "Delete Socio")
            log.registrar_error()
            result = 0
        
        self.db.close()
        return result
    
    
    def get_all(self):
        """ funcion para listar todos los socios """
        try:
            self.db.connect()
            socios = select_all(models.Socio)
        except Exception as e:
            log = RegistroLogError(e, datetime.now(), "Get all Socio")
            log.registrar_error()
            socios = []
        
        self.db.close()
        return socios
        
    
    def get_one(self, email):
        """funcion que nos retorna un socio lo buscamos por el email"""
        try:
            self.db.connect()
            socio = get_data(models.Socio, models.Socio.email == email)
        except Exception as e:
            log = RegistroLogError(e, datetime.now(), "Get one Socio")
            log.registrar_error()
            socio = {}
        
        self.db.close()
        return socio

    
    def ban_socio(self, email):
        """ funcion para prohibir un socio """
        try:
            self.db.connect()
            models.Socio.update(active=0,).where(models.Socio.email == email).execute()
            print(f"Socio {email} no esta mas activo")
            result = 1
        except Exception as e:
            log = RegistroLogError(e, datetime.now(), "Ban Socio")
            log.registrar_error()
            result = 0
        
        self.db.close()
        return result
    
    
    def activate_socio(self, email):
        """ funcion para activar un socio """
        try:
            self.db.connect()
            models.Socio.update(active=1,).where(models.Socio.email == email).execute()
            print(f"Socio {email} activado")
            result = 1
        except Exception as e:
            log = RegistroLogError(e, datetime.now(), "Activate Socio")
            log.registrar_error()
            result = 0
        
        self.db.close()
        return result
        
    
    def discount_socio_applications(self, email):
        """ funcion para disminuir las aplicaciones de los descuentos realizar al final del cobro"""
        result = 0
        try:
            socio = self.get_one(email)
            if socio.applications_left > 1:
                socio.applications_left -= 1
                socio.save()
                result = 1
            else:
                socio.discount_id = None
                socio.applications_left=0
                socio.save()
                result = 1
        except Exception as e:
            log = RegistroLogError(e, datetime.now(), "Discount socio applications Socio")
            log.registrar_error()
            result = 0
        
        self.db.close()
        return result
    
    
    # def add_or_change_discount(self, email, data):
    #     try:
    #         self.db.connect()
    #         descuento = get_data(models.Descuentos, models.Descuentos.percentage == data['descuento'])
    #         models.Socio.update(discount_id=descuento).where(models.Socio.email == email).execute()
    #         if descuento:
    #             socio = self.get_one(email)
    #             models.Application_left.update(applications=descuento.applications).where(models.Application_left.socio_id == socio.id).execute()
    #         print("Descuento actualizado con exito!")
    #     except Exception as error:
    #         print("ERROR: ", error)
    #     finally:
    #         self.db.close()
    
    
    def drop_table(self):
        self.db.connect()
        self.db.drop_tables(models.Socio)    
        self.db.close()
        
    
    
class DiscountCrud(Connection):
    def __init__(self) -> None:
        super().__init__()
        
    def get_all(self):
        """ funcion para listar todos los descuentos """
        try:
            self.db.connect(reuse_if_open=True)
            descuentos = select_all(models.Descuentos)
        except Exception as e:
            log = RegistroLogError(e, datetime.now(), "Get all Descuentos")
            log.registrar_error()
            descuentos = []
        
        self.db.close()
        return descuentos
    
    
    def get_one(self, id):
        try:
            self.db.connect(reuse_if_open=True)
            descuento = get_data(models.Descuentos, models.Descuentos.id == id)
        except Exception as e:
            log = RegistroLogError(e, datetime.now(), "Get one Descuentos")
            log.registrar_error()
            descuento = {}
        
        self.db.close()
        return descuento
    
    
    
class PlanesCrud(Connection):
    def __init__(self) -> None:
        super().__init__()
        
    def get_all(self):
        """ funcion para listar todos los planes """
        try:
            self.db.connect(reuse_if_open=True)
            planes = select_all(models.Planes)
        except Exception as e:
            log = RegistroLogError(e, datetime.now(), "Get all Planes")
            log.registrar_error()
            planes = []
        
        self.db.close()
        return planes
    
    
    def get_one(self, id):
        try:
            self.db.connect(reuse_if_open=True)
            plan = get_data(models.Planes, models.Planes.id == id)
        except Exception as e:
            log = RegistroLogError(e, datetime.now(), "Get one Descuentos")
            log.registrar_error()
            plan = {}
        
        self.db.close()
        return plan