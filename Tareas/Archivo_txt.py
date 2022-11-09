'''
                     29 de agosto de 2022
                      Archivos de texto
'''

#Ejemplo de iterar un archivo con escritura y lectura
'''
‘r’: Por defecto, para leer el fichero.
‘w’: Para escribir en el fichero.
‘x’: Para la creación, fallando si ya existe.
‘a’: Para añadir contenido a un fichero existente.
‘b’: Para abrir en modo binario.
'''

#crear un archivo
def crearArchivo():
     archivo=open("ejemplo.txt","w")
     archivo.close()


print("Archivo creado...")
#input()

#escribir
def escribir():
     archivo=open("ejemplo.txt","a")
     cad=input("Ingrese texto: ")
     archivo.write(cad+"\n")
     archivo.close()

#leer
def leer():
     archivo=open("ejemplo.txt","r")
     linea=archivo.readline()
     while(linea):
          print(linea)
          linea=(archivo.readline()) #primer linea del archivo
     archivo.close()


#Ejercicio leer un archivo y obtener suma y promedio
def leerNum():
     archivo=open("numero.txt","r")
     suma=0
     prom=0
     linea=archivo.readline()
     while(linea):
          suma=suma+int(linea)
          linea=archivo.readline()
          prom=prom+1
     print("La suma es: ",suma)
     prom=suma/prom
     print("El promedio es: ", prom)
     archivo.close()


#Escribir en archivo una frase y contar las vocales y mostrar la cantidad

def escVocales():
     cad=input("Ingrese la frase a ingresar: ").upper()
     archivo=open("Vocales.txt","w")
     archivo.write(cad+"\n")
     a=0
     e=0
     i=0
     oo=0
     u=0
     for letra in cad:
          if letra=="A":
               a=a+1
          elif letra=="E":
               e=e+1
          elif letra=='I':
               i = i + 1
          elif letra == "O":
               oo = oo + 1
          elif letra == "U":
                u = u+  1
     archivo.write("A = "+str(a)+"\n")
     archivo.write("E = " + str(e) + "\n")
     archivo.write("I = " + str(i) + "\n")
     archivo.write("O = " + str(oo) + "\n")
     archivo.write("U = " + str(u) + "\n")
     archivo.close()
escVocales()





leerNum()

