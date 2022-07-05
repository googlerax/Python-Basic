#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.


bisiesto =int(input('Introduce el año'))

if bisiesto % 4 == 0 and (bisiesto % 100 != 0 or bisiesto % 400 == 0):
	print("Es año bisiesto")
else:
	print("No es año bisiesto")



