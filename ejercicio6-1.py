
class Vehiculo():    #clase
    color='azul'     #atributos o propiedades
    ruedas=4
    puertas=4



class Coche(Vehiculo):   #clase Coche hereda de vehiculo
    velocidad=200
    cilindradas= 973



auto=Coche()  #instancia de la clase coche.

print(auto.color,auto.ruedas,auto.puertas,auto.velocidad,auto.cilindradas)
