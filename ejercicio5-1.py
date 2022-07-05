#Escribe una función que calcule el área de un triángulo,
# recibiendo la altura y la base como parámetros y otra función
# que calcule el área de un círculo recibiendo el radio del mismo.


altura=float(input('introduce la altura del triangulo'))
base=float(input('introduce la base del triangulo'))


def area(altura,base):
    return base * altura / 2


print('el area del triangulo es de',round(area(altura,base),2))