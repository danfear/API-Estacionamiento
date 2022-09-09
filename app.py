###módulo principal, donde se despliega el servidor

from flask import Flask, jsonify
from routes.auth import routes_auth
from routes.users_github import users_github
from dotenv import load_dotenv
import Reportes
import Ingreso

app = Flask(__name__) #servidor

app.register_blueprint(routes_auth, url_prefix="/api")
app.register_blueprint(users_github, url_prefix="/api")

#Ingreso y salida de vehículos

@app.route('/ingreso/<string:placa>/<string:tipo>', methods=['GET', 'POST']) #agregar registro de vehículo
def addregistro(placa, tipo):
    Ingreso.ingresar(placa, tipo)
    return jsonify({"message": "Vehiculo agregado satisfactoriamente"})

@app.route('/salida/<string:placa>', methods=['GET', 'PUT']) #registrar salida de vehículo
def exitregistro(placa):
    result = Ingreso.salir(placa)
    return jsonify({"message": result})

#consultas, devuelven JSON

#Para setConsulta1 y setConsulta1 las fechas introducidas deben ser string de formato YYYY-MM-DD

@app.route('/consulta1/<string:fecha1>/<string:fecha2>', methods=['GET']) #recibe dos fechas como parámetro
def setConsulta1(fecha1, fecha2):
    dictconsulta = Reportes.consulta1(fecha1, fecha2)    
    return jsonify(dictconsulta)                        

@app.route('/consulta2/<string:fecha1>/<string:fecha2>', methods=['GET']) 
def setConsulta2(fecha1, fecha2):
    listaconsulta = Reportes.consulta2(fecha1, fecha2)
    a="Entre " + fecha1 + " y " + fecha2
    return jsonify({a : listaconsulta})

@app.route('/consulta3/<string:tipo>', methods=['GET']) #recibe tipo (str) como parámetro.
def setConsulta3(tipo):
    dictconsulta = Reportes.consulta3(tipo)    
    return jsonify(dictconsulta)

@app.route('/consulta4/<string:tipo>', methods=['GET'])
def setConsulta4(tipo):
    listaconsulta = Reportes.consulta4(tipo)   
    return jsonify({tipo : listaconsulta})

if __name__== '__main__':
    load_dotenv()
    app.run(debug=True, port=5000)