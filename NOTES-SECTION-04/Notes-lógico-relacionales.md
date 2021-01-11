### Lógico 
Python tiene presente las comparaciones lógicas. Por ejemplo:
```
1+1 == 3        #false
1+1 == 2        #true
```

### Operadores lógicos
Comparaciones boleanas con lógicos
```
*** AND ***
not True                #False
not True == False       #True
True and True           #True
False and True          #False

Comparaciones aritmeticas y lógicos
a = 13
a > 10 and a < 20       #True

c = "Hola mundo"
len(c) >= 5 and c[0] == "H"      #True

*** OR ***
False or True                    #True
b = "Hola"
len(b) >= 5 or c[0] == "H"       #True

n = "Lector"
c[0] == "H" or c[0] == "h"       #False
``` 

### Relacionales
```
Comparación de números. Por ejemplo:

3 == 2      #False      #Igual
3 != 2      #True       #Distinto
3 > 2       #True       #Mayor
3 < 2       #False      #Menor
3 >= 4      #False      #Mayor o igual
3 <= 4      #True       #Menor o igual

También puede compararser cadenas de texto:

"Hola" == "Hola"        #True
c = "Python"
c[0] == "P"             #True

Comparación entre listas:

lista_1 = [1,2,3]
lista_2 = [4,5,6]

lista_1 == lista_2              #False

len(lista_1) == len(lista_2)    #True - Longitud de las listas
```