# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''
# Ingreso de numeros
texto1 = input('Ingrese el primer número  (ej. 1, 2.5):\n')
texto2 = input('Ingrese el segundo número (ej. 1, 2.5):\n')
numero_1 = float(texto1)
numero_2 = float(texto2)
numero_3 = numero_1 - numero_2

# Calculo de diferencia entre los 2 numeros
comparacion = ""
if (numero_3 > 0):
    comparacion = "POSITIVO"
elif (numero_3 < 0):
    comparacion = "NEGATIVO"    
else:
    comparacion="CERO"

# Imprima en pantalla según corresponda
print('Diferencia entre', numero_1, ' y ', numero_2, ' es ', numero_3, comparacion) 

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio