from flask import Flask, jsonify, request
import json
from flask_cors import CORS  # Importar CORS desde flask_cors
import csv
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


# Cargar datos del archivo JSON al iniciar la aplicación
with open('usuarios.json', 'r') as file:
    datos_json = json.load(file)

@app.route('/billetera/contactos', methods=['GET', 'POST'])
def obtener_contactos():
    if request.method == 'GET':
        minumero = request.args.get('minumero')
    elif request.method == 'POST':
        minumero = request.json.get('query')  # Obtener el número de cuenta del cuerpo de la solicitud

    contactos_info = []

    for usuario in datos_json['usuarios']:
        if usuario['numero'] == minumero:
            for contacto_numero in usuario['contactos']:
                for user in datos_json['usuarios']:
                    if user['numero'] == contacto_numero:
                        contactos_info.append({'numero': user['numero'], 'nombre': user['nombre']})

    return jsonify({"contactos": contactos_info})

    
@app.route('/billetera/historial', methods=['GET', 'POST'])
def obtener_historial_por_numero():
    if request.method == 'GET':
        numero_cuenta = request.args.get('minumero')
    elif request.method == 'POST':
        numero_cuenta = request.json.get('query')  # Obtener el número de cuenta del cuerpo de la solicitud
    historial = []

    with open('transacciones.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['minumero'] == numero_cuenta or row['numerodestino'] == numero_cuenta:
                print(row['minumero'])
                historial.append({
                    'minumero': row['minumero'],
                    'numerodestino': row['numerodestino'],
                    'valor': row['valor']
                })
    
    return jsonify({"historial": historial})

if __name__ == '__main__':
    app.run(debug=True)
