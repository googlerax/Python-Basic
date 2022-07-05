#Para este ejercicio tenéis que crear en la consola de python variables que representen los siguientes datos de un contacto:
# Nombre
# Apellidos
# Edad
# Email
# Teléfono
# Casado (verdadero o falso)
# Con Hijos (verdadero o falso)
# Lista de amigos
# Películas vistas (diccionario con clave y valor. El valor será el título de la película)
# Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().



nombre = 'Marta'
apellido = 'Sanchez'
edad = 36
email = 'mgrrghs@gmail.com'
telefono = '1578663989'
casada = False
hijos = False

amigos = ['Ana','Alberto','Miguel','Pia']

pelisVistas = {
    'peli1':'Troya',
    'peli2':'Hombres de honor',
    'peli3':'Batman'
}

print(nombre,apellido,edad,'Años')
print('Edad:',edad,' ','Email:',email)
print('Casada:',casada)
print('Hijos:',hijos)

print('Sus amigos son:',amigos[0],amigos[1],amigos[2],'y',amigos[3],)
print('Peliculas vistas:',pelisVistas['peli1'],pelisVistas['peli2'],'y',pelisVistas['peli3'])


