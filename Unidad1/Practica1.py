
'''
                Tipos de Datos          Eileen Vega Hernández
              24 - Agosto -2022
'''

'''
Numericos
Texto
Booleano
'''

producto='Monitor Samsunm de 27 pulgadas'
precio=4599.0
oferta=True
descuento=10 #%
precio_oferta=precio-(precio*descuento/100)


'''
Condicionales

1.- if
2.- if-else
3.- if anidado
'''

if(oferta==True):
    precio_oferta =precio-(precio*descuento/100)
    print("Producto en oferta")
else:
    precio_oferta=precio
    print("Producto sin oferta")

print("Producto: "+ producto + "Precio: ", precio, " Oferta: "+str(oferta)+ " Precio Oferta: " + str(precio_oferta))

numero=5;
# Dado un numero , mostrar el dia de la semana
if(numero==1):
    print("Lunes")
else:
    if(numero==2):
        print("Martes")
    else:
        if (numero == 3):
            print("Miercoles")
        else:
            if (numero == 4):
                print("Jueves")
            else:
                if (numero == 5):
                    print("Viernes")
                else:
                    if (numero == 6):
                        print("Sabado")
                    else:
                        if (numero == 7):
                            print("Domingo")

