
import math

#Calculadora de IMC (Indice de masa corporal)

#IMC menos de 18.5, rango de peso insuficiente.
#IMC entre 18.5 y 24.9, rango de peso normal o saludable.
#IMC entre 25.0 y 29.9, rango de sobrepeso.
#IMC es 30.0 o superior, rango de obesidad.

peso = 55.0
estatura = 1.62

alCuadrado = math.pow(estatura,2)
imc = peso / alCuadrado

print('Tu indice de masa corporal es:',round(imc,2))