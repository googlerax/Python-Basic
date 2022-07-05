
#Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, 
# e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales. 
# Tienes que subir capturas de pantalla en una carpeta comprimida zip.




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
