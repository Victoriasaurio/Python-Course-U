### Lectura por teclado
Para que el usuario pueda igresar los datos se utiliza:
```
input()
```
Para convertir los valores basta con:
```
str = input("Ingresa un valor --> ")
15

Si queremos sumar un valor a ese 15, tendremos un error. Debemos convertir ese valor.

str = int(valor)
str + 45                #60

De ser necesario puede utilizarse:
float()
```
Para especificar un valor desde el input, puede realizarse de la sig manera:
```
entero = int(input("Ingresa un número entero --> "))
```
