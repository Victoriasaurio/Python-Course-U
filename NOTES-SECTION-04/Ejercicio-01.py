# Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos 
# (es suficiene con mostrar True o False):

# Si los dos números son iguales
# Si los dos números son diferentes
# Si el primero es mayor que el segundo
# Si el segundo es mayor o igual que el primero

number_1 = int(input("Ingrese el primer número --> "))
number_2 = int(input("Ingrese el segundo número --> "))

print("Iguales?", number_1 == number_2)
print("Diferentes?", number_1 != number_2)
print("Primero, mayor?", number_1 > number_2)
print("Segundo, mayor o igual?", number_1 <= number_2)