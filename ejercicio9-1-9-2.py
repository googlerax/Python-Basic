from functools import reduce


items = input("Introduce países separados por comas:\n")

paises = [pais for pais in items.split(",")]

print(",".join(sorted(list(set(paises)))))

#----------------------------------------------ejercicio 2-------------------------------------------#

lista=[14,54.8,7,0,15,99,52,70,11]

def impar(x):
    if x % 2 == 0:
        return True


def sum(a,b):
    return a + b

num_impar = filter(impar,lista)
suma = reduce(sum,num_impar)

print(f'Los numeros impares de la lista sumados entre si da como resultado: {suma}')
