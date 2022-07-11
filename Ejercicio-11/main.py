#En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
# la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3

conn = sqlite3.connect('Alumnos.db')
cursor_db= conn.cursor()

cursor_db.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

cursor_db.execute("INSERT INTO Alumnos VALUES(1,'Maria', 'Sanchez')")
cursor_db.execute("INSERT INTO Alumnos VALUES(2,'Matias', 'Rodriguez')")
cursor_db.execute("INSERT INTO Alumnos VALUES(3,'Jorge', 'Martinez')")
cursor_db.execute("INSERT INTO Alumnos VALUES(4,'Antonia', 'Perez')")
cursor_db.execute("INSERT INTO Alumnos VALUES(5,'Matheo', 'Herrero')")
cursor_db.execute("INSERT INTO Alumnos VALUES(6,'Carla', 'Gracia')")
cursor_db.execute("INSERT INTO Alumnos VALUES(7,'Iris', 'Moutng')")
cursor_db.execute("INSERT INTO Alumnos VALUES(8,'Coro', 'Villa')")

conn.commit()


conn.close()





