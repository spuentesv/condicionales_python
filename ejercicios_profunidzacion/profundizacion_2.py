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
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

# Ingreso de numeros
texto1 = input('Ingrese el primer número  (ej. 1, 4):\n')
texto2 = input('Ingrese el segundo número (ej. 1, 4):\n')
texto3 = input('Ingrese el tercero número (ej. 1, 4):\n')
numero_1 = int(texto1)
numero_2 = int(texto2)
numero_3 = int(texto3)

# Calculo si numero es par - numero 1
comparacion = ""
resultado = numero_1 % 2
if (resultado == 0):
    comparacion = "PAR"
else:
    comparacion="IMPAR"

# Imprima en pantalla según corresponda
print('Numero 1:', numero_1, ' es ', comparacion) 

# Calculo si numero es par - numero 2
comparacion = ""
resultado = numero_2 % 2
if (resultado == 0):
    comparacion = "PAR"
else:
    comparacion="IMPAR"

# Imprima en pantalla según corresponda
print('Numero 2:', numero_2, ' es ',  comparacion) 

# Calculo si numero es par - numero 3
comparacion = ""
resultado = numero_3 % 2
if (resultado == 0):
    comparacion = "PAR"
else:
    comparacion="IMPAR"

# Imprima en pantalla según corresponda
print('Numero 3:', numero_3, ' es ',  comparacion) 


print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio