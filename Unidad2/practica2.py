# Tema: Listas
# Fecha: 29 de agosto del 2022
# Autor: Carlos Israel Bautista Mejía
# Referencia: https://docs.python.org/es/3/tutorial/datastructures.html

# Estructura en Python que son actualizables.

# 1. Crear Listas
# nombre_lista = []
# otra_lista = list()

# 2. Accesar a elementos de una lista
# nombre_lista[posición]
# lista = ['Juan', 'Pedro', 'Carmen', 'Lucia', 'José']
# print(lista[1])
#
# for x in range(5):
#     print(lista[x])
#
# print(lista)
#
# print("Longitud de la lista: " + str(len(lista)) + "\n")

# 3. Longitud de una lista, utilice el método len()
# print( len(nombre_lista) )

# 4. Debanado (una parte ó rebanadas de listas)
#lista = [10,20,3.14,'Walter', 'Coto', 7, 'Estudiante', 'Cuaderno']

# Imprimir el elemento de la posición 5
# print(lista[5])

# Imprimir los cuatro primeros elementos de la lista
# print(lista[0:5])
# print(lista[0:2])



# Imprimir los dos primeros elementos, si no colocamos el primero Python entiende que
# desea procesar desde el primer elemento y de igual forma con el último
# print(lista[ : 2])
# print(lista[2: ])
# print(lista[ : 2])
# print(lista[2 : 4])

# Imprimir el último elemento, debanado negativo
# print(lista[-1])
# Cuando es así el número menor se coloca a la izquierda y el mayor a la derecha
# print(lista[-5 : -2 ]) # Recuerda que no se incluye el límite superior
# print(lista[-1])
# lista = ['Juan', 'Pedro', 'Carmen', 'Lucia', 'José']
# print(lista[-5:-3])  # listas[inicio:fin]

# Algunos métodos de listas
# lista_dos = [1, 2, 3, 4, 5]
# print(lista_dos)

# 1. Agregar elemento nombre_lista.append(elemento)
# lista_dos.append(6)
# print(lista_dos)

# 2. Agregar elemento en una posición dada nombre_lista.insert(i,elemento)
# lista_dos.insert(1,7)
# print(lista_dos)
# lista.insert(1,'Navarrete')
# print(lista)

# 3. Eliminar el primer elemento que encuentra en la lista, manda un ValueError si no existe.
#    nombre_lista.remove(elemento)
# lista_dos.remove(10)
# print(lista_dos)
# lista.remove('Navarrete')
# print(lista)

# 4. Quitar el últipo elemento de la lista, opcional se le puede pasar la posición del elemento
#    Si no existe la posición manda un error IndexError (fuera de rango) nombre_lista.pop([posicion])
# lista_dos.pop(10)
# print(lista_dos)
# lista_dos.pop(0) # Quita el primer elemento
# print(lista_dos)
# lista_dos.pop() # Quita el último elemento
# print(lista_dos)
# lista.pop()
# print(lista)


# 5. Regresar el indice del primer elemento encontrado, si no existe lanza una excepción ValueError
# print(lista_dos.index(3))
# print(lista.index('Carmen'))


# 6. Regresar el numero de veces que elemento aparece en la lista. nombre_lista.count(elemento)
# lista.insert(3,'Carmen')
# print(lista)
# print(lista.count('Carmen'))

# 7. Invierte los elementos de la lista. nombre_lista.reverse()
# lista_dos.reverse()
# print(lista_dos)
# lista.reverse()
# print(lista)


# 8. Listas por comprensión
# A. Generar una lista con los primeros 5 numeros
# lista = [i for i in range(5)]
# print(lista)

# B. Generar una lista con numeros aleatorios del 1 al 100
#    Referencia numeros aleatorios: https://j2logo.com/python/generar-numeros-aleatorios-en-python/
# import random
# lista = [random.randint(1,100) for i in range(10)]
# print(lista)

