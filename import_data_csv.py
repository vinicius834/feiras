import csv


import os
import sys

from django.core.wsgi import get_wsgi_application
from django.utils import timezone
from django.conf import settings



# derive location to your django project setting.py
proj_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
sys.path.append(proj_path)

# load your settings.py
os.chdir(proj_path)

# In essence you are actually loading up all the django components and settings
# so we gain access to djangos ORM
application = get_wsgi_application()
print(os.path.dirname(__file__))
from app.models import Feira
def read_file():
    file_path =  'feiras/DEINFO_AB_FEIRASLIVRES_2014.csv'
    with open(file_path, 'rt') as csvfile:
        file_read = csv.DictReader(csvfile, delimiter=',')
        next(file_read)
        print('Starting import data')
        for row in file_read:
            feira = instance_feira(row)
            feira.save()
        print('Success')

def instance_feira(row):
    return Feira(long=row['LONG'],
                 lat=row['LAT'],
                 set_cens=row['SETCENS'],
                 areap=row['AREAP'],
                 cod_dist=row['CODDIST'],
                 distrito=row['DISTRITO'],
                 cod_sub_pref=row['CODSUBPREF'],
                 sub_prefe=row['SUBPREFE'],
                 regiao5=row['REGIAO5'],
                 regiao8=row['REGIAO8'],
                 nome_feira=row['NOME_FEIRA'],
                 registro=row['REGISTRO'],
                 logradouro=row['LOGRADOURO'],
                 numero=row['NUMERO'],
                 bairro=row['BAIRRO'],
                 referecia=row['REFERENCIA'])


read_file()


