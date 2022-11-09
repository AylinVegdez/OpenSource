'''
                    Ciclos
            26 de agosto de 2022
'''
#For variable in, range(valor_inicial, valor_final, desplazamiento)
#While

#2. Imprimir numeros del 1 al 100
'''for x in range(1,100,2):
    print(x)
'''

#2. Imprimir numeros divisibles entre 3 al 500 al 1000
for x in range(500,1001):
    if x%3==0:
        print(x)
#3. Imprimir los numeros del 100 al 1
for x in range(101,0,-1):
    print(x)

# CICLO WHILE
'''
num=10
while num > 0:
    print(num)
    num -=1
'''
#4. Pedir numeros hasta que el usuario digite un cero

numero=1
while numero!=0:
     numero = int(input("Numero:"))
     print("Ingreso:")

#5. Pedir numeros de teclado  con break
while True:
    num=int(input("Dame un numero: "))
    if num==0:
        break
    print(num)