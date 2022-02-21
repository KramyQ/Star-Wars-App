from odds_computer import OddsComputer
import sqlite3
import sys
import json

sql = sqlite3.connect('universe.db')

start_parameters_adress = sys.argv[1]
empire_parameters_adress = sys.argv[2]
f = open(start_parameters_adress)
start_parameters = json.load(f)
f.close()
f = open(empire_parameters_adress)
empire_parameters = json.load(f)
f.close()
planetConnections = []
for row in sql.execute('SELECT * FROM ROUTES'):
    planetConnections.append({'link': [row[0], row[1]], 'travelTime': row[2]})

print(OddsComputer(start_parameters, empire_parameters, planetConnections).get_success_rate())