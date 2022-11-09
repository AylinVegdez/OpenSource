'''
Nombre:Eileen Gizelle Vega Hernández
Tema: Práctica 5_Diccionarios, Archivos y JSON
02 -Sep -2022
'''
print(" ----- Practica 5 ----- ")

#Inicializar variables
CP={}
datos=[]
archivo="CPdescarga.txt"
cad=""
cont=1

# Leer archivo linea a linea para filtrar con la palabra San Luis Potosí
#retornar una cadena con los resultados obtenidos

for linea in open(archivo,"r"):
        if 'San Luis Potosí' in linea:
                cad = cad + linea
listaSP=cad.split('\n')

#Separar por CP y agregar al diccionerio principal
for i in listaSP:
        try:
                info={}
                datos=i.split('|')
                if datos[4]=='San Luis Potosí': #Segundo filtro, para verificar el estado
                        info['CP']=datos[0]
                        info['Municipio']=datos[3]
                        info['Estado']=datos[4]
                        CP[datos[0]]=info
        except IndexError: #Control de index de recorrido for
                print()

print(CP)
print("\n-----------------------------\n")

import json
with open("resultado.json", 'w') as file:
        json.dump(CP, file,indent=4) # dump es disparar







