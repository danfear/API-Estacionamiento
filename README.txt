API Estacionamiento.
Permite registrar la entrada y salida de vehículos de un estacionamiento.
Además realiza cuatro tipos de consulta y las devuelve en formato JSON.

El repositorio contiene los siguientes archivos:
-Bases.py: Módulo donde se crean las bases de datos, 
debe ejecutarse una vez solo si en el repositorio no se encuentra
la base de datos 'Estacionamiento.sqlite'.
-Ingreso.py: Contiene las funciones de registro de entrada y
registro de salida del estacionamiento, las cuales retornan mensajes de aviso.
-Reportes.py: Contiene las funciones encargadas de ejecutar los cuatro tipos de consulta:
1. Reporte de total de autos y total de dinero recaudado en un intervalo de tiempo.
2. Reporte de datos como id, placa, fecha y hora de entrada y salida, tiempo estacionado,
tipo de vehiculo y total pagado según un intervalo de tiempo.
3. Reporte de total de autos y total de dinero recaudado discriminando
por tipo de vehículo
4. Reporte de datos como id, placa, fecha y hora de entrada y salida, tiempo estacionado,
 y total pagado discriminando por tipo de vehículo.
-app.py: El módulo principla encargado de darle al programa el caracter de API. Devuelve 
formatos JSON según el tipo de solicitud que se realice.

Instrucciones de despliegue:
1. Ejectute el archivo app.py
El valor del localhost es 5000
2. Puede ingresar un vehículo con la siguiente instrucción como ejemplo:
localhost:5000/ingreso/was123/bicicleta, donde 'was123' es la placa del vehículo y
'bicicleta' es el tipo, la hora de entrada se registra automaticamente.
Para un registro correcto se requiere que se introduzcan
los tipos de vehículo exactamente como se muestran a continuación:
'bicicleta', 'moto', 'automovil', 'vehiculo pesado', 'vehiculo oficial'.
3. Puede dar salida a un vehículo con la siguiente instrucción como ejemplo:
http://localhost:5000/salida/def123, donde 'def123' es la placa del vehículo.
Si se introduce una placa y no se encuentre en base de datos aparecerá un
mensaje de operación incorrecta.
4. Puede realizar los cuatro tipos de consulta descritos anteriormente:
a. Para la consulta 1 debe introducir una instrucción como la siguiente
http://localhost:5000/consulta1/2022-09-09/2022-09-10, donde los dos ultimos valores
son las fechas de inicio y final respectivamente. Es importante introducir las fechas
únicamente en el siguiente formato 'YYYY-MM-DD'
b. Para la consulta 2 debe introducir una instrucción como la siguiente
http://localhost:5000/consulta2/2022-09-09/2022-09-10, con las mismas recomendaciones de
la consulta anterior
c. Para la consulta 3 debe introducir una instrucción como la siguiente
http://localhost:5000/consulta3/moto, donde 'moto' es un tipo de vehiculo
que se puede consultar. Se debe tener en cuenta la forma correcta de introducir los tipos
previamente mencionada
d. Para la consulta 4 debe introducir una instrucción como la siguiente
http://localhost:5000/consulta4/automovil, donde 'automovil' es un tipo de vehiculo
que se puede consultar. Se debe tener en cuenta la forma correcta de introducir los tipos
previamente mencionada

Los archivos function_jwt, .env y carpetas routes y venv pertenecen al proceso de autenticación
con JWT
