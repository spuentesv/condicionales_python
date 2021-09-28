# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
comparacion = ""
if (texto_1 > texto_2):
    comparacion = "MAYOR"
elif (texto_1 < texto_2):
    comparacion = "MENOR"    
else:
    comparacion="IGUAL"
# Imprima en pantalla según corresponda
print('Comparacion entre texto1: ', texto_1, ' y ', 'texto2: ', texto_2, ' indica que es ', comparacion) 

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
Len1 = len(texto_1)
Len2 = len(texto_2)
comparacion = ""
if (Len1 > Len2):
    comparacion = "MAYOR"
elif (Len1 < Len2):
    comparacion = "MENOR"    
else:
    comparacion="IGUAL"
# Imprima en pantalla según corresponda
print('texto1 tiene una longitud de ', str(Len1), ' y ', 'texto_2 tiene una longitud de ', str(Len2), ' indica que son ', comparacion) 

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
comparacion = ""
if (texto_1[0] > texto_2[0]):
    comparacion = "MAYOR"
elif (texto_1[0] < texto_2[0]):
    comparacion = "MENOR"    
else:
    comparacion="IGUAL"
# Imprima en pantalla según corresponda
print('Primera letra de texto1 ', texto_1[0], ' y ', 'Primera letra de texto_2', texto_2[0] , ' indica que son ', comparacion) 

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
comparacion = ""
if (copia_texto_1 == texto_1):
    comparacion = "IGUAL"
else:
    comparacion="DISTINTA"
# Imprima en pantalla según corresponda
print('copia de texto1 ', copia_texto_1, ' y ', 'texto_1', texto_1 , ' son ', comparacion) 

# Verifique que copia_texto_1 es distinta a texto_2
comparacion = ""
if (copia_texto_1 == texto_2):
    comparacion = "IGUAL"
else:
    comparacion="DISTINTA"
# Imprima en pantalla según corresponda
print('copia de texto1 ', copia_texto_1, ' y ', 'texto_2', texto_1 , ' son ', comparacion) 