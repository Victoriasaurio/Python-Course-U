# Realiza un programa que pida al usuario cuantos números quiere introducir. 
# Luego lee todos los números y realiza una media aritmética.

base = 0
total = 0

cantidad_n = int(input("Cantidiad de números que desea introducir: "))
for x in range(cantidad_n):
    numero = float(input("Ingrese el número: "))
    suma = base + numero
    total += suma

print("La cantidad de números ingresados fue:",cantidad_n, ".La suma es:",total, 
      ".La media aritmética es:",total/cantidad_n)

# ------
# Otra forma
suma = 0
numeros = int(input("¿Cuántos números quieres introducir? ") )
for x in range(numeros):
    suma += float(input("Introduce un número: ") )
print("Se han introducido", numeros, "números que en total han sumado", 
        suma, "y la media es", suma/numeros)