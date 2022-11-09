'''
                             Listas
                        26 de agosto de 2022
'''
'''
nombre_lista=[]
otra_lista=list()

#1, Imprimir lista
lista1 = [1,2,3,4,5,6,7]

for i in lista1:
    print(i)

lista2=['yo', 'tu','ese', 'aquel']
for i in lista2:
    print(i)

lista3=['a',1,True, 'b',2,False, 'c',3,True]
for i in lista3:
    print(i)

#Otras cosas de listas
print(lista3[0])
print(lista3[2])
print(lista3[-1])

#3. Otra forma de recorrer listas

# Como agregar elementos a lista
lista4=[]
for i in lista4:
    print(i)
lista4.appened(100)
lista4.appened(200)
lista4.appened(300)
'''
#Vamos a pedir 10 numeros por teclado
#Ordenar e imprimir

listan=[]
c=1
x=0
while c<10:
    listan.append(input("Ingresa un numero: "))
    c=c+1
listan.sort()
print(listan)