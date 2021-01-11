# Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# En caso de introducir una opción inválida, el programa informará de que no es correcta.

n_1 = float(input("Introduzca un número: "))
n_2 = float(input("Introduzca un número: "))

op = int(input("¿Que operación desea realiza? 1)Suma 2)Resta 3)Multiplicación - "))

while(True):
    if(op == 1):
        print("La suma es: ", n_1 + n_2)
        break
    elif(op == 2):
        print("La resta es: ", n_1-n_2)
        break
    elif(op == 3):
        print("La multiplicación es: ", n_1 * n_2)
        break
    else:
        print("Número inválido")
        break