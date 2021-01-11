# Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una 
# longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).

cadena = input("Introduzca una cadena: ")
print(len(cadena) >= 3 and len(cadena) < 10)