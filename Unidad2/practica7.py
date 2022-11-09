'''
Tema: Aplicación de estructuras de Python: archivos, JSON, cifrado de contraseñas
Fecha: 06 de septiembre del 2022
Autor: Leonardo Martínez González
Continuación de la práctica 6
'''
import codecs
import json
import os
from random import random
import random
import bcrypt

'''
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes. (5) 10 min.
2. Crear un método que regrese un conjunto de tuplas de materias.
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"Base de Datos",
                "Promedio":85
            },
            {
                "Nombre":"Inteligencia Artificial",
                "Promedio":100
            },
            . . . 
        ],
        "Promedio general": 98.4
   }
   
4. Regresar una lista de JSON con las materias de un estudiante, el formato es el siguiente:
[
    {"Nombre": "Contabilidad Financiera"},
    {"Nombre": "Dise\u00f1o UX y UI"}, 
    {"Nombre": "Base de datos distribuidas"}, 
    {"Nombre": "Finanzas internacionales IV"}, 
    {"Nombre": "Analisis y dise\u00f1o de sistemas de informacion"}, 
    {"Nombre": "Microservicios"},
    {"Nombre": "Algoritmos inteligentes"}
]

'''

#4.- Lista de materias
import json
archivo=open("Estudiantes.prn","r")
archivo2=open("Kardex.txt",'r')
archivo3=open("usuarios.txt",'r')
Ctuplas=set()
Mtuplas=set()

#devuelve conjunto: ctrl, nombre
def Tuplas(archivo):
    for linea in archivo:
        num=linea[0:8]
        nom=linea[8:-1]
        tuplaAlu=(num,nom)
        Ctuplas.add(tuplaAlu)
    return Ctuplas


#retorna materias y promedio: ctrl, materia,promedio
def materias(archivo2):
    for linea in archivo2:
        listaMateria = linea.split('|')
        tuplaCal=(listaMateria[0],listaMateria[1],listaMateria[2].strip("\n"))
        Mtuplas.add(tuplaCal)
    return Mtuplas

#Retorna lista de materias por numero de control
def RetMaterias(ctrol):
    promedios=materias(archivo2)
    lista_materias=[]
    for mat in promedios:
        c,m,p=mat   #desestructurar la variable mat
        if ctrol==c:
            lista_materias.append({"Nombre":m})
    return json.dumps(lista_materias)

#print(RetMaterias('18420473'))

'''
5. Generar un archivo de usuarios que contenga el numero de control, éste será el usuario
   y se generará una contraseña de tamaño 10 la cual debe tener:
   A. Al menos una letra mayúscula 
   B. Al menos una letra minúscula
   C. Numeros
   D. Al menos UN carácter especial, considere ( @, #, $,%,&,_,?,! )

   Considere:
    - Crear un método para generar cada caracter
    - El codigo ascii: https://elcodigoascii.com.ar/
    - Encriptar la contraseña con bcrypt, se utiliza con node.js, react, etc. Para ello:
        * Descargue la libreria bcrypt con el comando: "pip install bcrypt" desde la terminal o desde PyCharm
        * Página: https://pypi.org/project/bcrypt/
        * Video:Como Cifrar Contraseñas en Python     https://www.youtube.com/watch?v=9tEovDYSPK4

   El formato del archivo usuarios.txt será:
   control contrasena contraseña_cifrada
'''
#Ejercicio 5

def Mayuscula():
    return chr(random.randint(65,90))

def Minuscula():
    return chr(random.randint(97,122))

def Numero():
    return chr(random.randint(48,57))

def Caracter():
    lista_c=['@','#','$','%','&','_','¿','¡']
    return lista_c[random.randint(0,7)]

def Password():
    password=""
    for i in range(0,10):
        num=random.randint(1,5)
        if num==1:
            password=password+Mayuscula()
        elif num==2:
            password = password + Minuscula()
        elif num==3:
            password = password + Caracter()
        elif num>=4 and num<=5:
            password = password + Numero()
    return  password

#cifrar contraseñas con bcryp
def Cifrado(contra): #convertir a bytes par apoder cifrar
    sal=bcrypt.gensalt()    #Default tiene 12
    passwordC=bcrypt.hashpw(contra.encode(),sal)
    return (passwordC)

#clave=Password()
#print("Contraseña generada:",clave+" \t----- \tCifrado:",Cifrado(Password()))


#generar archivo usuarios
def TxtPass():
    listaE=list(Tuplas(archivo))
    archivo3 = open("usuarios.txt", 'w')
    for linea in listaE:
        c,n=linea
        clave=Password()
        archivo3.write(c+" "+clave+" "+(str(Cifrado(clave),'UTF-8')+"\n"))
    print("Archivo Generado")

#print(bcrypt.checkpw("0&W03¿400G".encode('utf-8'),"$2b$12$R/C5TMpr7DwQA81.oIraMeAUwA9cjsHlhK43VcCOmucX08VYrWjHS".encode('utf-8')))
#TxtPass()

'''
6. Crear un método "autenticar_usuario(usuario,contrasena)" que regrese una bandera que 
   indica si se pudo AUTENTICAR, el nombre del estudiante y un mensaje, regresar el JSON:
   {
        "Bandera": True,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
   }
     ó

   {
        "Bandera": False,
        "Usuario": "",
        "Mensaje": "No existe el Usuario"
   }

   ó

    {
        "Bandera": False,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Contraseña incorrecta"
   }


'''
def ObtenerNombre(num_ctrol):
    archivo=open("Estudiantes.prn",'r')
    datafile = archivo.readlines()
    for linea in datafile:
        if num_ctrol in linea:
            nom=linea[8:-1]
    return nom


def Autentificar(usuario,password):
    Bandera=bool
    nom=""
    msj=""
    Dic = {}
    print("\t\t   Validando...\n")
    for linea in archivo3:
        if usuario in linea:
            Bandera=True
            lista= linea.split(' ')
            en=lista[2].strip('\n')
            if bcrypt.checkpw(password.encode('utf-8'), en.encode('utf-8')):
                Bandera = True
                msj = "Bienvenido al Sistema de Autenticacion de usuarios"
                # obtener nombre
                nom = ObtenerNombre(usuario)
            else:
                msj = "Password Inconrrecto"
                Bandera = False
                nom = ObtenerNombre(usuario)
            break
        else:
            Bandera = False
            msj = "No exite usuario"
    Dic["Bandera"]=Bandera
    Dic["Nombre"]=nom
    Dic["Mensaja"]=msj
    return print(json.dumps(Dic, indent=4)+"\n\n\t  Proceso terminado")

print("\t------ Practica 7 ------")
usuario=input("Ingrese su usuario(num Ctrol):")
contrasena=input("Ingrese la contraseña:")
Autentificar(usuario,contrasena)
#Autentificar('18420469','@6%H6Hm394') usuario correcto
#Autentificar('18420000','@6%H6Hm394') no existe usuario
#Autentificar('18420469','16%H6Hm394') contraseña no valida
 

