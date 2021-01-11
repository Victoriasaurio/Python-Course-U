### Sentencia if
### Sentecia Elif
Se encadena a un if para comprobar otra posible condición, siempre que la anterior no se cumpla.

### While
Condición para iterar, recorre los registros hasta encontrar coincidencias o termina el contador.
Es posible utilizar else en un while. Por ejemplo:
``` 
c = 0
while c <= 5:
    c+=1
    print(c)
else:
    print("Se ha acompletado el ciclo")
``` 

Menú interactivo
```
while(true):
    print("Que hacer? 1) Saludar 2)Sumar 3)salir")
    op = int(input())
    if op == 1:
        print("Hola")
    elif op == 2:
        n1 = int(intput("número 1: "))
        n2 = int(intput("número 2: "))
        print(n1 + n2)
    elif op == 3:
        print("Adios")
        break
    else:
        print("Número no válido")
```

### For
Podemos recorrer listas, cadena de caracteres ("Hola")
Ejemplos:
```
n = [1,2,3,4,5]

for num in n:
    print(n)
```

Manipulación del contenido de la lista
```
indice = 0
numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    numeros[indice] *= 10
    indice += 1

print(numeros)

Otra manera:
enumerate - Devuelve un índice y un número. Este for incremente el índice por si solo.

numeros = [1,2,3,4,5,6,7,8,9,10]
for indice, numero in enumerate(numeros):
    numeros[indice] *= 10
print(numeros)
```
Sin embargo, es imposible cambiar el valor de una cadena. Pero podemos obtener la misma logitud apartir de la cadena. Por ejemplo:
```
cadena_1 = "Hola mundo"
cadena_2 = ""

for caracter in cadena_1:
    cadena_2 += "*"
    cadena_2 += caracter * 2

print(cadena_2)             #"**********"
                            #"HHoollaa  mmuunnddoo"
```

Range no ocupa memoria porque se interpreta durante el tiempo de ejecución.
Podemos establecer un rango:
```
for i in range(10):
    print(i)            #Imprime del 0-9

print(range())          #range(0, 10), en caso de declarar o establecer el límite 10.

list(range(10))         #[0,1,2,3,4,5,6,7,8,9], En consola se imprime.
```
