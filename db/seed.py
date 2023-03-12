"""Informacion inicial para app"""
import json
import os

from pathlib import Path

this_directory = os.path.dirname(Path(__file__).parent)

with open(os.path.join(this_directory, 'socios.conf')) as file:
    socios = json.load(file)

def populate_tables_dict():
    data = {
        "planes" : [
            {'plan_name': 'basic', 'price': 2000, 'data': 'Acceso a peso libre, peso integrado, cardio y clases grupales'},
            {'plan_name': 'full', 'price': 4000, 'data': 'Acceso a peso libre, peso integrado, cardio, clases grupales, pileta y acceso a todas las sucursales'}
        ],

        "descuentos" : [
            {'percentage': 50, 'applications': 12},
            {'percentage': 30, 'applications': 6},
            {'percentage': 10, 'applications': 3}
        ],
        
        "socios": socios
    }
    return data
