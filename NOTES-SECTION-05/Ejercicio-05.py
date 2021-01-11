# Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto 
# se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

numero = 0
lista = [0,1,2,3,4,5,6,7,8,9]

while(True):
    numero = int(input("Ingrese un número entre el 0-9 -> "))
    if(numero >= 0 and numero <= 9):
        break
    
if numero in lista:
    print(numero,"Se encuentra en la lista")
else:
    print(numero, "No se encuentra en la lista")
    