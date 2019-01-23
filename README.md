# Feiras

Feiras is an api for dealing with street markets from São Paulo - Brazil.

## Instalation

```bash
git clone https://github.com/vinicius834/feiras.git

cd feiras

virtualenv --python=python3 venv

source venv/bin/activate

pip3 install -r requirements.txt

source venv/bin/activate

pip3 install -r requirements.txt

python manage.py makemigrations

python manage.py migrate


```
## OBS:

By default the API is using SQLITE3 as database, but you can use database you wish. 
 
## Usage

```bash
#to run tests

python manage.py test

#result and coverage report
nosetests --with-coverage --cover-package=app --verbosity=1
Creating test database for alias 'default'...
........
Name                                        Stmts   Miss  Cover
---------------------------------------------------------------
app/__init__.py                                 0      0   100%
app/admin.py                                    1      1     0%
app/migrations/0001_initial.py                  5      0   100%
app/migrations/0002_auto_20190120_1704.py       4      0   100%
app/migrations/__init__.py                      0      0   100%
app/models.py                                  21     21     0%
app/serializer.py                               6      0   100%
app/urls.py                                     9      0   100%
app/views.py                                   42      4    90%
---------------------------------------------------------------
TOTAL                                          88     26    70%
----------------------------------------------------------------------
Ran 8 tests in 0.124s

OK
Destroying test database for alias 'default'...


```

```python
#--------------------------#--------------------------#--------------------------
#create feira
POST feiras/feira/ 

#data
{
    "long": "-46550164",
    "lat": "-23558733",
    "set_cens": "355030885000091",
    "areap": "3550308005040",
    "cod_dist": "87",
    "distrito": "VILA FORMOSA",
    "cod_sub_pref": "26",
    "sub_prefe": "ARICANDUVA-FORMOSA-CARRAO",
    "regiao5": "Leste 1",
    "regiao8": "Leste",
    "nome_feira": "VILA FORMOSA",
    "registro": "4041-0",
    "logradouro": "RUA MARAGOJIPE",
    "numero": "S/N",
    "bairro": "VL FORMOSA",
    "referecia": "TV RUA PRETORIA"
}

#reponse
{
    "id": 5,
    "long": "-46550164",
    "lat": "-23558733",
    "set_cens": "355030885000091",
    "areap": "3550308005040",
    "cod_dist": "87",
    "distrito": "VILA FORMOSA",
    "cod_sub_pref": "26",
    "sub_prefe": "ARICANDUVA-FORMOSA-CARRAO",
    "regiao5": "Leste 1",
    "regiao8": "Leste",
    "nome_feira": "VILA FORMOSA",
    "registro": "4041-0",
    "logradouro": "RUA MARAGOJIPE",
    "numero": "S/N",
    "bairro": "VL FORMOSA",
    "referecia": "TV RUA PRETORIA"
}
#--------------------------#--------------------------#--------------------------
#list all
GET feiras/

[
    {
    "id": 5,
    "long": "-46550164",
    "lat": "-23558733",
    "set_cens": "355030885000091",
    "areap": "3550308005040",
    "cod_dist": "87",
    "distrito": "VILA FORMOSA",
    "cod_sub_pref": "26",
    "sub_prefe": "ARICANDUVA-FORMOSA-CARRAO",
    "regiao5": "Leste 1",
    "regiao8": "Leste",
    "nome_feira": "VILA FORMOSA",
    "registro": "4041-0",
    "logradouro": "RUA MARAGOJIPE",
    "numero": "S/N",
    "bairro": "VL FORMOSA",
    "referecia": "TV RUA PRETORIA"
    }
]

#update feira
PUT feiras/5

#data 
{
    "distrito": "OTHER FORMOSA",
   
}

#response

{
    "id": 5,
    "long": "-46550164",
    "lat": "-23558733",
    "set_cens": "355030885000091",
    "areap": "3550308005040",
    "cod_dist": "87",
    "distrito": "OTHER FORMOSA",
    "cod_sub_pref": "26",
    "sub_prefe": "ARICANDUVA-FORMOSA-CARRAO",
    "regiao5": "Leste 1",
    "regiao8": "Leste",
    "nome_feira": "VILA FORMOSA",
    "registro": "4041-0",
    "logradouro": "RUA MARAGOJIPE",
    "numero": "S/N",
    "bairro": "VL FORMOSA",
    "referecia": "TV RUA PRETORIA"
}

#--------------------------#--------------------------#--------------------------
#get by distrito(same way for the 'bairro', 'regiao5', 'nome_feira')
#EX: <distrito> = pinheiros
GET feiras/feira/distrito/<distrito>/
#EX: /feiras/feira/distrito/VILA%20FORMOSA/

#reponse
{
    "id": 5,
    "long": "-46550164",
    "lat": "-23558733",
    "set_cens": "355030885000091",
    "areap": "3550308005040",
    "cod_dist": "87",
    "distrito": "OTHER FORMOSA",
    "cod_sub_pref": "26",
    "sub_prefe": "ARICANDUVA-FORMOSA-CARRAO",
    "regiao5": "Leste 1",
    "regiao8": "Leste",
    "nome_feira": "VILA FORMOSA",
    "registro": "4041-0",
    "logradouro": "RUA MARAGOJIPE",
    "numero": "S/N",
    "bairro": "VL FORMOSA",
    "referecia": "TV RUA PRETORIA"
}

#same reponse
GET feiras/feira/nome_feira/<nome_feira>/
GET feiras/feira/bairro/<bairro>/

#--------------------------#--------------------------#--------------------------
#delete feira

DELETE feiras/5

#reponse
[]

```

## License
[GNU](https://www.gnu.org/licenses/licenses.pt-br.html)
