# IE6: archivo: datosjson.py
import json
import datetime
 
# IE6: Abrir archivo en variable json_file (nombre exacto requerido)
with open('/home/devasc/labs/devnet-src/parsing/myfile.json') as json_file:
    # IE7: Cargar JSON con json.load en ourjson (nombre exacto requerido)
    ourjson = json.load(json_file)
 
# IE8: Imprimir token
print("Token:", ourjson['access_token'])
 
# IE8: Calcular y mostrar tiempo restante antes de expiracion
expira   = datetime.datetime.strptime(ourjson['expires_in'], "%Y-%m-%d %H:%M:%S")
ahora    = datetime.datetime.now()
restante = expira - ahora
print("Tiempo restante antes de expiracion:", restante)

