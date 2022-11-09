'''
Tema: Aplicación Conocimiento Unidad 2
Fecha: 03 de Octubre del 2022
Autor: Eileen Gizelle Vega Hernández
'''
import json
from numbers import Real

estudiantes=open("Estudiantes.prn", "r")
kardex=open("Kardex.txt",'r')


def ObtenerNombre(num_ctrol):
    archivo=open("Estudiantes.prn",'r')
    datafile = archivo.readlines()
    nom=""
    for linea in datafile:
        if num_ctrol in linea:
            nom=linea[8:-1]
    return nom

#devuelve conjunto: ctrl, nombre
def Tuplas(estudiantes):
    Ctuplas = set()
    for linea in estudiantes:
        num=linea[0:8]
        tuplaAlu=(num)
        Ctuplas.add(tuplaAlu)
    return Ctuplas

#retorna materias y promedio: ctrl, materia,promedio
def materias():
    Mtuplas = set()
    kardex = open("Kardex.txt", 'r')
    for linea in kardex:
        listaMateria = linea.split('|')
        tuplaCal=(listaMateria[0],listaMateria[1],listaMateria[2].strip("\n"))
        Mtuplas.add(tuplaCal)
    return Mtuplas

#Retorna lista de materias por numero de control
def RetMaterias(ctrol):
    promedios=materias()
    lista_materias=[]
    for mat in promedios:
        c,m,p=mat   #desestructurar la variable mat
        if ctrol==c:
            lista_materias.append(m)
    return lista_materias


def MetodoExamen(*args):
    Dic={}
    ListaF=[]
    if len(args)!=0:
        lista=args[0]
        try:
            estudiantes = open("Estudiantes.prn", "r")
            kardex = open("Kardex.txt", 'r')
        except FileNotFoundError:
            print('¡El fichero no existe!')
        else:
            for e in lista:
                try:
                    nom=ObtenerNombre(e)
                except Exception:
                    print("Ocurrio un error en la busqueda")
                else:
                    Dic["Nombre"]=ObtenerNombre(e)
                    Dic["Materias"]=RetMaterias(e)
                print(json.dumps(Dic, indent=4))
                ListaF.append(Dic)
                Dic = {}
    else:
        try:
            estudiantes = open("Estudiantes.prn", "r")
            kardex = open("Kardex.txt", 'r')
            lista = Tuplas(estudiantes)
        except FileNotFoundError:
            print('¡El fichero no existe!')
        else:
            for e in lista:
                try:
                    nom = ObtenerNombre(e)
                except Exception:
                    print("Ocurrio un error en la busqueda")
                else:
                    Dic["Nombre"] = ObtenerNombre(e)
                    Dic["Materias"] = RetMaterias(e)
                print(json.dumps(Dic, indent=4))
                ListaF.append(Dic)
                Dic = {}
    with open("ResultadoExamen.json", 'w') as file:
        json.dump(ListaF, file, indent=4)  # dump es disparar

num=['18420478']
MetodoExamen()
MetodoExamen(num)
num.append('18420478')
MetodoExamen(num)
num.append('18420430')
num.append('18420427')
MetodoExamen(num)
