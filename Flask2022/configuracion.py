class BaseConfig:
    #variables de configuración base
    DEBUG =True
    SECRET_KEY="Palabra_Secreta"
    TESTING=True

class DevConfig(BaseConfig):
    #Variables de la clase padre + adicionales
    pass

class ProdConfig(BaseConfig):
    DEBUG = False
    TESTING = False
