# Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. 
# Al parecer contiene el nombre de un alumno y la nota de un exámen. 
# ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?

# Nombre Apellido ha sacado un Nota de nota.

cadena = "zeréP nauJ, 01"

nombre = cadena[-5] + cadena[-6] + cadena[-7] + cadena[-8]
apellido = cadena[-10] +cadena[-11] + cadena[-12] + cadena[-13] + cadena[-14]
nota = cadena[-1] + cadena[-2]

print(nombre + " " + apellido + " ha sacado un " + nota + " de nota")

# Otra solución del ejercicio
cadena_volteada = cadena[::-1] # Invierte la cadena - 10 ,Juan Pérez
print(cadena_volteada[4:], "ha sacado un", cadena_volteada[:2], "de nota.")