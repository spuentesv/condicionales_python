# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Condicionales anidados
numero_1 = 7
numero_2 = -2

# Verifique si el numero_1 es mayor a 5
#   --> En caso afirmativo, verifique si el numero_2
#       es positivo
#       --> En caso afirmativo imprima en pantalla "Resp=1"
#       --> En caso negativo imprima en pantalla   "Resp=2"
#  --> En caso negativo (numero_1 no es mayor a 5)
#      verifique si el numero_2 es mayor a 5
#       --> En caso afirmativo imprima en pantalla "Resp=3"
#       --> En caso negativo imprima en pantalla "Resp=4"

# Verifique la calificación de un estudiante según su
comparacion1 = ""
comparacion2 = ""
if (numero_1 > 5):
    comparacion1 = "numero_1:", str(numero_1), 'MAYOR a 5'
    if (numero_2 > 0):
        comparacion2 = "numero_2:", str(numero_2), 'POSITIVO'
    else:
        comparacion2 = "numero_2:", str(numero_2), 'NEGATIVO'            
else:
    comparacion1 = "numero_1:", str(numero_1), 'MENOR a 5'
    if (numero_2 > 5):
        comparacion2 = "numero_2:", str(numero_2), 'MAYOR a 5'
    else:
        comparacion2 = "numero_2:", str(numero_2), 'MENOR a 5'
print(comparacion1, ' y ', comparacion2)   
# puntaje en un examen
puntaje = 70

# Si el puntaje es mayor igual a 90 --> imprimir A
# Si el puntaje es mayor igual a 80 --> imprimir B
# Si el puntaje es mayor igual a 70 --> imprimir C
# Si el puntaje es mayor igual a 60 --> imprimir D
# Si el puntaje es menor a  60      --> imprimir F

# Debe imprimir en pantalla la calificacion
# Utilizar "if" anidados
comparacion = ""
if (puntaje >= 90):
    comparacion = "A"
elif (puntaje >= 80):
    comparacion = "B"    
elif (puntaje >= 70):
    comparacion = "C"
elif (puntaje >= 60):
    comparacion = "D"        
else:
    comparacion="F"
print('Calificacion: ', comparacion, 'por ', puntaje, ' puntos') 