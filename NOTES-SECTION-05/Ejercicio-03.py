# Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100.

inicio = 0
total = 0
for par in range(101):
    # print(par)
    if(par%2 == 0):
        suma = inicio + par
        total += suma
print("El resultado es, ", total)

# Otra forma 
suma = sum( range(0, 101, 2) )
print(suma)