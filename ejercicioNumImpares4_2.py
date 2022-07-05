numInicial=5
numFinal=17

lista=[]
lista.append(numInicial)
lista.append(numFinal)

print(lista)

def encontrarNum(lsta):
    inicio = lsta[0]
    final = lsta[-1]
    return sorted(set(range(inicio, final + 1)).difference(lsta))

lsta = lista
print(encontrarNum(lsta))

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo")
            return False
    print("Es primo")
    return True

es_primo(int(input('introduce un numero')))
