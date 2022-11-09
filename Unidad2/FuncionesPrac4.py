#insertar pasajeros
def AgregarP(pasajeros):
    nom=input("Ingrese el nombre:")
    clave=int(input("Clave de pasajero:"))
    destino=input("Cuidad de destino:")
    pasajeros.append((nom,clave,destino))

#insertar destinos
def AgregarC(ciudades):
    ciudad=input("Ingrese el nombre de la cuidad:")
    destino=input("Estado de destino:")
    ciudades .append((ciudad,destino))

#Busca clave y retorna ciudad
def BuscarCuidad(clave,pasajeros):
    for i in pasajeros:
        if i[1]==clave:
            return i[2]
    return "No existe un destino"

#Buscar estado por cuidad
def BuscarEstado(ciudad,ciudades):
    for c in ciudades:
        if c[0]==ciudad:
            return c[1]
    return "No hay estado"

#Contar las personas que van a un mismo destino
def conteoD(pasajeros):
    G=0
    Z=0
    L=0
    for i in pasajeros:
        if i[2]=="Zamora":
            Z=Z+1
        elif i[2]=="Guadalajara":
            G=G+1
        elif i[2]=="Leon":
            L=L+1
    return ("Zamora: "+ str(Z)+"\n"+"Guadalajara:"+str(G)+"\n"+"Leon:"+str(L))
#conteo por estados
def conteoE(estado,pasajeros,ciudades):
    c=0
    for i in ciudades:
        if
        if ciudades[1]==estado:
            c=c+1

#contar por cuidad
def contarXCiudad(ciudad,pasajeros):
    cont=0
    for p in pasajeros:
        if p[2]==ciudad:
            cont=cont+1
    return cont

