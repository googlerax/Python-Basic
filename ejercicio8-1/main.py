#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis
# y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.


# creacion  y apertura del archivo .txt
from pickle import dump, load

import self as self

create_file = open('archivo.txt','a')

#Escritura del archivo .txt
create_file.write('Mi nombre es \n')
#cierre del archivo
create_file.close()

#segundo acceso al archivo
create_file = open('archivo.txt','r+')
create_file.readline()
create_file.write('Griselda\n')
create_file.close()


class Vehiculo:
    def __init__(self,marca,color):
        self.marca= marca
        self.color=color

    def __str__(self):
        return f'Es un auto de marca {self.marca} y de color {self.color}'


auto=Vehiculo('Fiat','negro')
print(auto)

f = open('model_auto','w+b')

dump(auto,f) # dumps() nos permite serializar los objetos de Python como un str.

f.seek(0)
nuevo_auto = load(f)  #carga del archivo

print(nuevo_auto)
f.close()





