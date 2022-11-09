'''
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

'''
Nombre:Eileen Gizelle Vega Hernández
Tema: Práctica 6 Conjuntos, Archivos y JSON
05 -Sep -2022
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

def materias(archivo2):

    for linea in archivo2:
        listaMateria = linea.split('|')
        tuplaCal=(listaMateria[0],listaMateria[1],listaMateria[2].strip("\n"))
        Mtuplas.add(tuplaCal)
    return Mtuplas

def infoAlumno(ctrl,cAlumnos,cMaterias):
    MLista=list(cMaterias)
    Alista = list(cAlumnos)
    ListaD=[]
    Diccionario={}
    prom=0
    c=0
    for i in MLista:
        if i[0]==ctrl:
            DicAux = {}
            DicAux['Nombre']=i[1]
            DicAux['Promedio']=i[2]
            ListaD.append(DicAux)
            prom=prom+int(i[2])
            c=c+1
    for j in Alista:
        if j[0] == ctrl:
            Diccionario['Nombre'] = j[1]
    Diccionario['Materias'] = ListaD
    Diccionario['Promedio General'] =prom/c
    print(Diccionario)
    return Diccionario

import json #libreria que maneja este formato
ctrl=input("Ingrese el numero de control:")
with open("Estudiante.json", 'w') as file:
        json.dump(infoAlumno(ctrl,Tuplas(archivo),materias(archivo2)), file, indent=4) # dump es disparar


