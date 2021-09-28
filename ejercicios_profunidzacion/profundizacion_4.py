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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

# define list de temperaturas
wrdlst = []
lenlst = []

# Ingreso de numeros
texto1 = input('Ingrese palabra 1\n')
texto2 = input('Ingrese palabra 2\n')
texto3 = input('Ingrese palabra 3\n')

# adiciona temperaturas ingresadas a list
wrdlst.append(texto1)
wrdlst.append(texto2)
wrdlst.append(texto3)

lenlst.append(len(texto1))
lenlst.append(len(texto2))
lenlst.append(len(texto3))

# Selecciona tipo de orden
print('1 - Ordenar por orden alfabético (usando el operador ">")')
print('2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")')
orden = int(input('Ingrese tipo de orden \n'))

# Imprima en pantalla según corresponda
if (orden == 1):
    print('lista Ordena Alfabeticamente ', wrdlst, sorted(wrdlst, reverse=True)) 
elif (orden == 2):    
    print('lista Ordena por longitud ', lenlst, sorted(lenlst, reverse=True))
else:    
    print('lista Ordena Alfabeticamente ', wrdlst, sorted(wrdlst, reverse=True)) 

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
