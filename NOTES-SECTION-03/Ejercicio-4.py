# A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo que queremos es obtener la nota final. 
# El problema es que cada nota tiene un valor porcentual:
# La primera nota vale un 15% del total.
# La segunda nota vale un 35% del total.
# La tercera nota vale un 50% del total.

nota_1 = 10
nota_2 = 7
nota_3 = 4

nota_1 = (nota_1*15) / 100
nota_2 = (nota_2*35) / 100
nota_3 =(nota_3*50) / 100

nota_final = nota_1 + nota_2 + nota_3

print(nota_final)

# Otra solución del ejercicio
nota_final = (nota_1 * 0.15) + (nota_2 * 0.35) + (nota_3 * 0.50)  
print("La nota final es", nota_final)