import time

from operations import *

suma =sumar(48,0.5)
print('La suma es de: ',suma)

resta= restar(400,96)
print('La resta es de: ',resta)

multi = multiplicar(85,36)
print('La multiplicacion da: ',multi)

div = dividir(45,100)
print('La division es de: ',div)


#-----------------------------------------------------------------------------------#

salida = time.localtime().tm_hour


if (salida < 19):
    def falta():
        return 19 - salida
    print('Son las',salida,'y faltan',falta(),'Horas para salir del trabajo.')

elif (salida == 19):
    print('Es hora de irse')



hora = time.strftime('%H')

print(hora)


peso = input('Introduce tu peso en kg')
estatura = input('Introduce tu estatura en metros')

imc = round(float(peso) / float(estatura) ** 2,2)



print('Tu indice de masa corporal es:',str(imc))