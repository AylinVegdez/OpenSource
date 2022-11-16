'''
Tema: Aplicación Conocimiento Unidad 3
Fecha: 16 de Nomviembre del 2022
Autor: Eileen Gizelle Vega Hernández
'''

from crudmysql import MySQL
from Variables import variablesMySQL
import json

def Consulta_Promedio():
    obj_MySQL = MySQL(variablesMySQL)
    print("==Consulta General de estudiantes ==")
    ctrl = input("Dame el numero de control: ")
    obj_consulta=f"select E.control,E.nombre, format(avg(K.calificacion),1) as promedio from estudiantes E, kardex K where E.control='{ctrl}';"
    est=obj_MySQL.consulta_sql(obj_consulta)
    print("N_Control        Nombre               Promedio")
    for e in est:
        print(e[0], e[1] ,e[2])
    print("\n\n")

def Consultar_Materias():
    obj_MySQL = MySQL(variablesMySQL)  # *********************************
    print(" == CONSULTAR MATERIAS POR ESTUDIANTE ==")
    ctrl = input("Dame el numero de control: ")
    sql_materias = "SELECT E.nombre, K.materia, K.calificacion " \
                   "FROM estudiantes E, kardex K " \
                   f"WHERE E.control = K.control and E.control='{ctrl}';"
    print(sql_materias)
    resp = obj_MySQL.consulta_sql(sql_materias)
    r={}
    lista=[]
    m={}
    if resp:
        r["Estudiante"] = resp[0][0]
        for mat in resp:
            m["Materia"] = mat[1]
            m["Calificacion"]=mat[2]
            lista.append(m)
        r["Materias"]=lista
        print(r)

    else:
        print(f"El estudiante con Número de control: {ctrl} NO existe")


def menu():
    while True:
        print("\n=======================EXAMEN U3 Y U6  =============================\n");
        print("1.Consultar Materia");
        print("2.Obtener el promedio general del estudiante");
        print("3. Salir");
        print("\n==============================================================\n");
        print("Dame la opcion que deseas");
        try:
            opcion = int(input(""));
        except Exception as error:
            print("Error: ",error);
            break
        if opcion==1:
            Consultar_Materias()
        if opcion==2:
            Consulta_Promedio()
        if opcion==3:
            break
    else:
         print("opcion no validad");

menu()