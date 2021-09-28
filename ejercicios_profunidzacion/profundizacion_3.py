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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

# define list de temperaturas
temlst = []
# Ingreso de numeros
texto1 = input('Ingrese temperatura 1 (ej. 10.5, 30):\n')
texto2 = input('Ingrese temperatura 2 (ej. 10.5, 30):\n')
texto3 = input('Ingrese temperatura 3 (ej. 10.5, 30):\n')

# adiciona temperaturas ingresadas a list
temlst.append(float(texto1))
temlst.append(float(texto2))
temlst.append(float(texto3))

# Determina que temperatura es Maxima, minima y promedio
maxima = max(temlst)
minima = min(temlst)
promedio = sum(temlst)/len(temlst)

# Imprima en pantalla según corresponda
print('Temperatura Maxima:', maxima, ' Temperatura Minima:',  minima, ' Temperatura Promedio:', round(promedio,2)) 

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
