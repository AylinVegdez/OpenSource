'''
            29 agosto de 2022
            Listas anidadas
'''

alumnos=['Andrea','Carlos','Julian']
promedios=[]
print(alumnos)
#for alumnos in alumnos:
  #  promedios.append(alumnos[-1])
#print(promedios)
print(alumnos)

#lista por comprension
#promedios2 =[ alumnos[-1] for alumnos in alumnos]
#print(promedios2)

#Lista de estudiantes
#1. menu principal: insertar eliminar, actualizar, imprimir, salir, no valida
#2.no sale del menu

def insertar(nombre):
    alumnos.append(nombre)

def eliminar(nombre):
    alumnos.remove(nombre)

def actualizar(nombre):
    pos=alumnos.index(nombre)
    alumnos.remove(nombre)
    nombre=input("Ingrese el nuevo nombre:")
    alumnos.insert(pos,nombre)

def mostrar():
    print(alumnos)

def mostrarMenu():
    print("1.-Insertar")
    print("2.-Eliminar")
    print("3.-Actualizar")
    print("4.-Imprimir")
    print("5.- Salir")
    op = int(input("Ingrese la opcion deseada:"))
    menu(op)

def menu(op):
    if op==1:
        nombre =input("Ingrese el nombre:")
        insertar()
        mostrarMenu()
    elif op==2:
        nombre = input("Ingrese el nombre a eliminar:")
        eliminar(nombre)
        mostrarMenu()
    elif op==3:
        nombre = input("Ingrese el nombre a actualizar:")
        actualizar(nombre)
        mostrarMenu()
    elif op==4:
        mostrar()
        mostrarMenu()
    elif op==5:
        exit()
    else:
        print("Opcion no valida")
        mostrarMenu()

mostrarMenu()





