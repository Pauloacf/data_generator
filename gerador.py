import sys
from data import data_generator
from CSV import _csv
from JSON import _json
from SQL import _sql
from SQL import criartabela
'''from HTML import _html'''

arguments = []
arguments = sys.argv[1:3]

n = int(arguments[0])
tipo = arguments[1]

data_generator.persona(n)

if tipo == 'csv':
    _csv.generate_csv()
elif tipo == 'json':
    _json.generate_json()
elif tipo == 'sql':
    criartabela.create_table()
    _sql.generate_sql()
else:
    print("invalid arguments")
