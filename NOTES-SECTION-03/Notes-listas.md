### Listas
Listas variadas <br>
lista = [4, "Hola", 9.81, "Mundo"]
```
lista[-1:]      #['Mundo']
lista[-3:]      #['Hola', 9.81, 'Mundo']
```
Concatenación de las listas
```
numeros = [0,1,2,3]
n = numeros + [4,5,6,7]         #[1,2,3,8,5,6,7]
```
Obtener datos indicando su índice
```
n[2]    #3
n[6]    #7
```
Cambiando de valor en una lista
```
n[3] = 4
n           #[1,2,3,4,5,6,7]

Cambiando de lista a letras.

letras = ['a','b','c','d','e','f']
letras[:3] = ['A','B','C']
letras                              #['A','B','C','d','e','f']
```
Añade algún valor hasta el final de la lista - append
```
n.append(8)
n           #[1,2,3,4,5,6,7,8]
```
También es posible añadir valores utilizando expresiones aritméticas. Por ejemplo:
```
n.append(3*3)
```
Convertir una lista en una lista vacía:
```
letras = []

también puede ser realizando:

letras[:3] = []         #['d','e','f']
```
### Sublistas anidadas
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]
```
r               #[[1,2,3],[4,5,6],[7,8,9]]
r[0]            #[1,2,3]
r[-1]           #[7,8,9]

Para imprimir los números por medio de coordenadas.

r[0][0]         #1
r[1][1]         #5
r[2][2]         #9
r[1][2]         #6
r[2][1]         #8
```