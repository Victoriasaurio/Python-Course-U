### Indice
Indice en un string
```
palabra = "Python"
palabra[0]  #P
palabra[3]  #h
palabra[-1] #n
palabra[-2] #o
```

### Slicing
Límite entre los valores de una cadena.
```
palabra = "Python"
palabra[0:2]                #'Py'
palabra[:]                  #'Python'
palabra[2:]                 #'thon'
palabra[-2:]                #'on'
palabra[:2] + palabra[2:]   #'Python"
```

Cambiando la primera letra manualmente
```
palabra = "N" + palabra[1:]
#Nython
```

Longitud de algo. En este caso del string:
len(palabra)