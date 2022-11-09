import pymongo
from variablesMongo import variablesMongo
from crudmysql import MySQL
from Variables import variablesMySQL

class PyMongo():
    def __init__(self, variables):
        self.MONGO_URL = 'mongodb://'+variables["host"]+':'+variables["port"]
        self.MONGO_DATABASE = variables["bd"]
        self.MONGO_TIMEOUT = variables["timeout"]
        self.MONGO_CLIENT = None
        self.MONGO_RESPUESTA = None

    def conectar_mongodb(self):
        try:
            self.MONGO_CLIENT = pymongo.MongoClient(self.MONGO_URL, serverSelectionTimeOutMS = self.MONGO_TIMEOUT) # Conectado

        except Exception as error:
            print(error)
        else:
            print('Conexión al servidor de MongoDB realizada')

    def desconectar_mongodb(self):
        if self.MONGO_CLIENT:
            self.MONGO_CLIENT.close()

    def consulta_mongodb(self, tabla, filtro, atributos={"_id": 0}):
        response = {"status": False, "resultado": []}
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].find(filtro, atributos)
        if self.MONGO_RESPUESTA:
            response["status"] = True
            for reg in self.MONGO_RESPUESTA:
                # print(reg)
                response["resultado"].append(reg)
            # return self.MONGO_RESPUESTA
            # for reg in self.MONGO_RESPUESTA:
            #    print(reg)                                     #ARMAR JSON
        return response

    def consultar_mongodb(self, tabla):
        response = {'status': False, "resultado": []}
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].find({})
        if self.MONGO_RESPUESTA:
            response['status'] = True
            for reg in self.MONGO_RESPUESTA:
                response["resultado"].append(reg)
        return response

    def eliminar(self,tabla,filtro):
        response = {'status': False, "resultado": []}
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].delete_many(filtro)
        if self.MONGO_RESPUESTA:
            response['status'] = True
        return response

    def insertar_estudiante(self,est):
        self.MONGO_RESPUESTA=self.MONGO_CLIENT[self.MONGO_DATABASE]['estudiantes'].insert_one(est)
        if self.MONGO_RESPUESTA:
            return True
        else:
            return False

        # Insertar datos en la coleccion de estudiantes

    def insertar(self, tabla, documento):
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].insert_one(documento)
        if self.MONGO_RESPUESTA:
            return self.MONGO_RESPUESTA
        else:
            return None

       #Cargar alumnos desde archivos
    def cargar_Alumnos(self):
        archivo = open("Estudiantes.prn", "r")
        alumno={}
        for x in archivo:
            ctrl=(x[0:8])
            nom=(x[8:].replace("\n", ""))
            alumno["control"]=ctrl
            alumno["nombre"]=nom
            self.insertar_estudiante(alumno)
            alumno.clear()


    def actualizar(self, collection, filtro, new_values):
        response = {"status": False}
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][collection].update_many(filtro, new_values)
        if self.MONGO_RESPUESTA:
            response = {"status": False}
            # return self.MONGO_RESPUESTA
        # return None
        return response

    def obtener_promedio(self, tabla):
        response = {"status": False, "resultado": []}
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].aggregate(
                [{
                    "$group": {
                    "_id": "$control",
                    "promedio": { "$avg":"$calificacion"}
                            }
                }]
            )
        if self.MONGO_RESPUESTA:
            response["status"] = True
            for reg in self.MONGO_RESPUESTA:
                response["resultado"].append(reg)
        return response


def cargar_estudiantes():
    obj_MySQL = MySQL(variablesMySQL)
    obj_Mongo = PyMongo(variablesMongo)
    sql ="SELECT * FROM estudiantes;"
    obj_MySQL.conectar_mysql()
    lista_estudiantes = obj_MySQL.consulta_sql(sql)
    obj_MySQL.desconectar_mysql()
    obj_Mongo.conectar_mongodb()
    for est in lista_estudiantes:
        e = {
            "control": est[0],
            "nombre": est[1]
        }
        print(e)
        obj_Mongo.insertar('estudiantes', e)
        obj_Mongo.desconectar_mongodb()

    #actualizar documentos en las colecciones

    #Obtener el promedio de estudiantes






#obj_MongoDB = PyMongo(variablesMongo)
#obj_MongoDB.conectar_mongodb()
#obj_MongoDB.cargar_Alumnos()

