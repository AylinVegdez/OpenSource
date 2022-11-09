'''
Tema: conjuntos
Fecha: 05 de septiembre del 2022
Autor: Leonardo Martínez González
'''

# 1. Definición. en Python es utilizado para trabajar con conjuntos de elementos.
#    La principal característica de este tipo de datos es que es una colección cuyos elementos
#    no guardan ningún orden y que además son únicos.
#    los principales usos de esta clase se usan para conocer si un elemento pertenece o no
#    a una colección y eliminar duplicados de un tipo secuencial (list, tuple o str).

# 2. Creación. Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {},
#    o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable
#    (como una lista, una tupla, una cadena …).

c1={1,2,3,4,5,1}
c2=set([i for i in range(0,20,4)])
c3=set()
print(c1)
print(c2)
print(c3)


#    Usando la función froezenset. es inmutable y su contenido no puede ser modificado
#    una vez que ha sido inicializado
c4=frozenset([chr(i) for i in range(65,91)])
print(c4)
#    Los elementos repetidos se eliminan


# 3. Para acceder a los elementos de un conjunto. Dado que los conjuntos son colecciones
#    desordenadas, en ellos no se guarda la posición en la que son insertados los elementos
#    como ocurre en los tipos list o tuple. Es por ello que no se puede acceder a los elementos
#    a través de un índice.



# 4. Añadir elementos: con el método add() ó con el método update()
#    Agregar el numero 8 al conjunto c

c1.add(9)
c1.add(8)
print(c1)

#    Agregar varios elementos al conjunto
c1.update({20,30,40,45,50,60})
print(c1)
c1.update([90,89,78])
print(c1)
c1.add((11,12,13,14,15))
print(c1)


# 5. Eliminar elementos del conjunto: discard(elemento), remove(elemento), pop() y clear()
#    discard(elemento) y remove(elemento) son muy parecidos, solo que remove lanza una excepcion KeyError
#    en caso de no existir el elemento

print(c1)
c1.discard(50)
c1.discard(100)
print(c1)

#c1.remove(100)

#     pop() devuelve un elemento aleatorio y lo elimina, si el conjunto esta vacio lanza una
#     excepcion KeyError.

c1.pop()
c1.pop()
c1.pop()
print(c1)

#    El método clear() elimina todos los elementos del conjunto
#c1.clear()
print(c1)

#    Número de elementos en un conlunto con la función len()
print("Cantidad de Elementos de conjunto 1:", len(c1))

#    Verificar si un elemento esta dentro de un conjunto

print(20 in c1)
print(67 in c1)


# ************************ Operaciones con conjuntos
# 1. Union  ( | )
#a=([i for i in range(0,21,2)])
#b=([i for i in range(1,22,2)])
#print( a|b )
# 2. Intersección ( & )
#b.add(2,4,6,8,10)
#print( a & b)

# 3. Diferencia ( - )
#print(a)
#print(b)
#print( a - b )

# 4. Diferencia simétrica ( ^ ). es el conjunto que contiene los elementos de A y B
#    que no son comunes.
#print(a ^ b )

# 5. Inclusión de conjuntos.  Se utiliza el operador <= para comprobar si un conjunto A
#    es subconjunto de B y el operador >= para comprobar si un conjunto A es superconjunto de B.
#s1={1,2,3,4,5}
#s2={1,2,3,4,5,6,7}
#print(s1 <=s2)

# 5. Conjuntos disjuntos. Dos conjuntos A y B son disjuntos si no tienen elementos en común,
#    es decir, la intersección de A y B es el conjunto vacío.


# 6. Igualdad de conjuntos. En Python dos conjuntos son iguales si y solo si todos los elementos
#    de un conjunto están contenidos en el otro. Esto quiere decir que cada uno es un subconjunto
#    del otro.


'''
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes.
2. Crear un método que regrese un conjunto de tuplas de materias.
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"",
                "Promedio":
            },
            {
                "Nombre":"",
                "Promedio":
            },
            . . . 
        ],
        "Promedio general": 
   }


'''
archivo=open("Estudiantes.prn","r")
archivo2=open("Kardex.txt",'r')
Ctuplas=set()
Mtuplas=set()
def Tuplas(archivo):
    for linea in archivo:
        num=linea[0:8]
        nom=linea[8:-1]
        tuplaAlu=(num,nom)
        Ctuplas.add(tuplaAlu)
    return Ctuplas
Tuplas(archivo)


def materias(archivo2):

    for linea in archivo2:
        listaMateria = linea.split('|')
        tuplaCal=(listaMateria[0],listaMateria[1],listaMateria[2].strip("\n"))
        Mtuplas.add(tuplaCal)
    return Mtuplas

def infoAlumno(ctrl,cAlumnos,cMaterias):

    MLista=list[cMaterias]
    Alista = list[cAlumnos]
    DicAux={}
    for i in cMaterias:
        if ctrl in MLista:
            print("Encontrado")
            #DicAux['Nombre']=MLista[1]
            #DicAux['Promedio']=MLista[2]

materias(archivo2)
infoAlumno('18420493',Ctuplas,Mtuplas)








