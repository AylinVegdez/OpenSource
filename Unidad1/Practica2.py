'''
            26 de Agosto del 2022
            Eileen Gizelle Vega Hernandez
'''
'''
1.- IF
2.- IF-ELSE
3.- IF-ELSE ANIDADO
'''

#1. Pedir un numero del teclado y mostrar el valor absoluto
numero = int(input("Ingresa un numero: "))
if numero < 0:
    numero=numero*-1
print("Valor abosluto:  ", numero)

#2. Pedir 2 nombres, si la primera letra coincide a la ultima , entonces hay coincidencia
nombre1=input("Dame el primer nombre_")
nombre2=input("Dame el segundo nombre_")
pos=len(nombre1)-1
pos2=len(nombre2)-1

if nombre1[0]==nombre2[0] or nombre1[pos]==nombre2[pos2]: #nombre[-1]== ultima posicion
    print("Coincidencia")
else:
    print("No hay coincidencia")


#Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son
#A partido rojo
#B partido verde
#C partido azul
#Segun sea ABC se deberan imprimir el mensaje"Usted ha votado por el canditado que corresponde"
'''
print("A... Partido Rojo")
print("B... Partido Verde")
print("C... Partido Azul")
voto=input("Ingrese su voto:").upper()

if voto=='A':
     print("Usted ha votado por el canditado del partido ROJO")
 elif voto == 'B':
     print("Usted ha votado por el canditado del partido VERDE")
    elif voto == 'C':
        print("Usted ha votado por el canditado del partido AZUL")
    else:
        print("No existe, error")
'''

#Pedir una letra y si es vocal, mostrar que es vocal, validar que sea solo una letra
letra=input("Dame una letra").upper()
if len(letra)==1:
    if letra in "AEIOU":
        print("La letra es una vocal")
else:
    print("Ingrese un solo caracter")





