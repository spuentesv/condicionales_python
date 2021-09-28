# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
comparacion = ""
if (texto_1 > texto_2):
    comparacion = "MAYOR"
elif (texto_1 < texto_2):
    comparacion = "MENOR"    
else:
    comparacion="IGUAL"
# Imprima en pantalla según corresponda
print('Comparacion entre texto1: ', texto_1, ' y ', 'texto2: ', texto_2, ' indica que es ', comparacion) 

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
comparacion = ""
if (int(texto_1) >int(texto_2)):
    comparacion = "MAYOR"
elif (int(texto_1) < int(texto_2)):
    comparacion = "MENOR"    
else:
    comparacion="IGUAL"
# Imprima en pantalla según corresponda
print('Comparacion entre texto1: ', texto_1, ' y ', 'texto2: ', texto_2, ' indica que son ', comparacion) 

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
