
from crudmysql import  MySQL
from Variables import variablesAWS, variablesMySQL
from variablesMongo import variablesMongo
from MongoDB import PyMongo
from Caja import Password

def cargar_estudiantes():
    obj_MySQL = MySQL(variablesAWS)
    obj_Mongo = PyMongo(variablesMongo)
    #cargar consultas
    sql_estudiantes="SELECT * FROM estudiantes;"
    sql_Kardex="SELECT * FROM kardex;"
    sql_usuarios="SELECT * FROM usuarios;"
    obj_MySQL.conectar_mysql()
    lista_estudiantes = obj_MySQL.consulta_sql(sql_estudiantes)
    lista_Kardex=obj_MySQL.consulta_sql(sql_Kardex)
    lista_usuarios=obj_MySQL.consulta_sql(sql_usuarios)
    obj_MySQL.desconectar_mysql() #obj_MySQL ya lleva los datos de las consultas

    #insercion en mongo
    obj_Mongo.conectar_mongodb()
    #for est in lista_estudiantes:
     #   e = {
      #      "control": est[0],
       #     "nombre": est[1]
       # }
        #print(e)
        #obj_Mongo.insertar('estudiantes', e)
        #insercion materias
    for mat in lista_Kardex:
        k={
            "idKardex":mat[0],
            "control": mat[1],
            "materia": mat[2],
            "calificacion":float(mat[3])
        }
        #print(k)
        obj_Mongo.insertar('kardex',k)

        #insercion a usuarios
    for usuario in lista_usuarios:
        u = {
            "idUsuario":usuario[0],
            "control": usuario[1],
            "clave": usuario[2],
            "clave_cifrada": usuario[3]
        }
        #print(u)
        obj_Mongo.insertar('usuarios', u)
    print("Inserciones Terminadas con Exito")
    obj_Mongo.desconectar_mongodb()

def insertar_Estudiante():
    obj_PyMongo=PyMongo(variablesMongo)
    print("== Insertar estudiante ==")
    ctrl =input("Dame el numero de control: ")
    nombre=input("Dame el nombre del estudiante: ")
    clave=input("Dame la clave de acceso: ")
    obj_usuario = Password(longitud=len(clave), contrasena=clave)
    json_estudiante={'control':ctrl,'nombre':nombre}
    json_usuarios={'idUsuario':100,'clave':clave,'clave_cifrada':obj_usuario.contrasena_sifrada.decode()}
    obj_PyMongo.conectar_mongodb()
    obj_PyMongo.insertar('estudiantes',json_estudiante)
    obj_PyMongo.insertar('usuarios',json_usuarios)
    obj_PyMongo.desconectar_mongodb()
    print("Datos insertados Correctamente")

def actualizar_calificacion():
    obj_PyMongo = PyMongo(variablesMongo)
    print("==== ACTUALIZAR PROMEDIO =====")
    ctrl = input("Ingresa el número de control: ")
    materia = input("Ingresa el nombre de la materia: ")
    filtro_buscar_materia = {'control': ctrl, 'materia': materia}
    obj_PyMongo.conectar_mongodb()
    respuesta = obj_PyMongo.consulta_mongodb('kardex', filtro_buscar_materia)
    for reg in respuesta:
        print(reg)
    if respuesta:
        promedio = float(input("Dame el nuevo promedio "))
        json_actualiza_prom = {"$set":{"calificacion": promedio}}
        resp=obj_PyMongo.actualizar('kardex', filtro_buscar_materia, json_actualiza_prom)
        if resp['status']:
            print("El promedio ha sido actualizado")
        else:
            print('Ocurrio un error al actualizar')
    else:
        print(f"El estudiante con numero de control {ctrl} o la materia {materia} NO EXISTE")
    obj_PyMongo.desconectar_mongodb()

def consultar_materias():
    obj_PyMongo = PyMongo(variablesMongo) # *********************************
    print(" == CONSULTAR MATERIAS POR ESTUDIANTE ==")
    ctrl = input("Dame el numero de control: ")
    filtro={ 'control':ctrl}
    atributos_estudiente={"_id":0,"nombre":1}
    atributos_kardex={"_id":0,"materia":1,"calificacion":1}
    #sql_materias = "SELECT E.nombre, K.materia, K.calificacion " \
                   #"FROM estudiantes E, kardex K " \
                   #f"WHERE E.control = K.control and E.control='{ctrl}';"
    obj_PyMongo.conectar_mongodb()
    respuesta1 = obj_PyMongo.consulta_mongodb('estudiantes',filtro,atributos_estudiente)
    respuesta2=obj_PyMongo.consulta_mongodb('kardex',filtro,atributos_kardex)
    obj_PyMongo.desconectar_mongodb()
    #print(f"respuesta1:",respuesta1)
    #print(f"respuesta2:", respuesta2)
    if respuesta1["status"] and respuesta2["status"]:
        print("Estudiantes: ",respuesta1["resultado"][0]["nombre"])
        for mat in respuesta2["resultado"]:
            print(mat["materia"],mat["calificacion"])

def consulta_general():
        obj_Pymongo = PyMongo(variablesMongo)
        obj_Pymongo.conectar_mongodb()
        print("==== CONSULTA GENERAL =====")
        respuesta = obj_Pymongo.consultar_mongodb("estudiantes")
        respuesta2 = obj_Pymongo.consultar_mongodb("kardex")
        obj_Pymongo.desconectar_mongodb()
        i = 0;
        if respuesta["status"] and respuesta2["status"]:
            for res1 in respuesta["resultado"]:
                j = 0
                prom = 0
                cont = 0
                for res2 in respuesta2["resultado"]:
                    if respuesta["resultado"][i]["control"] == respuesta2["resultado"][j]["control"]:
                        prom += respuesta2["resultado"][j]["calificacion"]
                        cont += 1
                    j += 1
                if (cont > 0):
                    prom = prom / cont
                print( respuesta["resultado"][i]["control"],")",
                      respuesta["resultado"][i]["nombre"], "   --- ", prom)
                i += 1

def promedio_estudiante(promedios,ctrl):
    for p in promedios:
        if p['_id']==ctrl:
            return p['promedio']
    return 0

def consulta_generalA():
    obj_PyMongo = PyMongo(variablesMongo)
    filtro = {}
    obj_PyMongo.conectar_mongodb()
    lista_estudiantes = obj_PyMongo.consulta_mongodb('estudiantes', filtro)
    lista_promedios = obj_PyMongo.obtener_promedio('kardex')
    obj_PyMongo.desconectar_mongodb()
    for e in lista_estudiantes['resultado']:
        promedio=promedio_estudiante(lista_promedios['resultado'],e['control'])
        print(e['control'],') ',e['nombre'],':',round(promedio))

def eliminar_estudiante():
    obj_PyMongo = PyMongo(variablesMongo)
    print("=== ELIMINAR ESTUDIANTE ===")
    ctrl = input("Ingresa el número de control: ")
    filtro_eliminar = {'control': ctrl}
    obj_PyMongo.conectar_mongodb()
    respuesta1 = obj_PyMongo.consulta_mongodb('estudiantes', filtro_eliminar)
    if respuesta1["status"]:
        obj_PyMongo.eliminar('estudiantes',filtro_eliminar)
        obj_PyMongo.eliminar('kardex', filtro_eliminar)
        obj_PyMongo.eliminar('usuarios', filtro_eliminar)
        print(" ELIMINADO ")

    else:
        print(f"El estudiante con numero de control {ctrl} NO EXISTE")
    obj_PyMongo.desconectar_mongodb()



def menu():
    while True:
        print("\n=========================== MONGO DB ============================");
        print("1, Insertar estudiantes");
        print("2. Actualizar calificaciones");
        print("3. Consultar materia por estudiante");
        print("4. Consulta general de estudiante");
        print("5. Eliminar a un estudiante");
        print("6. Consulta con aaggregate");
        print("7. Salir");
        print("==============================================================");
        print("Dame la opcion que deseas");
        try:
            opcion = int(input(""));
        except Exception as error:
            print("Error: ",error);
            break
        if opcion==1:
            insertar_Estudiante()
        if opcion==2:
            actualizar_calificacion()
        if opcion==3:
            consultar_materias()
        if opcion==4:
            consulta_general()
        if opcion==5:
            eliminar_estudiante()
        if opcion==6:
            consulta_generalA()
        if opcion==7:
            break
    else:
        print("opcion no validad");


# ------------------------------------------------------------ #
#cargar_estudiantes()
menu()

