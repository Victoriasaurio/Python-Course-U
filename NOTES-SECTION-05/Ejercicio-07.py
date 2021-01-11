# Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
# pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = [1,2,3,4,5,6,7,8,9]
lista_2 = [5,6,4]

lista_3 = []
for numero in lista_1:
    if numero in lista_2 and numero not in lista_3:
        lista_3.append(numero)

print(lista_3)