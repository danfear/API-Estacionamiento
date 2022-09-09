###Módulo bases. Sólo se debe ejecutar una vez
#Su función es crear la base de datos y añadir a
#la tabla 'Tipos' los tipos de automovil

import sqlite3

Database_name = 'Estacionamiento.sqlite'

#función que conecta con la base de datos y retorna esa conexión
def conn_db():
    conn = sqlite3.connect(Database_name)
    return conn

#función que crea tabla con los tipos de vehículo e inserta sus valores
def crearTipoAuto(tipo, valor):
    
    db = conn_db()
    cur = db.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Tipos
        (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Tipo TEXT NOT NULL UNIQUE,
        ValorMinuto INTEGER NOT NULL)''')
    
    cur.execute('INSERT INTO Tipos (Tipo, ValorMinuto) values (?, ?)', (tipo, valor))
    
    db.commit()
    cur.close()
    db.close()

#función que crea la tabla instancias (tabla principal) contiene la primary key de la tabla 'Tipos'    
def crearEstancias():
    
    db = conn_db()
    cur = db.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Estancias
        (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
        Placa TEXT,
        Id_tipo INTEGER,
        HoraEntrada TIMESTAMP, 
        HoraSalida TIMESTAMP,
        Tiempo TIMESTAMP, 
        Costo INTEGER)''')

    cur.close()
    db.commit()
    db.close()
    
crearEstancias()

#Si se desea ingresar un nuevo tipo de vehículo basta con
#llamar a la función 'crearTipoAuto' y por parámetros introducir
#el tipo de auto en comillas y el costo de parqueo por minuto en pesos
#Ejemplo:
#crearTipoAuto("cuatrimoto", 20)

#Se comentan los siguientes llamados a función debido a que la tabla ya está creada
#crearTipoAuto("bicicleta", 5)
#crearTipoAuto("moto", 10)
#crearTipoAuto("automovil", 30)
#crearTipoAuto("vehiculo pesado", 40)
#crearTipoAuto("vehiculo oficial", 0)