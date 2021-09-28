# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
comparacion = ""
if (numero_1 > numero_2):
    comparacion = "MAYOR"
elif (numero_1 < numero_2):
    comparacion = "MENOR"    
else:
    comparacion="IGUAL"
# Imprima en pantalla según corresponda
print('Comparacion entre', numero_1, ' y ', numero_2, ' indica que ', numero_1, ' es ', comparacion, numero_2) 

# Verifique si el numero_1 positivo, negativo o cero
comparacion = ""
if (numero_1 > 0):
    comparacion = "POSITIVO"
elif (numero_1 < 0):
    comparacion = "NEGATIVO"    
else:
    comparacion="CERO"
# Imprima el resultado en cada caso
print(numero_1, ' es ', comparacion) 

# Verifique si el numero_1 es mayor a 0 y menor a 100
comparacion = ""
if (numero_1 > 0) and (numero_1 < 100):
    comparacion = "en el RANGO (1-99)"
else:
    comparacion = "FUERA del RANGO (1-99)"   
# Imprima en pantalla si se cumple o no la condición
print(numero_1, comparacion) 

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
if (numero_1 < 10) and (numero_2 > -2):
    comparacion = '(' + str(numero_1), ' es menor a 10 y ' + str(numero_2), ' mayor a -2)'
else:
    comparacion = 'NO se cumple que (' + str(numero_1), ' es menor a 10 y ' +  str(numero_2), ' mayor a -2)'
# Imprima en pantalla si se cumple o no la condición
print(comparacion) 