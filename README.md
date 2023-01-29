# PruebaTecnica

### Para correr el archivo "main.py" se necesita tener las siguiente liberiras de python 
####   $ pip install pandas
####   $ pip install psycopg2

### Para correr el archivo API.py se necesita tener las siguientes librerias de python

####   $ pip install python-tk


#### Adicional a esto, el repositorio tiene el .exe de API.py , por si solo se requiere probar la API

## Contenido del repositorio

En este repositorio de tiene un archivo "main.ipynb" el cual es un archivo jupyter, el cual tiene la descipcion paso apaso de como se limpio
y transformo la informacion del data set principal en uno nuevo ya con datos limpios.

En este repositorio se adjuntan los archivos de configuracion de docker-compose.yml, para realizar una imagen de docker,
la cual contine una imagen de "postgesql" y una imagen de "pgadmin" asi se podra configurar la base de datos desde la interfaz
de pg admin.

Aunado a esto se tiene una Dockerfile el cual contine una imagen de python:3.8-slim-buster para poder correr "main.py"
el cual es un archivo que contine una clase CHARGES, la cual inserta el data set limpio, dentro de la base de datos de postgreSQL,
asi mismo, tiene una funcion llamada "VIEW". La cual es una sentencia query, que nos ayuda a ver el monto total transaccionado por 
día para las diferentes compañías.

Finalmente se tiene un archivo llamado prueba.sql el cual es un archivo que se puede importar dentro de pgadmin, este contine
la base datos ya con la informacion del data set limpio , y este mismo archivo ya tiene implementada la view con el nombre
"Monto_por_Dia".




