'''
# Tema: Tuplas
# Fecha: 31 de agosto del 2022
# Autor: Leonardo Martínez González
'''
# 1. Definición. Es una colección de elementos inmutables.
#             Las tuplas son immutables y normalmente contienen una secuencia heterogénea
#             de elementos que son accedidos al desempaquetar o indizar.

# 2. Crear tuplas
tupla1=tuple()
tupla2=()
tupla3=(1,2,"Hola",'x')
# 3. Accesar a elementos de la tupla, igual que en las listas
print(tupla3[2])

for elem in tupla3:
    print(elem)
# 4. Operaciones.
# 4.A. Son inmutables

#tupla3[1]="Otra cadena"

# 4.B. Las tuplas pueden ser anidadas

grupoA=('Jose','Paola','Marco')
grupoB=('Karla', 'Pablo')
grupoC=(grupoA,grupoB)
print(grupoC)
numeros=((3,4),(4,7),(100,8))
print(numeros)

# 4.C. Las listas se pueden convertir en tuplas  haciendo uso de la función tuple()

lista=['A','B','C','D','E']
tuplaLetras=tuple(lista)
print(tuplaLetras)

# 4.D. Se puede asignar el valor de una tupla con n elementos a n variables

tuplaAlumno=(420101,'Gizelle Vega')
control,nombre=tuplaAlumno
print("Control: ",control,"Nombre: ",nombre)

# 5. Métodos de tuplas
#count retorna el numero de elementos existentes en la tupla, se da argumento
print(tupla3.count(1))


# index() Regresa el índice donde se ha encontrado, tambien puede pasarle un segundo es a parti de donde buscara
#print(tuplaLetras("D",3))

'''
Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas
con la siguiente forma:
(nombre, clave, destino)
Ejemplo:
pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Gualupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Nulvy Martinez", 202106, "León"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora"),
               ]

Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el estado al que pertencen.
Ejemplo:
ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("León","Guanajuato"),
           ]

Hacer un menú interactivo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de pasajeros
- Agregar ciudades a la lista de ciudades
- Dada la CLAVE de un pasajero, ver a que ciudad viaja
- Dada la CIUDAD, mostrar la cantidad de pasajeros que viajan a esa ciudad
- Dada la CLAVE de un pasajero, ver a que ESTADO viaja
- Dado un Estado, mostrar cuantos pasajeros viajan a ese Estado
- Salir del programa

NOTA: Haga uso de funciones
'''
from FuncionesPrac4 import *
pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Gualupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Nulvy Martinez", 202106, "León"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora"),
               ]
ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("León","Guanajuato"),
           ]

def MenuP():
    while True:
        print("\n"+"////////////////////////////////")
        print("1.- Agregar Pasajero")
        print("2.- Agregar Cuidad")
        print("3.- Consultar cuidad de destino")
        print("4.- Cantidad de pasajeros por destino")
        print("5.- Consultar estado destino")
        print("6.- Cantidad de pasajeros por estado")
        print("7.- Cantidad de pasajeros viajando")
        print("8.- Salir")
        print("////////////////////////////////"+"\n" )

        op=int(input("Ingrese la opcion: "))

        #Evaluar
        if op==1:
            print("\n"+"--- Agregar Pasajero ---")
            AgregarP(pasajeros)
            print(pasajeros)
        elif op==2:
            print("\n"+"--- Agregar Cuidad ---")
            AgregarC(ciudades)
            print(ciudades)
        elif op==3:
            print("\n" + "--- Mostrar destino ---")
            clave=int(input("Ingrese la clave del pasajero:"))
            ciudad=BuscarCuidad(clave,pasajeros)
            print("El pasajero ", clave, "viaja a la ciudad de ",ciudad)
        elif op==4:
            print("\n" + "--- Cantidad de pasajeros por destino ---")
            conteo=conteoD(pasajeros)
            print(conteo)
        elif op==5:
            print("\n" + "--- Consultar estado destino ---")
            clave = int(input("Ingrese la clave del pasajero:"))
            ciudad = BuscarCuidad(clave, pasajeros)
            estado= BuscarEstado(ciudad,ciudades)
            print("El pasajero ", clave, "viaja al estado de ", estado)
        elif op==6:
            print("\n" + "--- Cantidad de pasajeros por Estado---")
            estado=input("Ingrese el estado:")
            conteo = conteoE(estado,pasajeros,ciudades)
            print(conteo)
        elif op==7:
            print("\n" + "--- Cantidad de pasajeros por Cuidad ---")
            ciudad=input("Cuidad a buscar:")
            cantidad=contarXCiudad(ciudad,pasajeros)
            print("A la ciudad de "+ ciudad+" viajan "+str(cantidad)+" pasajeros")
        elif op==8:
            exit()
        else:
            print("Opcion no valida")

MenuP()
