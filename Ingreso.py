import datetime as dt
from Bases import conn_db

#función que ingresa en base de datos la placa y el tipo de vehiculo que entra al estacionamiento
def ingresar(placa, tipo):

    fecha=dt.datetime.now()
    db = conn_db()
    cur = db.cursor()

    #tipo pasará a tener valor numérico de la foreign key Id_tipo de la tabla Estancias
    cur.execute('SELECT ID FROM Tipos WHERE Tipo=?', (tipo, ))
    tipo=cur.fetchone()[0]

    #vehiculo insertado
    cur.execute('INSERT INTO Estancias (Placa, Id_tipo, HoraEntrada) values (?, ?, ?)', (placa, tipo, fecha))

    db.commit()
    cur.close()
    db.close()

#función que registra cuando un vehículo abandona el estacionamiento
#retorna el valor a pagar siempre que la placa se escriba correctamente
def salir(placa):
    
    fechasalida=dt.datetime.now()
    db = conn_db()
    cur = db.cursor()
    
    cur.execute('SELECT HoraEntrada, ID FROM Estancias WHERE Placa=?', (placa, ))

    try:
        #recupera  la fecha de entrada en base de datos
        consulta=cur.fetchone()
        id= consulta[1]
        fechaentrada = dt.datetime.strptime(consulta[0], '%Y-%m-%d %H:%M:%S.%f')
        minutos = round((fechasalida - fechaentrada) / dt.timedelta(minutes=1))
    
        #recupera valor de parqueo por minuto y calcula costo y tiempo estacionado
        cur.execute('SELECT Tipos.ValorMinuto FROM Estancias JOIN Tipos ON Estancias.Id_tipo=Tipos.ID WHERE Estancias.ID=?', (id, ))
        valorpormin=cur.fetchone()[0]
        pago=minutos*valorpormin
        t= str(minutos//60) + ":" + str(minutos%60)
        tiempo=dt.datetime.strptime(t, '%H:%M')
    
        #actualiza información en base de datos
        cur.execute('UPDATE Estancias SET HoraSalida=? WHERE ID=?', (fechasalida, id))
        cur.execute('UPDATE Estancias SET Costo=? WHERE ID=?', (pago, id))
        cur.execute('UPDATE Estancias SET Tiempo=? WHERE ID=?', (tiempo, id))

        return "El costo de estacionamiento para el vehiculo de placas '" + placa + "' es de $" + str(pago) + " pesos."
    
    except TypeError:
        #mensaje de alerta cuando la placa introducida no es encontrada
        return "La placa introducida no esta en base de datos."
    finally:
        db.commit()
        cur.close()
        db.close()