
import math

#Calculadora de IMC (Indice de masa corporal)

#IMC menos de 18.5, rango de peso insuficiente.
#IMC entre 18.5 y 24.9, rango de peso normal o saludable.
#IMC entre 25.0 y 29.9, rango de sobrepeso.
#IMC es 30.0 o superior, rango de obesidad.

peso = input('Introduce tu peso en kg')
estatura = input('Introduce tu estatura en metros')

imc = round(float(peso) / float(estatura) ** 2,2)



print('Tu indice de masa corporal es:',str(imc))
