variable = 'esto es una cadena de texto.'
print(variable)
tipo = type(variable)
print('La variable es del tipo:',tipo)

variable[1] = 'x'
print(variable)       #TypeError: 'str' object does not support item assignment      String es un tipo de dato inmutable,.
