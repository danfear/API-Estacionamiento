###modulo reportes, contiene las funciones de las consultas

import datetime as dt
from Bases import conn_db

#realiza la consulta 1: total de veículos y de recaudo dentro de un intervalo de tiempo
#retorna un diccionario con clave=intervalo de tiempo y valor=totales
def consulta1(f, f2):
    db = conn_db()
    cur = db.cursor()

    fecha = dt.datetime.strptime(f, '%Y-%m-%d')  
    fecha2 = dt.datetime.strptime(f2, '%Y-%m-%d')
    cur.execute('SELECT Costo FROM Estancias WHERE HoraEntrada >= ? AND HoraSalida <= ? AND Costo IS NOT NULL;', (fecha, fecha2)) 
    consulta=cur.fetchall()
    dicc=dict()
    totales=dict()
    sumarecaudado=0

    #suma los totales
    for n in consulta:
        sumarecaudado+=n[0]
    totales['total_vehiculos']=len(consulta)
    totales['total_recaudado']=sumarecaudado
    a="Entre " + f + " y " + f2
    dicc[a]=totales
    
    return dicc

#realiza la consulta 2: información de los vehiculos que entraron y salieron dentro de un intervalo de tiempo
#retorna una lista con toda la información para cada vehiculo         
def consulta2(f, f2):
    db = conn_db()
    cur = db.cursor()
       
    fecha = dt.datetime.strptime(f, '%Y-%m-%d')  
    fecha2 = dt.datetime.strptime(f2, '%Y-%m-%d')
    cur.execute('SELECT Estancias.ID, Placa, HoraEntrada, HoraSalida, Tiempo, Tipos.Tipo, Costo FROM Estancias JOIN Tipos ON Estancias.Id_tipo=Tipos.ID WHERE HoraEntrada >= ? AND HoraSalida < ? AND Costo IS NOT NULL;', (fecha, fecha2))
    consulta=cur.fetchall()
    lista=list()
    
    for n in consulta:
        listafechas=list()
        auto=dict()
        auto['Id']=n[0]
        auto['Placa']=n[1]
        listafechas.append(n[2])
        listafechas.append(n[3])
        auto['Fechas']=listafechas
        auto['Tiempo_estacionado']=n[4]
        auto['Tipo']=n[5]
        auto['Costo']=n[6]
        lista.append(auto)
    
    return lista

#realiza la consulta 3: total de veículos y de recaudo discriminando por tipo de automovil
#retorna un diccionario con clave=tipo y valor=totales        
def consulta3(tipo):
    db = conn_db()
    cur = db.cursor()
    
    cur.execute('SELECT ID FROM Tipos WHERE Tipo=?', (tipo, ))
    tipo=cur.fetchone()[0]
    
    cur.execute('SELECT Tipos.Tipo, Costo FROM Estancias JOIN Tipos ON Estancias.Id_tipo=Tipos.ID WHERE Estancias.Id_tipo=? AND Estancias.Costo IS NOT NULL', (tipo, ))
    consulta=cur.fetchall()

    dicc=dict()
    totales=dict()
    sumarecaudado=0

    for n in consulta:
        sumarecaudado+=n[1]
        t=n[0]

    totales['total_vehiculos']=len(consulta)
    totales['total_recaudado']=sumarecaudado
    dicc[t]=totales
    
    return dicc
    
#realiza la consulta 4: información de los vehiculos que entraron y salieron discriminado por tipo
#retorna una lista con toda la información para cada vehiculo  
def consulta4(tipo):
    db = conn_db()
    cur = db.cursor()
    
    cur.execute('SELECT ID FROM Tipos WHERE Tipo=?', (tipo, ))
    tipo=cur.fetchone()[0]
    
    cur.execute('SELECT Estancias.ID, Placa, HoraEntrada, HoraSalida, Tiempo, Costo, Tipos.Tipo FROM Estancias JOIN Tipos ON Estancias.Id_tipo=Tipos.ID WHERE Estancias.Id_tipo=? AND Estancias.Costo IS NOT NULL', (tipo, ))
    consulta=cur.fetchall()
    lista=list()
    
    for n in consulta:
        listafechas=list()
        auto=dict()
        auto['Id']=n[0]
        auto['Placa']=n[1]
        listafechas.append(n[2])
        listafechas.append(n[3])
        auto['Fechas']=listafechas
        auto['Tiempo_estacionado']=n[4]
        auto['Total_pagado']=n[5]
        lista.append(auto)
    
    return lista
