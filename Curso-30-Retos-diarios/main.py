"""
*Lenguaje: Python
*IDE recomendado: PyCharm
*Nivel: Inicial
*Enunciado: Dado un fichero excel con nombres y correos (columna nombre y columna email), realiza un script en Python que devuelva los mails únicos de la columna email.
Consideraciones: Utiliza la librería pandas para procesar el fichero Excel (.xls).
"""
import pprint

import pandas as pd
import xlrd as xlrd

file = 'C:/Users/GRISELDA/Documents/Libro1.xlsx'

wb = xlrd.open_workbook(file)

hja = wb.sheet_by_index(0)

print(f'tiene {hja.nrows} filas y {hja.ncols} columnas')

#pprint.pprint(hja.col(1))

for i in range(1,hja.nrows):
    print(hja.cell_value(i,1))
