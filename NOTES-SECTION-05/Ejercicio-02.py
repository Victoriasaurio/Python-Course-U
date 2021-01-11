# Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, 
# debe repetise el proceso hasta que lo introduzca correctamente.

numero = 0
while(numero%2 == 0):
    numero = int(input("Ingrese un número impar -> "))