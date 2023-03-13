"""Modelos de la app"""
from peewee import *
from datetime import datetime
import json
import os

from pathlib import Path

this_directory = os.path.dirname(Path(__file__).parent)

def get_settings(settings=None):
    """funcion para configurar la base de datos"""
    if not settings:
        with open(os.path.join(this_directory, 'settings.conf')) as file:
                settings = json.load(file)
    
    if settings['type'] == "MySQL":
        return MySQLDatabase(
            settings['name'], 
            user = settings['user'], 
            password = settings['password'],
            host = settings['host'], 
            port = 3306
        )
    elif settings['type'] == "SQLite":
        return SqliteDatabase(settings['name'])


db = get_settings()

class BaseModel(Model):
    class Meta:
        database = db
        

class Planes(BaseModel):
    plan_name = CharField(max_length=255, unique=True)
    price = IntegerField()
    data = TextField()


class Descuentos(BaseModel):
    percentage = IntegerField(unique=True)
    applications = IntegerField()
    
                        
class Socio(BaseModel):
    name = CharField(max_length=255)
    lname = CharField(max_length=255)
    email = CharField(max_length=255, unique=True)
    plan_id = ForeignKeyField(Planes, backref='socios')
    discount_id = ForeignKeyField(Descuentos, backref='socios', null=True)
    applications_left = IntegerField(default=0)
    active = IntegerField(default=1)
    created_at = DateTimeField(default=datetime.now)


class Application_left(BaseModel):
    socio_id = IntegerField()
    applications = IntegerField(null=True)
    